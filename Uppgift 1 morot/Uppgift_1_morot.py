
tor=int(input("Tors tid: "))
mor=int(input("Mors tid: "))

tid=0
morot=40
#Tors morot // Mors morot 
tm=0
mm=0

while morot>0:
	tid+=1

	if morot == 1 and tid%tor == 0 and tid%mor == 0:
		
		morot-=1

	if tid % tor == 0 and morot!=0:
		morot-=1
		tm+=1
				
	if tid % mor == 0 and morot!=0:
		morot-=1
		mm+=1
		
print("Tor at",tm,"morotter, och mor at",mm,"morotter")
