"""
"Coster.exe" is an implementation of Shadow's MP Costing Formula for 
ZEJ Roleplaying's house brand of Statistical Roleplaying.

Documentation on the formula can be found in the README.

Original Idea: "Shadow"
Contributors: - Gabriel "Muddy" Sousa
			  - Jake "Eebit" Fryer
"""

import math

baseValue = 0 #Base Value        || Vbase
aDamage	  = 0 #Adjusted Damage   || D adj
aRange 	  = 0 #Adjusted Range    || R adj
aAccuracy = 0 #Adjusted Accuracy || A adj
aVariance = 0 #Adjusted Variance || P adj

########################################################################
# 1. BASIC FORMULA
########################################################################

"""
1.1. Minimum Value Cap
"""
def minimumValueCap(vPre, vPost):
	return (max(4, vPre) + vPost)

"""
1.2. Base Value
"""
def setBaseValue():
	bValue = float(raw_input("Input Base Value./n"))
	print("Base Value saved/n")
	return bValue

"""
1.3. Adjusted Damage
"""
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

"""
1.4. Adjusted Range
"""
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

"""
1.5. Adjusted Accuracy
I'll... Just pass on this
"""
def setAdjustedAccuracy(aDamage):
	#aRate = float(raw_input("Insert Accuracy %"))/100
	#aMod = (aRate + 1)/2
	#wRel = aDamage + ???
	#buffer = wRel * aMod
	pass

"""
1.6. Adjusted Variance
"""
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

"""
1.7.1. Adjusted Healing (HP)
"""
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

"""
1.7.2. Adjusted Healing (MP)
"""
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

########################################################################
# 2. MULTI-HIT FORMULA
########################################################################

########################################################################
# 3. AREA OF EFFECT FORMULA
########################################################################

########################################################################
# 6. PROPERTIES AND EFFECTS
########################################################################

def knockbackDist():
	pass

"""
6.2. Stat Modifications
"""
def statMod():
	boostVal = float(raw_input("Input Stat Increase % (Without the % symbol of course)/n"))
	statToInc  = raw_input("Basic or Percentile Stat? (b/p)/n")
	if (statToInc == b):
		baseCost = ((boostVal ** 2) / 125) + (boostVal / 25) + 2
	elif (statToInc == p):
		baseCost = ((boostVal ** 2) * 0.014) + (boostVal * 0.23) + 1.5
	else:
		baseCost = 0
	return baseCost

def percentRecovery():
	pass

def revivalProp():
	pass

