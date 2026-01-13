import os
import mne

# ================= 1. parameter choose =================
# file path
file_path = "Acquisition_90_convert.cdt_bl_notch_band_time_03.edf"

# output file
save_path = "processed_epochs-epo.fif"

# parameter
HP, LP = 1.0, 55.0    # Band-pass
NOTCH = 60.0          # Notch
RESAMPLE_FREQ = 500   # Resample
EPOCH_LEN = 5.0       # Epoch time (s)
OVERLAP = 0.0         # overlap length
# ================= 2. 處理流程 =================

def process_single_eeg(path):
    print(f"Processing: {path}")
    
    # 1. load file
    # preload=True 
    raw = mne.io.read_raw_edf(path, preload=True, verbose=False)
    
    # 2.  Montage
    rename_map = {}
    for ch in raw.ch_names:
        # remove noise & transfer to capital  ("EEG Fz-REF" -> "FZ")
        new_name = ch.replace("EEG", "").replace("-REF", "").replace(".", "").strip().upper()
        rename_map[ch] = new_name
    raw.rename_channels(rename_map)
    
    #  10-20 system Montage
    try:
        montage = mne.channels.make_standard_montage("standard_1020")
        raw.set_montage(montage, match_case=False, on_missing='warn')
    except Exception as e:
        print(f"Montage warning: {e}")

    # 3. Rereference 
    #  (Average Reference)
    raw.set_eeg_reference("average", projection=False, verbose=False)
    
    # 4. Band-pass Filter 
    raw.filter(l_freq=HP, h_freq=LP, fir_design="firwin", verbose=False)
    
    # 5. Notch Filter 
    raw.notch_filter(freqs=NOTCH, verbose=False)
    
    # 6. Resample 
    if raw.info['sfreq'] != RESAMPLE_FREQ:
        print(f"Resampling from {raw.info['sfreq']} to {RESAMPLE_FREQ} Hz...")
        raw.resample(RESAMPLE_FREQ, npad="auto")
        
    # 7. Epoch & Extract 
    # make_fixed_length_epochs
    epochs = mne.make_fixed_length_epochs(
        raw, 
        duration=EPOCH_LEN, 
        overlap=OVERLAP, 
        preload=True, 
        verbose=False
    )
    
    return epochs

# ================= 3. initiate & save =================

if os.path.exists(file_path):
    try:
        # processing
        epochs_data = process_single_eeg(file_path)
        
        # Save
        epochs_data.save(save_path, overwrite=True)
        
        print(f"\n[Success] Done！")
        print(f"Epochs num: {len(epochs_data)}")
        print(f"save path: {save_path}")
        
    except Exception as e:
        print(f"\n[Error] fail: {e}")
else:
    print(f"[Error] can't find : {file_path}")
