BPM = int(input("Enter BPM: ")) #input BPM
interval = (60000/BPM) #calculate the corresbonding time in milliseconds
print("A quarter note delay in milliseconds for",BPM,"BPM is",interval,"ms.")