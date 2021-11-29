from psychopy import parallel

# BUTTON BOX 
BBOX = parallel.ParallelPort(0x3048) # instantiate the port

# flip the control bit, if necessary
ctrl_port = parallel.ParallelPort(0x3048+2)
ctrl_port.setPin(7, 1)

num_times_pressed = 0 # test for 
while num_times_pressed < 20:
    response = BBOX.readData() # returns 1, 2, 4
    
    if response: # only proceeds if response = 1, 2, 4, breaks if response = 0
        print(response)
        num_times_pressed += 1
