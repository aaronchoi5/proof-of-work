import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def target(d, writeFilePath):
	d = int(d)
	#d is difficulty
	if(d > 256 or d < 0):
		print("Invalid d!")
		return
	#this checks if d is valid
	onesLength = 256 - d
	ones = 0
	base10 = 1
	for x in range(0, onesLength):
		ones = ones + base10
		base10 = base10 * 10
	target = str(ones).zfill(256)
	#this adds zeroes in front of the ones until we get a number that is 256 digits long
	print(target)
	with open(writeFilePath, 'w') as f:
		f.write(target)

def solution(targetPath, messagePath):
	with open(targetPath, 'r') as target:
		targetVar = target.read()
	with open(messagePath, 'r') as message:
		messageVar = message.read()

	nonce = 0
	meetsTarget = False
	#we must find a nonce that can be used in a hash function with the message to produce a solution <= target
	while(meetsTarget == False):
		messageVarWithCounter = messageVar + str(nonce)
		digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
		messageBytesArray = messageVarWithCounter.encode('utf-8')
		digest.update(messageBytesArray)
		#Some fancy conversion to hex and then to binary and then to decimal. I originally intended to check the binary form for debugging.

		bytesVar = digest.finalize()
		hexstr = "".join(["{0}".format(format(byte,"02x")) for byte in bytesVar])
		byteBin = bin(int(hexstr, 16))[2:].zfill(8)
		decimalFormBytes = int(byteBin, base=2)
		#print(decimalFormBytes)
		targetDecimalForm = int(targetVar, base=2)
		#print(targetDecimalForm)
		if(targetDecimalForm >= decimalFormBytes):
			meetsTarget = True
			print(nonce)
			with open("../data/solution.txt", 'w') as f:
				f.write(str(nonce))
		else:
			nonce += 1

def verify(inputPath, solutionPath, targetPath):
	with open(inputPath, 'r') as i:
		inputVar = i.read()
	with open(solutionPath, 'r') as solution:
		solutionVar = solution.read()
	with open(targetPath, 'r') as target:
		targetVar = target.read()

	
	messageAndSol = inputVar + solutionVar
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	messageAndSolBytes = messageAndSol.encode('utf-8')
	digest.update(messageAndSolBytes)
	bytesVar = digest.finalize()
	#conversion to hex then binary and then decimal
	hexstr = "".join(["{0}".format(format(byte,"02x")) for byte in bytesVar])
	byteBin = bin(int(hexstr, 16))[2:].zfill(8)
	decimalFormBytes = int(byteBin, base=2)
	targetDecimalForm = int(targetVar, base=2)
	if(targetDecimalForm >= decimalFormBytes):
		print(1)
	else:
		print(0)



def main():
	if sys.argv[1] == "target":
		target(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == "solution":
		solution(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == "verify":
		verify(sys.argv[2], sys.argv[3], sys.argv[4])
main()