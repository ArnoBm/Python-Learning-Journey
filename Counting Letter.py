
print("Letter Counter")

srt = input("Enter a String: ")
target = input("Enter a Letter: ")

lowstr = srt.casefold()
lowtarget = target.casefold()

print ("With Space: ",len(srt))
print (f"Number of {target}: ", lowstr.count(lowtarget))
