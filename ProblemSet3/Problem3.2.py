note = int(input("Enter a MIDI number between 0 and 127: ")) #input midi note number
frequency = ((2 ** ((note - 69)/12))*440) #calculate the corresbonding frequency  
print("The frequency of the MIDI note number",note, "is" ,frequency, "Hz.")