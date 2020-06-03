#import adb and time module
#if you didn't install ppadb.client , install using pip
from ppadb.client import Client
import time

#function to run the program:
def taptap():
    #initializing tapped as 0
    tapped = 0
    print('No of taps:', tapped)
    #loop to contiuously run the program
    while True:
        first_tap = 1
        device.shell(' input touchscreen tap 127 833  ')
        device.shell(' input touchscreen tap 869 890 ')
        print('time is',time.ctime(time.time()) )
        tapped += first_tap
        print(tapped)
    
        if time.time()>timeout:
            break
    print('------------------------------------END---------------------------')
    print('Total Number of taps = ', tapped)
    print('End time : ', time.ctime(time.time()))
#connecting to adb client
adb = Client(host="127.0.0.1", port=5037)

#setting run time, in this case am setting it for 5 minutes
timeout = time.time() + 60 * 5

#storing the first device in a variable
devices = adb.devices()
device = devices[0]

#checking if there is any device connected or not
if len(devices) == 0:
    print('There is no device connected')



# displaying starting time
current_time = time.ctime(time.time())
print('The starting time is:', current_time)

#calling the function to continuously run the program
taptap()


    