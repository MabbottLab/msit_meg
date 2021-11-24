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
    size=(1024, 768), fullscr=True, screen=0, 
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
VPIXX = 0   # set to 1 if testing in the MEG

if VPIXX:
    # BUTTON BOX RESPONSES----------------------------------------------------#
    BBOX_1_OR_2 = parallel.ParallelPort(0x3048)
    BBOX_3 = parallel.ParallelPort(0x3048+2)
    
    # return button press and send signal to ACQ
    def readButtons():
        if BBOX_1_OR_2.readPin(2):
            return('1')
        elif BBOX_1_OR_2.readPin(3):
            return('2')
        elif BBOX_3.readPin(2):
            return('3')
        else:
            return('none')

    # SENDING OUT info about trials--------------------------------------------#
    MEG_ACQ         = parallel.ParallelPort(address=0x4048)
    triplet_congruent     = 1
    triplet_incongruent   = 2
    button_out            = [4, 8, 16]

    # send signal to ACQ
    def sendTrigger(triggerVal):
        MEG_ACQ.setData(int(triggerVal))
        core.wait(0.01)
        MEG_ACQ.setData(0)

#------------TASK PARAMETERS--------------------------------------------------#
FIX_START_TIME = 0.0
FIX_DURATION = 0.1
TRIPLET_START_TIME = 0.1
TRIPLET_DURATION = 0.1 # set to lower value to debug
ROUTINE_DURATION = 0.200 # set to 4.0000 usually

TOTAL_PRACTICE = 20 # 10+10 congruent/incogruent trials
TOTAL_TASK = 200 # 100+100 congruent/incongruent trials

# setup instruction slides
prac_instr = [{'imgidx': _thisDir + '\\images\\Slide' + str(x+1) + '.png'} \
                for x in np.arange(14)]

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
key_dict = {'left': '1', 'down': '2', 'right': '3', \
            '1': 'left', '2': 'down', '3': 'right'}

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
key_resp_2 = event.BuilderKeyResponse()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb',  
    # languageStyle='LTR',
    depth=0.0);
