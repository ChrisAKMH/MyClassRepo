class Time:
    def __init__(self, hours = 0 , minutes = 0 , seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def SetData(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def PrintClock(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")
    
t1 = Time()
hours = int(input("Write hours: "))
minutes = int(input("Write minutes: "))
seconds = int(input("Write seconds: "))
t1.SetData(hours, minutes, seconds)
t1.PrintClock()

t2 = Time(12,11,32)
t2.PrintClock()

t3 = Time(12,11,32)
t3.PrintClock()
t4 = Time(12,11,32)
t4.PrintClock()
