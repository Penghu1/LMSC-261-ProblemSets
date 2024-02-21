BPM = int(input("enter the songs tempo in BPM:"))# input the tempo
duration = int(input("Enter the song duration in seconds:"))# input the song duration

second =1 
while second<=duration: # limit the time below total duration
    totalbeats=second*BPM//60 #calculate number of beat in each second
    print("At second",second,"total beats:",totalbeats) 
    second +=1 