grating = visual.GratingStim(
    win=win, name='grating',units='height', 
    tex='sin', mask='circle',
    ori=0.0, pos=(-0.7,-0.3), size=[0.2], sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    contrast=1.0, # blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
triplets = visual.TextStim(win=win, name='triplets',
    text='hello',
    font='Open Sans', alignHoriz='center', alignVert='center',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', 
    # languageStyle='LTR',
    depth=0.0);
feedback = visual.TextStim(win=win, ori=0, name='feedback',
    text='nonsense', font='Open Sans',
    alignHoriz='center', alignVert='top',
    pos=(0, 0.3), height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', 
    depth=0.0)
key_resp = event.BuilderKeyResponse()

# Initialize components for Routine "instr_task"
instr_taskClock = core.Clock()
task_instruct = visual.ImageStim(win=win, name='task_instruct',
                image='images/Slide16.PNG', mask=None,
                ori=0.0, pos=(0, 0), size=None,
                color=[1,1,1], colorSpace='rgb',
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = event.BuilderKeyResponse()

# Initialize components for Routine "task"
taskClock = core.Clock()
fix_2 = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb',  
    # languageStyle='LTR',
    depth=0.0);
grating_2 = visual.GratingStim(
    win=win, name='grating',units='height', 
    tex='sin', mask='circle',
    ori=0.0, pos=(-0.7,-0.3), size=[0.2], sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    contrast=1.0, # blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
triplets_2 = visual.TextStim(win=win, name='triplets',
    text='hello',
    font='Open Sans', alignHoriz='center', alignVert='center',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', 
    # languageStyle='LTR',
    depth=0.0);
key_resp_4 = event.BuilderKeyResponse()

# Initialize components for Routine "thx"
thxClock = core.Clock()
thanks = visual.ImageStim(win=win, name='thanks',
                image='images/Slide17.PNG', mask=None,
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
    triplets.setText(stim)

    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    practiceComponents = [fix, grating, triplets, key_resp, feedback]
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
        if fix.status == STARTED and t >= FIX_START_TIME + FIX_DURATION:
            # keep track of stop time/frame for later
            fix.tStop = t  # not accounting for scr refresh
            fix.frameNStop = frameN  # exact frame index
            fix.setAutoDraw(False)
    
        # *grating* updates
        if grating.status == NOT_STARTED and t >= FIX_START_TIME:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.setAutoDraw(True)
        if grating.status == STARTED and t >= FIX_START_TIME + TRIPLET_DURATION:
            # keep track of stop time/frame for later
            grating.tStop = t  # not accounting for scr refresh
            grating.frameNStop = frameN  # exact frame index
            grating.setAutoDraw(False)
    
        # *triplets* updates
        if triplets.status == NOT_STARTED and t >= TRIPLET_START_TIME:
            # keep track of start time/frame for later
            triplets.frameNStart = frameN  # exact frame index
            triplets.tStart = t  # local t and not account for scr refresh
            triplets.setAutoDraw(True)
            
            # send trigger for trial type
            if prac_trials_type[type_counter]: # type 1 = control
                win.callOnFlip(sendTrigger, triplet_congruent)
            else:
                win.callOnFlip(sendTrigger, triplet_incongruent)
            type_counter += 1

            feedback.setText('')
            feedback.setAutoDraw(True)
        elif triplets.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION:
            # keep track of stop time/frame for later
            triplets.tStop = t  # not accounting for scr refresh
            triplets.frameNStop = frameN  # exact frame index
            # win.timeOnFlip(triplets, 'tStopRefresh')  # time at next scr refresh
            triplets.setAutoDraw(False)
            feedback.setAutoDraw(False)
    
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= TRIPLET_START_TIME:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and t >= TRIPLET_START_TIME + 3.0: 
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            key_resp.status = FINISHED
        if key_resp.status == STARTED:
            # read relevant buttons
            theseKeys = event.getKeys()
            response = readButtons()

            if "escape" in theseKeys:
                endExpNow = True
            if response != 'none':
                key_resp.rt = key_resp.clock.getTime() 
                sendTrigger(button_out[int(response)-1])
                logging.log(level=logging.EXP,\
                            msg="Button box received: %s"&(response))
                key_resp.keys = response

                # was this correct?
                val, counts = np.unique(list(stim), return_counts=True)
                if key_dict[key_resp.keys] == val[counts == 1] or key_resp.keys == val[counts == 1]:
                    key_resp.corr = 1
                    feedback.setText("Correct!")
                    feedback.setColor('white')
                else:
                    key_resp.corr = 0
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
    trials_prac.addData('grating.started', grating.tStart)
    trials_prac.addData('grating.stopped', grating.tStop)
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
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
instr_taskComponents = [task_instruct, key_resp_3]
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
    if key_resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
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
    triplets_2.setText(stim)
    key_resp_4.keys = []
    key_resp_4.rt = []
    # keep track of which components have finished
    taskComponents = [fix_2, grating_2, triplets_2, key_resp_4]
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
        
        # *fix_2* updates
        if fix_2.status == NOT_STARTED and t >= FIX_START_TIME:
            # keep track of start time/frame for later
            fix_2.frameNStart = frameN  # exact frame index
            fix_2.tStart = t  # local t and not account for scr refresh
            fix_2.setAutoDraw(True)
        if fix_2.status == STARTED and t >= FIX_START_TIME + FIX_DURATION:
            # keep track of stop time/frame for later
            fix_2.tStop = t  # not accounting for scr refresh
            fix_2.frameNStop = frameN  # exact frame index
            fix_2.setAutoDraw(False)
    
        # *grating_2* updates
        if grating_2.status == NOT_STARTED and t >= FIX_START_TIME:
            # keep track of start time/frame for later
            grating_2.frameNStart = frameN  # exact frame index
            grating_2.tStart = t  # local t and not account for scr refresh
            grating_2.setAutoDraw(True)
        if grating_2.status == STARTED and t >= FIX_START_TIME + FIX_DURATION:
            # is it time to stop? (based on global clock, using actual start)
            # keep track of stop time/frame for later
            grating_2.tStop = t  # not accounting for scr refresh
            grating_2.frameNStop = frameN  # exact frame index
            grating_2.setAutoDraw(False)
    
        # *triplets_2* updates
        if triplets_2.status == NOT_STARTED and t >= TRIPLET_START_TIME:
            # keep track of start time/frame for later
            triplets_2.frameNStart = frameN  # exact frame index
            triplets_2.tStart = t  # local t and not account for scr refresh
            
            # send trigger for trial type
            if task_trials_type[type_counter]: # type 1 = control
                win.callOnFlip(sendTrigger, triplet_congruent)
            else:
                win.callOnFlip(sendTrigger, triplet_incongruent)
            type_counter += 1
            
            triplets_2.setAutoDraw(True)
        if triplets_2.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION:
            # is it time to stop? (based on global clock, using actual start)
            # keep track of stop time/frame for later
            triplets_2.tStop = t  # not accounting for scr refresh
            triplets_2.frameNStop = frameN  # exact frame index
            triplets_2.setAutoDraw(False)
    
        # *key_resp_4* updates
        if key_resp_4.status == NOT_STARTED and t >= TRIPLET_START_TIME:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and t >= TRIPLET_START_TIME + TRIPLET_DURATION:
            # keep track of stop time/frame for later
            key_resp_4.tStop = t  # not accounting for scr refresh
            key_resp_4.frameNStop = frameN  # exact frame index
            key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED:
            # read relevant buttons
            theseKeys = event.getKeys()
            response = readButtons()

            if "escape" in theseKeys:
                endExpNow = True
            if response != 'none':
                key_resp_4.rt = key_resp_4.clock.getTime() 
                sendTrigger(button_out[int(response)-1])
                logging.log(level=logging.EXP,\
                            msg="Button box received: %s"&(response))
                key_resp_4.keys = response

                # was this correct?
                val, counts = np.unique(list(stim), return_counts=True)
                if key_dict[key_resp_4.keys] == val[counts == 1] or key_resp_4.keys == val[counts == 1]:
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0

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
    trials_task.addData('fix_2.started', fix_2.tStart)
    trials_task.addData('fix_2.stopped', fix_2.tStop)
    trials_task.addData('grating_2.started', grating_2.tStart)
    trials_task.addData('grating_2.stopped', grating_2.tStop)
    trials_task.addData('triplets_2.started', triplets_2.tStart)
    trials_task.addData('triplets_2.stopped', triplets_2.tStop)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_task (TrialHandler)
    trials_task.addData('key_resp_4.keys',key_resp_4.keys)
    trials_task.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials_task.addData('key_resp_4.rt', key_resp_4.rt)
    trials_task.addData('key_resp_4.started', key_resp_4.tStart)
    trials_task.addData('key_resp_4.stopped', key_resp_4.tStop)
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
