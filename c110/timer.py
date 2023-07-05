import time

def countDownTimer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        second=int(seconds%60)
        timer=f"{mins}:{second}"
        print(timer)
        seconds-=1
    print("timeUp")
seconds=int(input("ENTER THE TIME IN NUMBER OF SECONDS "))
countDownTimer(seconds)
       