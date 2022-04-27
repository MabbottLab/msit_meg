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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = 'v1.85.2'
expName = 'MSIT_v1-85-2_MEG'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='C:\\Users\\julie tseng\\msit_meg\\MSIT_v2021-1-4_keyboard.py',
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
    size=(1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    # blendMode='avg', 
    useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = event.BuilderKeyResponse()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

############# EVERYTHING HERE IS CUSTOM SETUP #################################

# ---------- PARALLEL PORT SETUP ---------------------------------------------#
VPIXX = 1   # set to 1 if testing in the MEG

if VPIXX:
    # BUTTON BOX RESPONSES----------------------------------------------------#
    BBOX = parallel.ParallelPort(0x3048) # instantiate data register
    CTRL_PORT = parallel.ParallelPort(0x3048+2) # instantiate ctrl register
    if not CTRL_PORT.readPin(7):  # flip control bit to set pport as input
        CTRL_PORT.setPin(7,1)

    # SENDING OUT info about trials--------------------------------------------#
    MEG_ACQ         = parallel.ParallelPort(address=0x4048)
    triplet_congruent     = 1
    triplet_incongruent   = 2
    button_out            = [4, 8, 16] # [1, 2, 3] values, [G, Y, R] colours
    correct               = 32
    incorrect             = 64

    # send signal to ACQ
    def sendTrigger(triggerVal):
        """ Sets data to be presented to the paralell port of 0xD030.  
        Sets `triggerVal` pin to high, wait 0.01s, then set all ports to low.
        """
        MEG_ACQ.setData(int(triggerVal))
        core.wait(0.01)
        MEG_ACQ.setData(0)
    
    # return button press
    def readButtons():
        if BBOX.readPin(2): # green/left/1
            sendTrigger(button_out[0])
            return(1)
        elif BBOX.readPin(3): # yellow/up/2
            sendTrigger(button_out[1])
            return(2)
        elif BBOX.readPin(4): # red/right/3
            sendTrigger(button_out[2])
            return(3)
        else:
            return(0)
    
#------------TASK PARAMETERS--------------------------------------------------#
FIX_START_TIME = 0.5
FIX_DURATION = 0.5
TRIPLET_START_TIME = 1.0
TRIPLET_DURATION = 3.0 # set to lower value to debug
ROUTINE_DURATION = 4.000 # set to 4.0000 usually

TOTAL_PRACTICE = 20 # 10+10 congruent/incogruent trials
TOTAL_TASK = 200 # 100+100 congruent/incongruent trials

# setup instruction slides
prac_instr = [{'imgidx': _thisDir + '\\images\\Slide' + str(x+1) + '.png'} \
                for x in np.arange(15)]

# Declare stimuli types
all_control_stim=['100','020','003']
all_int_stim=['221','212','331','313','112','211','332','233','131','311',\
    '232','322']

# Set up practice and task trial condition order
prac_trials_type = np.concatenate((np.ones(10), np.zeros(10))) # generate 1s, 0s
task_trials_type = np.concatenate((np.ones(100), np.zeros(100)))
shuffle(prac_trials_type) # shuffle it up
shuffle(task_trials_type)

# fill in resampled order as list of dicts
prac_trials = [{'stim': randchoice(all_control_stim)} if prac_trials_type[x] == 1 \
                else {'stim': randchoice(all_int_stim)} \
                for x in np.arange(TOTAL_PRACTICE)]

task_trials = [{'stim': randchoice(all_control_stim)} if task_trials_type[x] == 1 \
               else {'stim': randchoice(all_int_stim)} \
               for x in np.arange(TOTAL_TASK)]

# set up dict of correct responses
key_dict = {'left': '1', 'up': '2', 'right': '3', \
            '1': 'left', '2': 'up', '3': 'right'}

################ INITIALIZING COMPONENTS FOR EXPERIMENT ################################

# Initialize components for Routine "instr_prac"
instr_pracClock = core.Clock()
instr_slide = visual.ImageStim(
    win=win,
    name='instr_slide', 
    image='images/Slide1.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', 
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = event.BuilderKeyResponse()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
taskClock = core.Clock()
fix = visual.ImageStim(
    win=win,
    name='fix', 
    image='images/fix_white.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', 
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
grating = visual.GratingStim(
    win=win, name='grating',units='height', 
    tex='sin',
    ori=0.0, pos=(-0.7,-0.3), size=[0.2], sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    contrast=1.0, # blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
triplets = visual.ImageStim(
    win=win,
    name='triplets', 
    image='images/100.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', 
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='nonsense', font='Open Sans',
    alignHoriz='center', alignVert='top',
    pos=(0, 0.3), height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', 
    depth=0.0)
square = visual.Rect(
    win=win, name='square', units='height', 
    width = 0.1, height = 0.1, 
    fillColor=[1,1,1], pos=(-0.84, 0))    
square_black = visual.Rect(
    win=win, name='square', units='height', 
    width = 0.1, height = 0.1, 
    fillColor=[-1,-1,-1], lineColor=[-1,-1,-1], pos=(-0.84, 0))

# Initialize components for Routine "instr_task"
instr_taskClock = core.Clock()
task_instruct = visual.ImageStim(win=win, name='task_instruct',
                image='images/Slide17.PNG', mask=None,
                ori=0.0, pos=(0, 0), size=None,
                color=[1,1,1], colorSpace='rgb',
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "thx"
thxClock = core.Clock()
thanks = visual.ImageStim(win=win, name='thanks',
                image='images/Slide18.PNG', mask=None,
                ori=0.0, pos=(0, 0), size=None,
                color=[1,1,1], colorSpace='rgb', 
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)

################################################################################
########## PRACTICE INSTRUCTIONS #####################################################
################################################################################

# set up handler to look after randomisation of conditions etc
instr_prac = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=prac_instr,
    seed=None, name='instr_prac')
thisExp.addLoop(instr_prac)  # add the loop to the experiment
thisInstr_prac = instr_prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstr_prac.rgb)
if thisInstr_prac != None:
    for paramName in thisInstr_prac:
        exec('{} = thisInstr_prac[paramName]'.format(paramName))

for thisInstr_prac in instr_prac:
    currentLoop = instr_prac
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_prac.rgb)
    if thisInstr_prac != None:
        for paramName in thisInstr_prac:
            exec('{} = thisInstr_prac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    instr_slide.setImage(imgidx)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [instr_slide, key_resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    instr_pracClock.reset()  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = instr_pracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_slide* updates
        if instr_slide.status == NOT_STARTED and t >= 0.0:
            # keep track of start time/frame for later
            instr_slide.setAutoDraw(True)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 0.0:
            # keep track of start time/frame for later
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            if "space" in theseKeys:
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

################################################################################
########## PRACTICE TRIALS #####################################################
################################################################################

# set up handler to look after randomisation of conditions etc
trials_prac = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=prac_trials, # drop in trials content
    seed=None, name='trials_prac')
thisExp.addLoop(trials_prac)  # add the loop to the experiment
thisTrials_prac = trials_prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
if thisTrials_prac != None:
    for paramName in thisTrials_prac:
        exec('{} = thisTrials_prac[paramName]'.format(paramName))

type_counter = 0
for thisTrials_prac in trials_prac:
    currentLoop = trials_prac
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
    if thisTrials_prac != None:
        for paramName in thisTrials_prac:
            exec('{} = thisTrials_prac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    routineTimer.add(ROUTINE_DURATION)
    # update component parameters for each repeat
    triplets.setImage(_thisDir + '\\images\\' + str(stim) + '.png')

    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    practiceComponents = [fix, grating, triplets, key_resp, square, square_black, feedback]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    practiceClock.reset()  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and t >= FIX_START_TIME:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.setAutoDraw(True)
            square_black.setAutoDraw(True)
        if fix.status == STARTED and t >= FIX_START_TIME + FIX_DURATION:
            # keep track of stop time/frame for later
            fix.tStop = t  # not accounting for scr refresh
            fix.frameNStop = frameN  # exact frame index
            fix.setAutoDraw(False)
            square_black.setAutoDraw(False)
    
        # *triplets* updates
        if triplets.status == NOT_STARTED and t >= TRIPLET_START_TIME:
            # keep track of start time/frame for later
            triplets.frameNStart = frameN  # exact frame index
            triplets.tStart = t  # local t and not account for scr refresh
            triplets.setAutoDraw(True)
            square.setAutoDraw(True)
            grating.setAutoDraw(True)
            feedback.setText('')
            feedback.setAutoDraw(True)
            
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')  # clear events on next screen flip
            
            # send trigger for trial type
            if prac_trials_type[type_counter]: # type 1 = control
                win.callOnFlip(sendTrigger, triplet_congruent)
            else:
                win.callOnFlip(sendTrigger, triplet_incongruent)
            type_counter += 1
        elif triplets.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION:
            # keep track of stop time/frame for later
            triplets.tStop = t  # not accounting for scr refresh
            triplets.frameNStop = frameN  # exact frame index
            # win.timeOnFlip(triplets, 'tStopRefresh')  # time at next scr refresh
            continueRoutine = False
            triplets.setAutoDraw(False)
            square.setAutoDraw(False)
            grating.setAutoDraw(False)
            feedback.setAutoDraw(False)
    
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION: 
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            key_resp.status = FINISHED
        if key_resp.status == STARTED:
            # read relevant buttons
            response = readButtons() # will return 1, 2, 3, or 0 and send trigger
            if response and not key_resp.keys:
                key_resp.rt = key_resp.clock.getTime()
                key_resp.keys = str(response)
                key_resp.status = FINISHED

                # was this correct?
                val, counts = np.unique(list(stim), return_counts=True) # right answer = number with 1 occurrence
                if key_dict[key_resp.keys] == val[counts == 1] or key_resp.keys == val[counts == 1]:
                    key_resp.corr = 1
                    sendTrigger(correct)
                    feedback.setText("Correct!")
                    feedback.setColor('white')
                else:
                    key_resp.corr = 0
                    sendTrigger(incorrect)
                    feedback.setText("Nice try.\nThe correct answer is %s."%(key_dict[val[counts == 1][0]]))
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    trials_prac.addData('fix.started', fix.tStart)
    trials_prac.addData('fix.stopped', fix.tStop)
    trials_prac.addData('triplets.started', triplets.tStart)
    trials_prac.addData('triplets.stopped', triplets.tStop)
    # check responses
    if key_resp.keys in ['', [], None, 'none']:  # No response was made
        key_resp.keys = None
        key_resp.corr = 0;  # correct non-response
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('key_resp.keys',key_resp.keys)
    trials_prac.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials_prac.addData('key_resp.rt', key_resp.rt)
    trials_prac.addData('key_resp.started', key_resp.tStart)
    trials_prac.addData('key_resp.stopped', key_resp.tStop)
    thisExp.nextEntry()
    
# ------Prepare to start Routine "instr_task"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
instr_taskComponents = [task_instruct, key_resp]
for thisComponent in instr_taskComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
instr_taskClock.reset()  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_task"-------
while continueRoutine:
    # get current time
    t = instr_taskClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *task_instruct* updates
    if task_instruct.status == NOT_STARTED and t >= 0.0-frameTolerance:
        task_instruct.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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

print("Moving onto the actual task.")

# -------Ending Routine "instr_task"-------
for thisComponent in instr_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_task = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=task_trials,
    seed=None, name='trials_task')
thisExp.addLoop(trials_task)  # add the loop to the experiment
thisTrials_task = trials_task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_task.rgb)
if thisTrials_task != None:
    for paramName in thisTrials_task:
        exec('{} = thisTrials_task[paramName]'.format(paramName))

type_counter = 0
for thisTrials_task in trials_task:
    currentLoop = trials_task
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_task.rgb)
    if thisTrials_task != None:
        for paramName in thisTrials_task:
            exec('{} = thisTrials_task[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "task"-------
    continueRoutine = True
    routineTimer.add(ROUTINE_DURATION)
    # update component parameters for each repeat
    triplets.setImage(_thisDir + '\\images\\' + str(stim) + '.png')
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    taskComponents = [fix, grating, triplets, square, square_black, key_resp]
    for thisComponent in taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    taskClock.reset()  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = taskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and t >= FIX_START_TIME:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.setAutoDraw(True)
            square_black.setAutoDraw(True)
        if fix.status == STARTED and t >= FIX_START_TIME + FIX_DURATION:
            # keep track of stop time/frame for later
            fix.tStop = t  # not accounting for scr refresh
            fix.frameNStop = frameN  # exact frame index
            fix.setAutoDraw(False)
            square_black.setAutoDraw(False)
    
        # *triplets* updates
        if triplets.status == NOT_STARTED and t >= TRIPLET_START_TIME:
            # keep track of start time/frame for later
            triplets.frameNStart = frameN  # exact frame index
            triplets.tStart = t  # local t and not account for scr refresh
            triplets.setAutoDraw(True)
            square.setAutoDraw(True)
            grating.setAutoDraw(True)
            feedback.setText('')
            feedback.setAutoDraw(True)
            
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')  # clear events on next screen flip
            
            # send trigger for trial type
            if task_trials_type[type_counter]: # type 1 = control
                win.callOnFlip(sendTrigger, triplet_congruent)
            else:
                win.callOnFlip(sendTrigger, triplet_incongruent)
            type_counter += 1
        elif triplets.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION:
            # keep track of stop time/frame for later
            triplets.tStop = t  # not accounting for scr refresh
            triplets.frameNStop = frameN  # exact frame index
            # win.timeOnFlip(triplets, 'tStopRefresh')  # time at next scr refresh
            continueRoutine = False
            triplets.setAutoDraw(False)
            square.setAutoDraw(False)
            grating.setAutoDraw(False)
            feedback.setAutoDraw(False)
            
        waitOnFlip = False
        # *key_resp* updates
        if key_resp.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION: 
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            key_resp.status = FINISHED
        if key_resp.status == STARTED:
            # read relevant buttons
            response = readButtons() # will return 1, 2, 3, or 0 and send trigger
            if response and not key_resp.keys:
                key_resp.rt = key_resp.clock.getTime()
                key_resp.keys = str(response)
                key_resp.status = FINISHED

                # was this correct?
                val, counts = np.unique(list(stim), return_counts=True) # right answer = number with 1 occurrence
                if key_dict[key_resp.keys] == val[counts == 1] or key_resp.keys == val[counts == 1]:
                    key_resp.corr = 1
                    sendTrigger(correct)
                    feedback.setText("Correct!")
                    feedback.setColor('white')
                else:
                    key_resp.corr = 0
                    sendTrigger(incorrect)
                    feedback.setText("Nice try.\nThe correct answer is %s."%(key_dict[val[counts == 1][0]]))
        

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    trials_task.addData('fix.started', fix.tStart)
    trials_task.addData('fix.stopped', fix.tStop)
    trials_task.addData('grating.started', grating.tStart)
    trials_task.addData('grating.stopped', grating.tStop)
    trials_task.addData('triplets.started', triplets.tStart)
    trials_task.addData('triplets.stopped', triplets.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_task (TrialHandler)
    trials_task.addData('key_resp.keys',key_resp.keys)
    trials_task.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials_task.addData('key_resp.rt', key_resp.rt)
    trials_task.addData('key_resp.started', key_resp.tStart)
    trials_task.addData('key_resp.stopped', key_resp.tStop)
    thisExp.nextEntry()

# ------Prepare to start Routine "thx"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
thxComponents = [thanks]
for thisComponent in thxComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
thxClock.reset()  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thx"-------
while continueRoutine:
    # get current time
    t = thxClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and t >= 0.0:
        thanks.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
