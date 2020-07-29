import time
import os
#number of iterations we need to go through the loop (In this case its 60 since i want this script to collect output for 5 minutes every 5 seconds).
iteration = 0
while True:
    if(iteration == 60):
        break
    else:
        
        Outputfile = 'jstack_' + time.strftime("%m%d-%H%M%S")
# Jstack on Java pid
        jstackoutput = os.system("jstack <JAVA_PID> >> Output_" + Outputfile)
# Runs the command every 5 seconds
        time.sleep(5)
