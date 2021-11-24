from psychopy import parallel, event

# CLOCK
key_resp = event.BuilderKeyResponse()

# BUTTON BOX RESPONSES----------------------------------------------------#
BBOX_1_OR_2 = parallel.ParallelPort(0x3048)
BBOX_3 = parallel.ParallelPort(0x3048+2)

# return button press
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
    
pressed = False

key_resp.keys = []
key_resp.rt = []
key_resp.clock.reset()

num_times_pressed = 0
while not pressed:
    response = readButtons()
    
    if response != 'none':
        key_resp.rt = key_resp.clock.getTime()
        sendTrigger(button_out[int(response)-1])
        key_resp.keys = response
        print("Button press detected!\nReaction Time: %.2f" % key_resp.rt)
        num_times_pressed += 1
        
        key_resp.rt = []
        key_resp.clock.reset()
        
    if num_times_pressed > 5:
        pressed = True