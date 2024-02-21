seconds = int(input("Enter the song duration in seconds: "))##input song duration in seconds
minutes = (seconds//60)## calculate the number of minutes
seconds = (seconds%60) ## calculate the remaining seconds
print("The song duration is",minutes, "minutes and",seconds,"seconds")