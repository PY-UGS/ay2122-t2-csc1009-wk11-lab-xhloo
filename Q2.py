class clockTime:

    # constructor
    def __init__(self, hours, minutes, seconds):
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds

    # set hours
    def setHours(self, hours):
        self.hours = hours
    
    # set minutes
    def setMinutes(self, minutes):
        self.minutes = minutes

    # set seconds
    def setSeconds(self, seconds):
        self.seconds = seconds

    # display the time in hours:minutes:seconds format
    def showTime(self):
        print("The time is {}:{}:{}".format(self.hours, self.minutes, self.seconds))

# initialize default
time = clockTime(0, 0, 0)

# loop 
while True:
    # user input for hr
    hr = int(input("Please enter hour(s): ")) 
    # if hr > 23
    if hr > 23:
        # print msg
        print("Hour(s) should be from 0 to 23")
    else:
        # if <= 23, set hr
        time.setHours(hr)
        # user input for min
        min = int(input("Please enter minute(s): ")) 
        # if min > 59
        if min > 59:
            # print msg
            print("Minute(s) should be from 0 to 59")
        else:
            # if <= 59, set min
            time.setMinutes(min)
            # user input for sec
            sec = int(input("Please enter second(s): ")) 
            # if sec > 59
            if sec > 60:
                print("Second(s) should be from 0 to 59")
            else:
                # if <= 59, set sec
                time.setSeconds(sec)
                # display the time
                time.showTime()
                # exit
                break
