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

# user input
hr = int(input("Please enter hour(s): ")) 
min = int(input("Please enter minute(s): ")) 
sec = int(input("Please enter second(s): ")) 

# passing the parameters into clockTime() class
time = clockTime(hr, min, sec)

# display the time
time.showTime()