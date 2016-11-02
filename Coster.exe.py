import math

baseValue = 0 #Base Value        || Vbase
aDamage	  = 0 #Adjusted Damage   || D adj
aRange 	  = 0 #Adjusted Range    || R adj
aAccuracy = 0 #Adjusted Accuracy || A adj
aVariance = 0 #Adjusted Variance || P adj

def minimumValueCap(vPre, vPost):
	return (max(4, vPre) + vPost)

def setBaseValue():
	bValue = float(raw_input("Input Base Value./n"))
	print("Base Value saved/n")
	return bValue

def setAdjustedDamage():
	damOutput = float(raw_input("Input Damage Output % (Without the % symbol of course)/n"))/100
	piercing  = raw_input("Piercing? (y/n)/n")
	if piercing == "y":
		if damOutput < 1:
				buffer = (damOutput*10 + 2)
			else:
				buffer = (damOutput*20 - 8 + math.floor((damOutput-1)*5)*4) #This formula is so lol
	else:
		if damOutput < 2:
			buffer = (damOutput*10 - 10)
		else:
			buffer = (damOutput*20 - 28)
	destruct = raw_input("Destruct? (y/n)/n")
	if destruct == 'y':
		if buffer > 0:
			buffer *= 1.5
		else:
			buffer += 1
	print "Value for Adjusted Damage: " + str(buffer) + "/n"
	temp = raw_input("Override value? (y/n)/n")
	if temp == 'n':
		return buffer
	else:
		return float(raw_input("Insert value. If you're using this, rewrite the code so you don't need to./n"))


def setAdjustedRange():
	buffer = 0
	sources = float(raw_input("Insert Amount of Sources/n"))
	for i in range(sources):
		dMax = float(raw_input("Insert Maximum Distance of source" + str(i+1) + "/n"))
		dNull = float(raw_input("Number of Distances Excluded of source" + str(i+1) + "/n"))
		buffer += dMax - (dNull + 1)

	print "Value for Adjusted Range: " + str(buffer) + "/n"
	temp = raw_input("Override value? (y/n)/n")
	if temp == 'n':
		return buffer
	else:
		return float(raw_input("Insert value. If you're using this, rewrite the code so you don't need to./n"))

'''I'll... Just pass on this'''
def setAdjustedAccuracy(aDamage):
	#aRate = float(raw_input("Insert Accuracy %"))/100
	#aMod = (aRate + 1)/2
	#wRel = aDamage + ???
	#buffer = wRel * aMod
	pass

def setAdjustedVariance():
	pMin = float(raw_input("Insert Variance's Lower Bound %/n"))/100
	pMax = float(raw_input("Insert Variance's Upper Bound %/n"))/100
	buffer = (pMin + pMax) * 5
	print "Value for Adjusted Variance: " + str(buffer) + "/n"
	temp = raw_input("Override value? (y/n)/n")
	if temp == 'n':
		return buffer
	else:
		return float(raw_input("Insert value. If you're using this, rewrite the code so you don't need to./n"))

def setAdjustedHPHealing():
	hOut = float(raw_input("Insert HP Healing %/n"))/100
	if hOut < 2:
		buffer = hOut*10 - 8
	else
		buffer = hOut*20 - 24
	print "Value for Adjusted HP Healing: " + str(buffer) + "/n"
	temp = raw_input("Override value? (y/n)/n")
	if temp == 'n':
		return buffer
	else:
		return float(raw_input("Insert value. If you're using this, rewrite the code so you don't need to./n"))

def setAdjustedMPHealing():
	hOut = float(raw_input("Insert MP Healing %/n"))/100
	if hOut < 2:
		buffer = hOut*10 + 2
	else
		buffer = hOut*20 - 8
	print "Value for Adjusted MP Healing: " + str(buffer) + "/n"
	temp = raw_input("Override value? (y/n)/n")
	if temp == 'n':
		return buffer
	else:
		return float(raw_input("Insert value. If you're using this, rewrite the code so you don't need to./n"))

