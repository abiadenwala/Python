import time
import os
while True:
    Outputfile = 'jstack_' + time.strftime("%m%d-%H%M%S")
# Jstack on Java pid
    jstackoutput = os.system("jstack <JAVA_PID> >> Output_" + Outputfile)
# Runs the command every 5 seconds
    time.sleep(5)