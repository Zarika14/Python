import time
hour= int(time.strftime('%H'))
print(hour)

hour=int(input("Enter the time :"))

if (hour>=0 and hour<12):
    print("Good Morning sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir")
if(hour>=17 and hour<24):
    print("Good Night Sir")    
       



