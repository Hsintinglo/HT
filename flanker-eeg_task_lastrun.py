#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on May 14, 2025, at 13:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pygame'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'flanker_task'  # from the Builder filename that created this script
expInfo = {
    'participant': '21000',
    'session': '1',
    'version': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Exp\\flanker_task\\flanker-eeg_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trigger" ---
# Run 'Begin Experiment' code from eeg_trig
import serial
import time
import threading

Connected = True

# Open the Windows device manager, search for the "TriggerBox VirtualSerial Port (COM6)"
# in "Ports /COM & LPT)" and enter the COM port number in the constructor.
#Setting up the link between psychopy and actiCHAMP
port = serial.Serial("COM4")

# Run 'Begin Experiment' code from ecg_trig
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
begin = visual.TextStim(win=win, name='begin',
    text='Click to begin task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intro" ---
intro_game = visual.MovieStim3(
    win=win, name='intro_game', units='pix',
    noAudio = False,
    filename='stimuli/intro/intro_game.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1920,1080),
    depth=0.0,
    )
key_resp_12 = keyboard.Keyboard()

# --- Initialize components for Routine "remember" ---
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='stimuli/images/gooblemiddle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_14 = keyboard.Keyboard()

# --- Initialize components for Routine "block1_rest" ---
rest_1 = visual.ImageStim(
    win=win,
    name='rest_1', 
    image='stimuli/images/block1_rest.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
animation_1 = visual.MovieStim(
    win, name='animation_1',
    filename='stimuli/animations/block1_animation.mp4', movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=(1920,1080), units='pix',
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)
lets_go = sound.Sound('stimuli/sounds/letsgo.wav', secs=2.0, stereo=True, hamming=True,
    name='lets_go')
lets_go.setVolume(1.0)

# --- Initialize components for Routine "ITI_1" ---
fix_1 = visual.ImageStim(
    win=win,
    name='fix_1', 
    image='stimuli/images/block1_fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "block1" ---
stimuli_1 = visual.ImageStim(
    win=win,
    name='stimuli_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_1 = keyboard.Keyboard()
background_1 = visual.ImageStim(
    win=win,
    name='background_1', 
    image='stimuli/images/block1_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "block2_rest" ---
rest_2 = visual.ImageStim(
    win=win,
    name='rest_2', 
    image='stimuli/images/block2_rest.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
animation_2 = visual.MovieStim3(
    win=win, name='animation_2', units='pix',
    noAudio = False,
    filename='stimuli/animations/block2_animation.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1920,1080),
    depth=-1.0,
    )
lets_go2 = sound.Sound('stimuli/sounds/letsgo.wav', secs=2.0, stereo=True, hamming=True,
    name='lets_go2')
lets_go2.setVolume(1.0)

# --- Initialize components for Routine "ITI_2" ---
fix_2 = visual.ImageStim(
    win=win,
    name='fix_2', 
    image='stimuli/images/block2_fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "block2" ---
stimuli_2 = visual.ImageStim(
    win=win,
    name='stimuli_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
background_2 = visual.ImageStim(
    win=win,
    name='background_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "block3_rest" ---
rest_3 = visual.ImageStim(
    win=win,
    name='rest_3', 
    image='stimuli/images/block3_rest.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
animation_3 = visual.MovieStim3(
    win=win, name='animation_3', units='pix',
    noAudio = False,
    filename='stimuli/animations/block3_animation.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1920,1080),
    depth=-1.0,
    )
lets_go3 = sound.Sound('stimuli/sounds/letsgo.wav', secs=2.0, stereo=True, hamming=True,
    name='lets_go3')
lets_go3.setVolume(1.0)

# --- Initialize components for Routine "ITI_3" ---
fix_3 = visual.ImageStim(
    win=win,
    name='fix_3', 
    image='stimuli/images/block3_fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "block3" ---
stimuli_3 = visual.ImageStim(
    win=win,
    name='stimuli_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()
background_3 = visual.ImageStim(
    win=win,
    name='background_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "block4_rest" ---
rest_4 = visual.ImageStim(
    win=win,
    name='rest_4', 
    image='stimuli/images/block4_rest.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
animation_4 = visual.MovieStim3(
    win=win, name='animation_4', units='pix',
    noAudio = False,
    filename='stimuli/animations/block4_animation.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1920,1080),
    depth=-1.0,
    )
lets_go4 = sound.Sound('stimuli/sounds/letsgo.wav', secs=2.0, stereo=True, hamming=True,
    name='lets_go4')
lets_go4.setVolume(1.0)

# --- Initialize components for Routine "ITI_4" ---
fix_4 = visual.ImageStim(
    win=win,
    name='fix_4', 
    image='stimuli/images/block4_fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "block4" ---
stimuli_4 = visual.ImageStim(
    win=win,
    name='stimuli_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()
background_4 = visual.ImageStim(
    win=win,
    name='background_4', 
    image='stimuli/images/block4_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "block5_rest" ---
rest_5 = visual.ImageStim(
    win=win,
    name='rest_5', 
    image='stimuli/images/block5_rest.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
animation_5 = visual.MovieStim3(
    win=win, name='animation_5', units='pix',
    noAudio = False,
    filename='stimuli/animations/block5_animation.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1920,1080),
    depth=-1.0,
    )
lets_go5 = sound.Sound('stimuli/sounds/letsgo.wav', secs=2.0, stereo=True, hamming=True,
    name='lets_go5')
lets_go5.setVolume(1.0)

# --- Initialize components for Routine "ITI_5" ---
fix_5 = visual.ImageStim(
    win=win,
    name='fix_5', 
    image='stimuli/images/block5_fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "block5" ---
stimuli_5 = visual.ImageStim(
    win=win,
    name='stimuli_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()
background_5 = visual.ImageStim(
    win=win,
    name='background_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "end" ---
end_scene = visual.MovieStim3(
    win=win, name='end_scene', units='pix',
    noAudio = False,
    filename='stimuli/animations/endscene_animation.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=(1920,1080),
    depth=0.0,
    )

# --- Initialize components for Routine "endslide" ---
endscene_text = visual.ImageStim(
    win=win,
    name='endscene_text', 
    image='stimuli/images/endscene_text.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.255),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "trigger" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
triggerComponents = [begin, key_resp]
for thisComponent in triggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trigger" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin* updates
    if begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin.frameNStart = frameN  # exact frame index
        begin.tStart = t  # local t and not account for scr refresh
        begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'begin.started')
        begin.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trigger" ---
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
introComponents = [intro_game, key_resp_12]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_game* updates
    if intro_game.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_game.frameNStart = frameN  # exact frame index
        intro_game.tStart = t  # local t and not account for scr refresh
        intro_game.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_game, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_game.started')
        intro_game.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_12.started')
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
intro_game.stop()
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "remember" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
rememberComponents = [image_11, key_resp_14]
for thisComponent in rememberComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "remember" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_11.started')
        image_11.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_14.started')
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rememberComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "remember" ---
for thisComponent in rememberComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()
# the Routine "remember" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "block1_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
lets_go.setSound('stimuli/sounds/letsgo.wav', secs=2.0, hamming=True)
lets_go.setVolume(1.0, log=False)
# keep track of which components have finished
block1_restComponents = [rest_1, animation_1, lets_go]
for thisComponent in block1_restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "block1_rest" ---
while continueRoutine and routineTimer.getTime() < 27.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_1* updates
    if rest_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_1.frameNStart = frameN  # exact frame index
        rest_1.tStart = t  # local t and not account for scr refresh
        rest_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_1.started')
        rest_1.setAutoDraw(True)
    if rest_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_1.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            rest_1.tStop = t  # not accounting for scr refresh
            rest_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_1.stopped')
            rest_1.setAutoDraw(False)
    
    # *animation_1* updates
    if animation_1.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        animation_1.frameNStart = frameN  # exact frame index
        animation_1.tStart = t  # local t and not account for scr refresh
        animation_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(animation_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'animation_1.started')
        animation_1.setAutoDraw(True)
        animation_1.play()
    if animation_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > animation_1.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            animation_1.tStop = t  # not accounting for scr refresh
            animation_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'animation_1.stopped')
            animation_1.setAutoDraw(False)
            animation_1.stop()
    # start/stop lets_go
    if lets_go.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        # keep track of start time/frame for later
        lets_go.frameNStart = frameN  # exact frame index
        lets_go.tStart = t  # local t and not account for scr refresh
        lets_go.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('lets_go.started', tThisFlipGlobal)
        lets_go.play(when=win)  # sync with win flip
    if lets_go.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lets_go.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            lets_go.tStop = t  # not accounting for scr refresh
            lets_go.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lets_go.stopped')
            lets_go.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block1_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "block1_rest" ---
for thisComponent in block1_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
animation_1.stop()
lets_go.stop()  # ensure sound has stopped at end of routine
# Run 'End Routine' code from strt_mrkr_1
#  Stim marker: start of block1
port.write([0x01])

# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-27.000000)

# set up handler to look after randomisation of conditions etc
block1_trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/block1_conditions.xlsx'),
    seed=None, name='block1_trial')
thisExp.addLoop(block1_trial)  # add the loop to the experiment
thisBlock1_trial = block1_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1_trial.rgb)
if thisBlock1_trial != None:
    for paramName in thisBlock1_trial:
        exec('{} = thisBlock1_trial[paramName]'.format(paramName))

for thisBlock1_trial in block1_trial:
    currentLoop = block1_trial
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1_trial.rgb)
    if thisBlock1_trial != None:
        for paramName in thisBlock1_trial:
            exec('{} = thisBlock1_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ITI_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from jitter_1
    #jitter is randomized between 1.3 and 1.7
    jitter = random() * (1.7 - 1.3) + 1.3
    
    # keep track of which components have finished
    ITI_1Components = [fix_1]
    for thisComponent in ITI_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_1* updates
        if fix_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_1.frameNStart = frameN  # exact frame index
            fix_1.tStart = t  # local t and not account for scr refresh
            fix_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_1.started')
            fix_1.setAutoDraw(True)
        if fix_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_1.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                fix_1.tStop = t  # not accounting for scr refresh
                fix_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_1.stopped')
                fix_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_1" ---
    for thisComponent in ITI_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from jitter_1
    #to save jitter to data sheet
    thisExp.addData('jitter', jitter)
    # the Routine "ITI_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stimuli_1.setImage(stimuli_file)
    key_resp_1.keys = []
    key_resp_1.rt = []
    _key_resp_1_allKeys = []
    # Run 'Begin Routine' code from stim_mrkr_1
    responded = False
    
    # set congruent bool based off filename of stim image
    if stimuli_1.image.replace('.png', '').split('_')[-1][0] == 'C':
        congruent = True
    elif stimuli_1.image.replace('.png', '').split('_')[-1][0] == 'I':
        congruent = False
    else:
        congruent = None
        
    # set directionality of stim image as well
    if stimuli_1.image.replace('.png', '').split('_')[-1][1] == 'R':
        direction = 'right'
    elif stimuli_1.image.replace('.png', '').split('_')[-1][1] == 'L':
        direction = 'left'
    else: # neither direction was true?
        direction = None
    
    if congruent is True: 
        # write 0A / 10
        port.write([0x0A])
    elif congruent is False:
        # write 0B / 12
        port.write([0x0C])
    #else: # else was neither congruent nor incongruent?
        # write error FF / 255
    #    port.write([0xFF])
        
    
    # keep track of which components have finished
    block1Components = [stimuli_1, key_resp_1, background_1]
    for thisComponent in block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block1" ---
    while continueRoutine and routineTimer.getTime() < 1.65:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli_1* updates
        if stimuli_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_1.frameNStart = frameN  # exact frame index
            stimuli_1.tStart = t  # local t and not account for scr refresh
            stimuli_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuli_1.started')
            stimuli_1.setAutoDraw(True)
        if stimuli_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_1.tStop = t  # not accounting for scr refresh
                stimuli_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_1.stopped')
                stimuli_1.setAutoDraw(False)
        
        # *key_resp_1* updates
        waitOnFlip = False
        if key_resp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_1.frameNStart = frameN  # exact frame index
            key_resp_1.tStart = t  # local t and not account for scr refresh
            key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1.started')
            key_resp_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_1.tStartRefresh + 1.65-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_1.tStop = t  # not accounting for scr refresh
                key_resp_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1.stopped')
                key_resp_1.status = FINISHED
        if key_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_1_allKeys.extend(theseKeys)
            if len(_key_resp_1_allKeys):
                key_resp_1.keys = _key_resp_1_allKeys[0].name  # just the first key pressed
                key_resp_1.rt = _key_resp_1_allKeys[0].rt
                # was this correct?
                if (key_resp_1.keys == str(corrAns)) or (key_resp_1.keys == corrAns):
                    key_resp_1.corr = 1
                else:
                    key_resp_1.corr = 0
        
        # *background_1* updates
        if background_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            background_1.frameNStart = frameN  # exact frame index
            background_1.tStart = t  # local t and not account for scr refresh
            background_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_1.started')
            background_1.setAutoDraw(True)
        if background_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_1.tStartRefresh + 0.65-frameTolerance:
                # keep track of stop time/frame for later
                background_1.tStop = t  # not accounting for scr refresh
                background_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_1.stopped')
                background_1.setAutoDraw(False)
        # Run 'Each Frame' code from stim_mrkr_1
        if len(key_resp_1.keys) != 0:
            if not responded:
        #        port.write([0x04])
                responded = True
                
                # if answer is correct
                if key_resp_1.keys == direction:
                    # write 0C / 14
                    port.write([0x0E])
                elif key_resp_1.keys != direction:
                    # write 0D / 15
                    port.write([0x0F])
                    
        if congruent is True and stimuli_1.status==FINISHED: 
            # write 0B / 11
            port.write([0x0B])
        elif congruent is False and stimuli_1.status==FINISHED:
            # write 0B / 13
            port.write([0x0D])
        #else: 
        #    port.write([0xFF])
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block1" ---
    for thisComponent in block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_1.keys in ['', [], None]:  # No response was made
        key_resp_1.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_1.corr = 1;  # correct non-response
        else:
           key_resp_1.corr = 0;  # failed to respond (incorrectly)
    # store data for block1_trial (TrialHandler)
    block1_trial.addData('key_resp_1.keys',key_resp_1.keys)
    block1_trial.addData('key_resp_1.corr', key_resp_1.corr)
    if key_resp_1.keys != None:  # we had a response
        block1_trial.addData('key_resp_1.rt', key_resp_1.rt)
    # Run 'End Routine' code from stim_mrkr_1
    if not responded: #missed trial marker 16
        port.write([0x10])
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.650000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block1_trial'


# --- Prepare to start Routine "block2_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
lets_go2.setSound('stimuli/sounds/letsgo.wav', secs=2.0, hamming=True)
lets_go2.setVolume(1.0, log=False)
# Run 'Begin Routine' code from strt_mrkr_2
#  Stim marker: end of block1
port.write([0x02])

# keep track of which components have finished
block2_restComponents = [rest_2, animation_2, lets_go2]
for thisComponent in block2_restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "block2_rest" ---
while continueRoutine and routineTimer.getTime() < 27.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_2* updates
    if rest_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_2.frameNStart = frameN  # exact frame index
        rest_2.tStart = t  # local t and not account for scr refresh
        rest_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_2.started')
        rest_2.setAutoDraw(True)
    if rest_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_2.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            rest_2.tStop = t  # not accounting for scr refresh
            rest_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_2.stopped')
            rest_2.setAutoDraw(False)
    
    # *animation_2* updates
    if animation_2.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        animation_2.frameNStart = frameN  # exact frame index
        animation_2.tStart = t  # local t and not account for scr refresh
        animation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(animation_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'animation_2.started')
        animation_2.setAutoDraw(True)
    if animation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > animation_2.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            animation_2.tStop = t  # not accounting for scr refresh
            animation_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'animation_2.stopped')
            animation_2.setAutoDraw(False)
    # start/stop lets_go2
    if lets_go2.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
        # keep track of start time/frame for later
        lets_go2.frameNStart = frameN  # exact frame index
        lets_go2.tStart = t  # local t and not account for scr refresh
        lets_go2.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('lets_go2.started', tThisFlipGlobal)
        lets_go2.play(when=win)  # sync with win flip
    if lets_go2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lets_go2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            lets_go2.tStop = t  # not accounting for scr refresh
            lets_go2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lets_go2.stopped')
            lets_go2.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block2_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "block2_rest" ---
for thisComponent in block2_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
animation_2.stop()
lets_go2.stop()  # ensure sound has stopped at end of routine
# Run 'End Routine' code from strt_mrkr_2
#  Start of block2
port.write([0x01])
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-27.000000)

# set up handler to look after randomisation of conditions etc
block2_trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/block2_conditions.xlsx'),
    seed=None, name='block2_trial')
thisExp.addLoop(block2_trial)  # add the loop to the experiment
thisBlock2_trial = block2_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2_trial.rgb)
if thisBlock2_trial != None:
    for paramName in thisBlock2_trial:
        exec('{} = thisBlock2_trial[paramName]'.format(paramName))

for thisBlock2_trial in block2_trial:
    currentLoop = block2_trial
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2_trial.rgb)
    if thisBlock2_trial != None:
        for paramName in thisBlock2_trial:
            exec('{} = thisBlock2_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ITI_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from jitter_2
    #jitter is randomized between 1.3 and 1.7
    jitter = random() * (1.7 - 1.3) + 1.3
    # keep track of which components have finished
    ITI_2Components = [fix_2]
    for thisComponent in ITI_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_2* updates
        if fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_2.frameNStart = frameN  # exact frame index
            fix_2.tStart = t  # local t and not account for scr refresh
            fix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_2.started')
            fix_2.setAutoDraw(True)
        if fix_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_2.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                fix_2.tStop = t  # not accounting for scr refresh
                fix_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_2.stopped')
                fix_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_2" ---
    for thisComponent in ITI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from jitter_2
    thisExp.addData('jitter', jitter)
    # the Routine "ITI_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stimuli_2.setImage(stimuli_file)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    background_2.setImage('stimuli/images/block2_background.png')
    # Run 'Begin Routine' code from stim_mrkr_2
    responded = False
    
    # set congruent bool based off filename of stim image
    if stimuli_2.image.replace('.png', '').split('_')[-1][0] == 'C':
        congruent = True
    elif stimuli_2.image.replace('.png', '').split('_')[-1][0] == 'I':
        congruent = False
    else:
        congruent = None
        
    # set directionality of stim image as well
    if stimuli_2.image.replace('.png', '').split('_')[-1][1] == 'R':
        direction = 'right'
    elif stimuli_2.image.replace('.png', '').split('_')[-1][1] == 'L':
        direction = 'left'
    else: # neither direction was true?
        direction = None
    
    if congruent is True: 
        # write 0A / 10
        port.write([0x0A])
    elif congruent is False:
        # write 0B / 12
        port.write([0x0C])
    #else: # else was neither congruent nor incongruent?
        # write error FF / 255
    #    port.write([0xFF])
        
    # keep track of which components have finished
    block2Components = [stimuli_2, key_resp_2, background_2]
    for thisComponent in block2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block2" ---
    while continueRoutine and routineTimer.getTime() < 1.65:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli_2* updates
        if stimuli_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_2.frameNStart = frameN  # exact frame index
            stimuli_2.tStart = t  # local t and not account for scr refresh
            stimuli_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuli_2.started')
            stimuli_2.setAutoDraw(True)
        if stimuli_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_2.tStop = t  # not accounting for scr refresh
                stimuli_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_2.stopped')
                stimuli_2.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.65-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
        
        # *background_2* updates
        if background_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            background_2.frameNStart = frameN  # exact frame index
            background_2.tStart = t  # local t and not account for scr refresh
            background_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_2.started')
            background_2.setAutoDraw(True)
        if background_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_2.tStartRefresh + 0.65-frameTolerance:
                # keep track of stop time/frame for later
                background_2.tStop = t  # not accounting for scr refresh
                background_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_2.stopped')
                background_2.setAutoDraw(False)
        # Run 'Each Frame' code from stim_mrkr_2
        if len(key_resp_2.keys) != 0:
            if not responded:
        #        port.write([0x04])
                responded = True
                
                # if answer is correct
                if key_resp_2.keys == direction:
                    # write 0C / 14
                    port.write([0x0E])
                elif key_resp_2.keys != direction:
                    # write 0D / 15
                    port.write([0x0F])
                    
        if congruent is True and stimuli_2.status==FINISHED: 
            # write 0B / 11
            port.write([0x0B])
        elif congruent is False and stimuli_2.status==FINISHED:
            # write 0B / 13
            port.write([0x0D])
        #else: 
        #    port.write([0xFF])
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block2" ---
    for thisComponent in block2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for block2_trial (TrialHandler)
    block2_trial.addData('key_resp_2.keys',key_resp_2.keys)
    block2_trial.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        block2_trial.addData('key_resp_2.rt', key_resp_2.rt)
    # Run 'End Routine' code from stim_mrkr_2
    if not responded: #missed trial marker 16
        port.write([0x10])
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.650000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block2_trial'


# --- Prepare to start Routine "block3_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
lets_go3.setSound('stimuli/sounds/letsgo.wav', secs=2.0, hamming=True)
lets_go3.setVolume(1.0, log=False)
# Run 'Begin Routine' code from strt_mrkr_3
#  Stim marker: end of block2
port.write([0x02])
# keep track of which components have finished
block3_restComponents = [rest_3, animation_3, lets_go3]
for thisComponent in block3_restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "block3_rest" ---
while continueRoutine and routineTimer.getTime() < 27.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_3* updates
    if rest_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_3.frameNStart = frameN  # exact frame index
        rest_3.tStart = t  # local t and not account for scr refresh
        rest_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_3.started')
        rest_3.setAutoDraw(True)
    if rest_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_3.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            rest_3.tStop = t  # not accounting for scr refresh
            rest_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_3.stopped')
            rest_3.setAutoDraw(False)
    
    # *animation_3* updates
    if animation_3.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        animation_3.frameNStart = frameN  # exact frame index
        animation_3.tStart = t  # local t and not account for scr refresh
        animation_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(animation_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'animation_3.started')
        animation_3.setAutoDraw(True)
    if animation_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > animation_3.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            animation_3.tStop = t  # not accounting for scr refresh
            animation_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'animation_3.stopped')
            animation_3.setAutoDraw(False)
    # start/stop lets_go3
    if lets_go3.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        lets_go3.frameNStart = frameN  # exact frame index
        lets_go3.tStart = t  # local t and not account for scr refresh
        lets_go3.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('lets_go3.started', tThisFlipGlobal)
        lets_go3.play(when=win)  # sync with win flip
    if lets_go3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lets_go3.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            lets_go3.tStop = t  # not accounting for scr refresh
            lets_go3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lets_go3.stopped')
            lets_go3.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block3_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "block3_rest" ---
for thisComponent in block3_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
animation_3.stop()
lets_go3.stop()  # ensure sound has stopped at end of routine
# Run 'End Routine' code from strt_mrkr_3
#  Start of block3
port.write([0x01])
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-27.000000)

# set up handler to look after randomisation of conditions etc
block3_trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/block3_conditions.xlsx'),
    seed=None, name='block3_trial')
thisExp.addLoop(block3_trial)  # add the loop to the experiment
thisBlock3_trial = block3_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3_trial.rgb)
if thisBlock3_trial != None:
    for paramName in thisBlock3_trial:
        exec('{} = thisBlock3_trial[paramName]'.format(paramName))

for thisBlock3_trial in block3_trial:
    currentLoop = block3_trial
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3_trial.rgb)
    if thisBlock3_trial != None:
        for paramName in thisBlock3_trial:
            exec('{} = thisBlock3_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ITI_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from jitter_3
    #jitter is randomized between 1.3 and 1.7
    jitter = random() * (1.7 - 1.3) + 1.3
    # keep track of which components have finished
    ITI_3Components = [fix_3]
    for thisComponent in ITI_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_3* updates
        if fix_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_3.frameNStart = frameN  # exact frame index
            fix_3.tStart = t  # local t and not account for scr refresh
            fix_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_3.started')
            fix_3.setAutoDraw(True)
        if fix_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_3.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                fix_3.tStop = t  # not accounting for scr refresh
                fix_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_3.stopped')
                fix_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_3" ---
    for thisComponent in ITI_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from jitter_3
    thisExp.addData('jitter', jitter)
    # the Routine "ITI_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stimuli_3.setImage(stimuli_file)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    background_3.setImage('stimuli/images/block3_background.png')
    # Run 'Begin Routine' code from stim_mrkr_3
    responded = False
    
    # set congruent bool based off filename of stim image
    if stimuli_3.image.replace('.png', '').split('_')[-1][0] == 'C':
        congruent = True
    elif stimuli_3.image.replace('.png', '').split('_')[-1][0] == 'I':
        congruent = False
    else:
        congruent = None
        
    # set directionality of stim image as well
    if stimuli_3.image.replace('.png', '').split('_')[-1][1] == 'R':
        direction = 'right'
    elif stimuli_3.image.replace('.png', '').split('_')[-1][1] == 'L':
        direction = 'left'
    else: # neither direction was true?
        direction = None
    
    if congruent is True: 
        # write 0A / 10
        port.write([0x0A])
    elif congruent is False:
        # write 0B / 12
        port.write([0x0C])
    #else: # else was neither congruent nor incongruent?
        # write error FF / 255
    #    port.write([0xFF])
        
    # keep track of which components have finished
    block3Components = [stimuli_3, key_resp_3, background_3]
    for thisComponent in block3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block3" ---
    while continueRoutine and routineTimer.getTime() < 1.65:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli_3* updates
        if stimuli_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_3.frameNStart = frameN  # exact frame index
            stimuli_3.tStart = t  # local t and not account for scr refresh
            stimuli_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuli_3.started')
            stimuli_3.setAutoDraw(True)
        if stimuli_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_3.tStop = t  # not accounting for scr refresh
                stimuli_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_3.stopped')
                stimuli_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 1.65-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[0].name  # just the first key pressed
                key_resp_3.rt = _key_resp_3_allKeys[0].rt
                # was this correct?
                if (key_resp_3.keys == str(corrAns)) or (key_resp_3.keys == corrAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
        
        # *background_3* updates
        if background_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            background_3.frameNStart = frameN  # exact frame index
            background_3.tStart = t  # local t and not account for scr refresh
            background_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_3.started')
            background_3.setAutoDraw(True)
        if background_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_3.tStartRefresh + 0.65-frameTolerance:
                # keep track of stop time/frame for later
                background_3.tStop = t  # not accounting for scr refresh
                background_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_3.stopped')
                background_3.setAutoDraw(False)
        # Run 'Each Frame' code from stim_mrkr_3
        if len(key_resp_3.keys) != 0:
            if not responded:
        #        port.write([0x04])
                responded = True
                
                # if answer is correct
                if key_resp_3.keys == direction:
                    # write 0C / 14
                    port.write([0x0E])
                elif key_resp_3.keys != direction:
                    # write 0D / 15
                    port.write([0x0F])
                    
        if congruent is True and stimuli_3.status==FINISHED: 
            # write 0B / 11
            port.write([0x0B])
        elif congruent is False and stimuli_3.status==FINISHED:
            # write 0B / 13
            port.write([0x0D])
        #else: 
        #    port.write([0xFF])
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block3" ---
    for thisComponent in block3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for block3_trial (TrialHandler)
    block3_trial.addData('key_resp_3.keys',key_resp_3.keys)
    block3_trial.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        block3_trial.addData('key_resp_3.rt', key_resp_3.rt)
    # Run 'End Routine' code from stim_mrkr_3
    if not responded: #missed trial marker 16
        port.write([0x10])
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.650000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block3_trial'


# --- Prepare to start Routine "block4_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
lets_go4.setSound('stimuli/sounds/letsgo.wav', secs=2.0, hamming=True)
lets_go4.setVolume(1.0, log=False)
# Run 'Begin Routine' code from strt_mrkr_4
#  Stim marker: end of block3
port.write([0x02])
# keep track of which components have finished
block4_restComponents = [rest_4, animation_4, lets_go4]
for thisComponent in block4_restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "block4_rest" ---
while continueRoutine and routineTimer.getTime() < 27.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_4* updates
    if rest_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_4.frameNStart = frameN  # exact frame index
        rest_4.tStart = t  # local t and not account for scr refresh
        rest_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_4.started')
        rest_4.setAutoDraw(True)
    if rest_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_4.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            rest_4.tStop = t  # not accounting for scr refresh
            rest_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_4.stopped')
            rest_4.setAutoDraw(False)
    
    # *animation_4* updates
    if animation_4.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        animation_4.frameNStart = frameN  # exact frame index
        animation_4.tStart = t  # local t and not account for scr refresh
        animation_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(animation_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'animation_4.started')
        animation_4.setAutoDraw(True)
    if animation_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > animation_4.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            animation_4.tStop = t  # not accounting for scr refresh
            animation_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'animation_4.stopped')
            animation_4.setAutoDraw(False)
    # start/stop lets_go4
    if lets_go4.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        lets_go4.frameNStart = frameN  # exact frame index
        lets_go4.tStart = t  # local t and not account for scr refresh
        lets_go4.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('lets_go4.started', tThisFlipGlobal)
        lets_go4.play(when=win)  # sync with win flip
    if lets_go4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lets_go4.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            lets_go4.tStop = t  # not accounting for scr refresh
            lets_go4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lets_go4.stopped')
            lets_go4.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block4_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "block4_rest" ---
for thisComponent in block4_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
animation_4.stop()
lets_go4.stop()  # ensure sound has stopped at end of routine
# Run 'End Routine' code from strt_mrkr_4
#  Start of block4
port.write([0x01])
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-27.000000)

# set up handler to look after randomisation of conditions etc
block4_trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/block4_conditions.xlsx'),
    seed=None, name='block4_trial')
thisExp.addLoop(block4_trial)  # add the loop to the experiment
thisBlock4_trial = block4_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock4_trial.rgb)
if thisBlock4_trial != None:
    for paramName in thisBlock4_trial:
        exec('{} = thisBlock4_trial[paramName]'.format(paramName))

for thisBlock4_trial in block4_trial:
    currentLoop = block4_trial
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4_trial.rgb)
    if thisBlock4_trial != None:
        for paramName in thisBlock4_trial:
            exec('{} = thisBlock4_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ITI_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from jitter_4
    #jitter is randomized between 1.3 and 1.7
    jitter = random() * (1.7 - 1.3) + 1.3
    # keep track of which components have finished
    ITI_4Components = [fix_4]
    for thisComponent in ITI_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_4* updates
        if fix_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_4.frameNStart = frameN  # exact frame index
            fix_4.tStart = t  # local t and not account for scr refresh
            fix_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_4.started')
            fix_4.setAutoDraw(True)
        if fix_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_4.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                fix_4.tStop = t  # not accounting for scr refresh
                fix_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_4.stopped')
                fix_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_4" ---
    for thisComponent in ITI_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from jitter_4
    thisExp.addData('jitter', jitter)
    # the Routine "ITI_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stimuli_4.setImage(stimuli_file)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # Run 'Begin Routine' code from stim_mrkr_4
    responded = False
    
    # set congruent bool based off filename of stim image
    if stimuli_4.image.replace('.png', '').split('_')[-1][0] == 'C':
        congruent = True
    elif stimuli_4.image.replace('.png', '').split('_')[-1][0] == 'I':
        congruent = False
    else:
        congruent = None
        
    # set directionality of stim image as well
    if stimuli_4.image.replace('.png', '').split('_')[-1][1] == 'R':
        direction = 'right'
    elif stimuli_4.image.replace('.png', '').split('_')[-1][1] == 'L':
        direction = 'left'
    else: # neither direction was true?
        direction = None
    
    if congruent is True: 
        # write 0A / 10
        port.write([0x0A])
    elif congruent is False:
        # write 0B / 12
        port.write([0x0C])
    #else: # else was neither congruent nor incongruent?
        # write error FF / 255
    #    port.write([0xFF])
        
    # keep track of which components have finished
    block4Components = [stimuli_4, key_resp_4, background_4]
    for thisComponent in block4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block4" ---
    while continueRoutine and routineTimer.getTime() < 1.65:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli_4* updates
        if stimuli_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_4.frameNStart = frameN  # exact frame index
            stimuli_4.tStart = t  # local t and not account for scr refresh
            stimuli_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuli_4.started')
            stimuli_4.setAutoDraw(True)
        if stimuli_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_4.tStop = t  # not accounting for scr refresh
                stimuli_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_4.stopped')
                stimuli_4.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 1.65-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[0].name  # just the first key pressed
                key_resp_4.rt = _key_resp_4_allKeys[0].rt
                # was this correct?
                if (key_resp_4.keys == str(corrAns)) or (key_resp_4.keys == corrAns):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
        
        # *background_4* updates
        if background_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            background_4.frameNStart = frameN  # exact frame index
            background_4.tStart = t  # local t and not account for scr refresh
            background_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_4.started')
            background_4.setAutoDraw(True)
        if background_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_4.tStartRefresh + 0.65-frameTolerance:
                # keep track of stop time/frame for later
                background_4.tStop = t  # not accounting for scr refresh
                background_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_4.stopped')
                background_4.setAutoDraw(False)
        # Run 'Each Frame' code from stim_mrkr_4
        if len(key_resp_4.keys) != 0:
            if not responded:
        #        port.write([0x04])
                responded = True
                
                # if answer is correct
                if key_resp_4.keys == direction:
                    # write 0C / 14
                    port.write([0x0E])
                elif key_resp_4.keys != direction:
                    # write 0D / 15
                    port.write([0x0F])
                    
        if congruent is True and stimuli_4.status==FINISHED: 
            # write 0B / 11
            port.write([0x0B])
        elif congruent is False and stimuli_4.status==FINISHED:
            # write 0B / 13
            port.write([0x0D])
        #else: 
        #    port.write([0xFF])
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block4" ---
    for thisComponent in block4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for block4_trial (TrialHandler)
    block4_trial.addData('key_resp_4.keys',key_resp_4.keys)
    block4_trial.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        block4_trial.addData('key_resp_4.rt', key_resp_4.rt)
    # Run 'End Routine' code from stim_mrkr_4
    if not responded: #missed trial marker 16
        port.write([0x10])
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.650000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block4_trial'


# --- Prepare to start Routine "block5_rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
lets_go5.setSound('stimuli/sounds/letsgo.wav', secs=2.0, hamming=True)
lets_go5.setVolume(1.0, log=False)
# Run 'Begin Routine' code from strt_mrkr_5
#  Stim marker: end of block4
port.write([0x02])
# keep track of which components have finished
block5_restComponents = [rest_5, animation_5, lets_go5]
for thisComponent in block5_restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "block5_rest" ---
while continueRoutine and routineTimer.getTime() < 27.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_5* updates
    if rest_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_5.frameNStart = frameN  # exact frame index
        rest_5.tStart = t  # local t and not account for scr refresh
        rest_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_5.started')
        rest_5.setAutoDraw(True)
    if rest_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_5.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            rest_5.tStop = t  # not accounting for scr refresh
            rest_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_5.stopped')
            rest_5.setAutoDraw(False)
    
    # *animation_5* updates
    if animation_5.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        animation_5.frameNStart = frameN  # exact frame index
        animation_5.tStart = t  # local t and not account for scr refresh
        animation_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(animation_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'animation_5.started')
        animation_5.setAutoDraw(True)
    if animation_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > animation_5.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            animation_5.tStop = t  # not accounting for scr refresh
            animation_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'animation_5.stopped')
            animation_5.setAutoDraw(False)
    # start/stop lets_go5
    if lets_go5.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
        # keep track of start time/frame for later
        lets_go5.frameNStart = frameN  # exact frame index
        lets_go5.tStart = t  # local t and not account for scr refresh
        lets_go5.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('lets_go5.started', tThisFlipGlobal)
        lets_go5.play(when=win)  # sync with win flip
    if lets_go5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lets_go5.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            lets_go5.tStop = t  # not accounting for scr refresh
            lets_go5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lets_go5.stopped')
            lets_go5.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block5_restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "block5_rest" ---
for thisComponent in block5_restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
animation_5.stop()
lets_go5.stop()  # ensure sound has stopped at end of routine
# Run 'End Routine' code from strt_mrkr_5
#  Start of block5
port.write([0x01])
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-27.000000)

# set up handler to look after randomisation of conditions etc
block5_trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/block5_conditions - Copy.xlsx'),
    seed=None, name='block5_trial')
thisExp.addLoop(block5_trial)  # add the loop to the experiment
thisBlock5_trial = block5_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock5_trial.rgb)
if thisBlock5_trial != None:
    for paramName in thisBlock5_trial:
        exec('{} = thisBlock5_trial[paramName]'.format(paramName))

for thisBlock5_trial in block5_trial:
    currentLoop = block5_trial
    # abbreviate parameter names if possible (e.g. rgb = thisBlock5_trial.rgb)
    if thisBlock5_trial != None:
        for paramName in thisBlock5_trial:
            exec('{} = thisBlock5_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ITI_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from jitter_5
    #jitter is randomized between 1.3 and 1.7
    jitter = random() * (1.7 - 1.3) + 1.3
    # keep track of which components have finished
    ITI_5Components = [fix_5]
    for thisComponent in ITI_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI_5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_5* updates
        if fix_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_5.frameNStart = frameN  # exact frame index
            fix_5.tStart = t  # local t and not account for scr refresh
            fix_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_5.started')
            fix_5.setAutoDraw(True)
        if fix_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_5.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                fix_5.tStop = t  # not accounting for scr refresh
                fix_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_5.stopped')
                fix_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_5" ---
    for thisComponent in ITI_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from jitter_5
    thisExp.addData('jitter', jitter)
    # the Routine "ITI_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stimuli_5.setImage(stimuli_file)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    background_5.setImage('stimuli/images/block5_background.png')
    # Run 'Begin Routine' code from stim_mrkr_5
    responded = False
    
    # set congruent bool based off filename of stim image
    if stimuli_5.image.replace('.png', '').split('_')[-1][0] == 'C':
        congruent = True
    elif stimuli_5.image.replace('.png', '').split('_')[-1][0] == 'I':
        congruent = False
    else:
        congruent = None
        
    # set directionality of stim image as well
    if stimuli_5.image.replace('.png', '').split('_')[-1][1] == 'R':
        direction = 'right'
    elif stimuli_5.image.replace('.png', '').split('_')[-1][1] == 'L':
        direction = 'left'
    else: # neither direction was true?
        direction = None
    
    if congruent is True: 
        # write 0A / 10
        port.write([0x0A])
    elif congruent is False:
        # write 0B / 12
        port.write([0x0C])
    #else: # else was neither congruent nor incongruent?
        # write error FF / 255
    #    port.write([0xFF])
        
    # keep track of which components have finished
    block5Components = [stimuli_5, key_resp_5, background_5]
    for thisComponent in block5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block5" ---
    while continueRoutine and routineTimer.getTime() < 1.65:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli_5* updates
        if stimuli_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_5.frameNStart = frameN  # exact frame index
            stimuli_5.tStart = t  # local t and not account for scr refresh
            stimuli_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stimuli_5.started')
            stimuli_5.setAutoDraw(True)
        if stimuli_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_5.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_5.tStop = t  # not accounting for scr refresh
                stimuli_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimuli_5.stopped')
                stimuli_5.setAutoDraw(False)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_5.tStartRefresh + 1.65-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[0].name  # just the first key pressed
                key_resp_5.rt = _key_resp_5_allKeys[0].rt
                # was this correct?
                if (key_resp_5.keys == str(corrAns)) or (key_resp_5.keys == corrAns):
                    key_resp_5.corr = 1
                else:
                    key_resp_5.corr = 0
        
        # *background_5* updates
        if background_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            background_5.frameNStart = frameN  # exact frame index
            background_5.tStart = t  # local t and not account for scr refresh
            background_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_5.started')
            background_5.setAutoDraw(True)
        if background_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_5.tStartRefresh + 0.65-frameTolerance:
                # keep track of stop time/frame for later
                background_5.tStop = t  # not accounting for scr refresh
                background_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_5.stopped')
                background_5.setAutoDraw(False)
        # Run 'Each Frame' code from stim_mrkr_5
        if len(key_resp_5.keys) != 0:
            if not responded:
        #        port.write([0x04])
                responded = True
                
                # if answer is correct
                if key_resp_5.keys == direction:
                    # write 0C / 14
                    port.write([0x0E])
                elif key_resp_5.keys != direction:
                    # write 0D / 15
                    port.write([0x0F])
                    
        if congruent is True and stimuli_5.status==FINISHED: 
            # write 0B / 11
            port.write([0x0B])
        elif congruent is False and stimuli_5.status==FINISHED:
            # write 0B / 13
            port.write([0x0D])
        #else: 
        #    port.write([0xFF])
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block5" ---
    for thisComponent in block5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_5.corr = 1;  # correct non-response
        else:
           key_resp_5.corr = 0;  # failed to respond (incorrectly)
    # store data for block5_trial (TrialHandler)
    block5_trial.addData('key_resp_5.keys',key_resp_5.keys)
    block5_trial.addData('key_resp_5.corr', key_resp_5.corr)
    if key_resp_5.keys != None:  # we had a response
        block5_trial.addData('key_resp_5.rt', key_resp_5.rt)
    # Run 'End Routine' code from stim_mrkr_5
    if not responded: #missed trial marker 16
        port.write([0x10])
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.650000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'block5_trial'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from end_mrkr_5
#  Stim marker: end of block5
port.write([0x02])
# keep track of which components have finished
endComponents = [end_scene]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_scene* updates
    if end_scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_scene.frameNStart = frameN  # exact frame index
        end_scene.tStart = t  # local t and not account for scr refresh
        end_scene.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_scene, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_scene.started')
        end_scene.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
end_scene.stop()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "endslide" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
endslideComponents = [endscene_text]
for thisComponent in endslideComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "endslide" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endscene_text* updates
    if endscene_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endscene_text.frameNStart = frameN  # exact frame index
        endscene_text.tStart = t  # local t and not account for scr refresh
        endscene_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endscene_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endscene_text.started')
        endscene_text.setAutoDraw(True)
    if endscene_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endscene_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            endscene_text.tStop = t  # not accounting for scr refresh
            endscene_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endscene_text.stopped')
            endscene_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endslideComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "endslide" ---
for thisComponent in endslideComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
