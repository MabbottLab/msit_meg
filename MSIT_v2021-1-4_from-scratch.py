#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on September 30, 2021, at 15:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'MSIT_v2021-1-4_from-scratch'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\julie tseng\\msit\\MSIT_v2021-1-4_from-scratch.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Declare stimuli types
all_control_stim=['100','020','003']
all_int_stim=['221','212','331','313','112','211','332','233','131','311',\
    '232','322']

# Set up practice and task trial condition order
prac_trials = np.concatenate((np.ones(10), np.zeros(10))) # generate 1s, 0s
task_trials = np.concatenate((np.ones(100), np.zeros(100)))
shuffle(prac_trials) # shuffle it up
shuffle(task_trials)
# fill in resampled order as list of dicts
prac_trials = [{'stim': randchoice(all_control_stim)} if prac_trials[x] == 1 \
                else {'stim': randchoice(all_int_stim)} \
                for x in np.arange(20)]

task_trials = [{'stim': randchoice(all_control_stim)} if task_trials[x] == 1 \
               else {'stim': randchoice(all_int_stim)} \
               for x in np.arange(200)]

# set up dict of correct responses
key_dict = {'left': '1', 'down': '2', 'right': '3'}

# Initialize components for Routine "instr_prac"
instr_pracClock = core.Clock()
instr_text = visual.TextStim(win=win, name='instr_text',
    text="We\n\nneed\n\nLiz's\n\nmodified\n\ninstructions",
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
grating = visual.GratingStim(
    win=win, name='grating',units='height', 
    tex='sin', mask='circle',
    ori=0.0, pos=(-0.7,-0.3), size=[0.2], sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
triplets = visual.TextStim(win=win, name='triplets',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='nonsense',    font='Arial',
    alignText='center', anchorVert='top',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instr_task"
instr_taskClock = core.Clock()
task_instruct = visual.TextStim(win=win, name='task_instruct',
    text='now\nfor\nactual\ntask \ninstructions',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "task"
taskClock = core.Clock()
fix_2 = visual.TextStim(win=win, name='fix_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
grating_2 = visual.GratingStim(
    win=win, name='grating_2',units='height', 
    tex='sin', mask='circle',
    ori=0.0, pos=(-0.7,-0.3), size=[0.2], sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
triplets_2 = visual.TextStim(win=win, name='triplets_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "thx"
thxClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='thanks for playing!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr_prac"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instr_pracComponents = [instr_text, key_resp_2]
for thisComponent in instr_pracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_prac"-------
while continueRoutine:
    # get current time
    t = instr_pracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_pracClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text* updates
    if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_text.frameNStart = frameN  # exact frame index
        instr_text.tStart = t  # local t and not account for scr refresh
        instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
        instr_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_prac"-------
for thisComponent in instr_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_text.started', instr_text.tStartRefresh)
thisExp.addData('instr_text.stopped', instr_text.tStopRefresh)
# the Routine "instr_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_prac = data.TrialHandler(nReps=20.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=prac_trials,
    seed=None, name='trials_prac')
thisExp.addLoop(trials_prac)  # add the loop to the experiment
thisTrials_prac = trials_prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
if thisTrials_prac != None:
    for paramName in thisTrials_prac:
        exec('{} = thisTrials_prac[paramName]'.format(paramName))

for thisTrials_prac in trials_prac:
    currentLoop = trials_prac
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
    if thisTrials_prac != None:
        for paramName in thisTrials_prac:
            exec('{} = thisTrials_prac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    triplets.setText(stim)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    practiceComponents = [fix, grating, triplets, key_resp, feedback]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *grating* updates
        if grating.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            grating.setAutoDraw(True)
        if grating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                grating.tStop = t  # not accounting for scr refresh
                grating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
                grating.setAutoDraw(False)
        
        # *triplets* updates
        if triplets.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            triplets.frameNStart = frameN  # exact frame index
            triplets.tStart = t  # local t and not account for scr refresh
            triplets.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triplets, 'tStartRefresh')  # time at next scr refresh
            triplets.setAutoDraw(True)
            feedback.setText('')
            feedback.setAutoDraw(True)
        if triplets.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > triplets.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                triplets.tStop = t  # not accounting for scr refresh
                triplets.frameNStop = frameN  # exact frame index
                win.timeOnFlip(triplets, 'tStopRefresh')  # time at next scr refresh
                triplets.setAutoDraw(False)
                feedback.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                val, counts = np.unique(list(stim), return_counts=True)
                if key_dict[key_resp.keys] == val[counts == 1]:
                    key_resp.corr = 1
                    feedback.setText("Correct!")
                    feedback.setColor('white')
                else:
                    key_resp.corr = 0
                    feedback.setText("Oops, incorrect :(")
                    feedback.setColor('red')
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_prac.addData('fix.started', fix.tStartRefresh)
    trials_prac.addData('fix.stopped', fix.tStopRefresh)
    trials_prac.addData('grating.started', grating.tStartRefresh)
    trials_prac.addData('grating.stopped', grating.tStopRefresh)
    trials_prac.addData('triplets.started', triplets.tStartRefresh)
    trials_prac.addData('triplets.stopped', triplets.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('key_resp.keys',key_resp.keys)
    trials_prac.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials_prac.addData('key_resp.rt', key_resp.rt)
    trials_prac.addData('key_resp.started', key_resp.tStartRefresh)
    trials_prac.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'trials_prac'


# ------Prepare to start Routine "instr_task"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instr_taskComponents = [task_instruct, key_resp_3]
for thisComponent in instr_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_task"-------
while continueRoutine:
    # get current time
    t = instr_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *task_instruct* updates
    if task_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        task_instruct.frameNStart = frameN  # exact frame index
        task_instruct.tStart = t  # local t and not account for scr refresh
        task_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(task_instruct, 'tStartRefresh')  # time at next scr refresh
        task_instruct.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_task"-------
for thisComponent in instr_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('task_instruct.started', task_instruct.tStartRefresh)
thisExp.addData('task_instruct.stopped', task_instruct.tStopRefresh)
# the Routine "instr_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_task = data.TrialHandler(nReps=200.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=task_trials,
    seed=None, name='trials_task')
thisExp.addLoop(trials_task)  # add the loop to the experiment
thisTrials_task = trials_task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_task.rgb)
if thisTrials_task != None:
    for paramName in thisTrials_task:
        exec('{} = thisTrials_task[paramName]'.format(paramName))

for thisTrials_task in trials_task:
    currentLoop = trials_task
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_task.rgb)
    if thisTrials_task != None:
        for paramName in thisTrials_task:
            exec('{} = thisTrials_task[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    triplets_2.setText(stim)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    taskComponents = [fix_2, grating_2, triplets_2, key_resp_4]
    for thisComponent in taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_2* updates
        if fix_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            fix_2.frameNStart = frameN  # exact frame index
            fix_2.tStart = t  # local t and not account for scr refresh
            fix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
            fix_2.setAutoDraw(True)
        if fix_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_2.tStop = t  # not accounting for scr refresh
                fix_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_2, 'tStopRefresh')  # time at next scr refresh
                fix_2.setAutoDraw(False)
        
        # *grating_2* updates
        if grating_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            grating_2.frameNStart = frameN  # exact frame index
            grating_2.tStart = t  # local t and not account for scr refresh
            grating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_2, 'tStartRefresh')  # time at next scr refresh
            grating_2.setAutoDraw(True)
        if grating_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                grating_2.tStop = t  # not accounting for scr refresh
                grating_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(grating_2, 'tStopRefresh')  # time at next scr refresh
                grating_2.setAutoDraw(False)
        
        # *triplets_2* updates
        if triplets_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            triplets_2.frameNStart = frameN  # exact frame index
            triplets_2.tStart = t  # local t and not account for scr refresh
            triplets_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triplets_2, 'tStartRefresh')  # time at next scr refresh
            triplets_2.setAutoDraw(True)
        if triplets_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > triplets_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                triplets_2.tStop = t  # not accounting for scr refresh
                triplets_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(triplets_2, 'tStopRefresh')  # time at next scr refresh
                triplets_2.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[0].name  # just the first key pressed
                key_resp_4.rt = _key_resp_4_allKeys[0].rt
                # was this correct?
                if (key_resp_4.keys == str('')) or (key_resp_4.keys == ''):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "task"-------
    for thisComponent in taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_task.addData('fix_2.started', fix_2.tStartRefresh)
    trials_task.addData('fix_2.stopped', fix_2.tStopRefresh)
    trials_task.addData('grating_2.started', grating_2.tStartRefresh)
    trials_task.addData('grating_2.stopped', grating_2.tStopRefresh)
    trials_task.addData('triplets_2.started', triplets_2.tStartRefresh)
    trials_task.addData('triplets_2.stopped', triplets_2.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_task (TrialHandler)
    trials_task.addData('key_resp_4.keys',key_resp_4.keys)
    trials_task.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials_task.addData('key_resp_4.rt', key_resp_4.rt)
    trials_task.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials_task.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 200.0 repeats of 'trials_task'


# ------Prepare to start Routine "thx"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
thxComponents = [thanks]
for thisComponent in thxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thx"-------
while continueRoutine:
    # get current time
    t = thxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thx"-------
for thisComponent in thxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)
# the Routine "thx" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
