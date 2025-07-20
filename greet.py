import time

timestamp = time.strftime('%H:%M:%S')
hrs = int(time.strftime('%H'))
print("The Time is:", timestamp)

if(hrs >= 5 and hrs <= 8):
    print("Good Morning Sir!, Lets Go for a Walk!")
if(hrs >= 9 and hrs <= 12):
    print("What is the Work Sir?, I am always Ready!")
if(hrs >= 13 and hrs <= 16):
    print("Good Afternoon Sir!")
if(hrs >= 17 and hrs <= 20):
    print("Good Evening Sir!, Coffee?")
if(hrs >= 21 and hrs <= 23):
    print("Good Night Sir!, It was nice to work with you")
if(hrs >= 0 and hrs <= 4):
    print("Its Past Midnight Sir, We shall Sleep!")