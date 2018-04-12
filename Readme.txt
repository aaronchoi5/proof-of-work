Specs: Ubuntu 16.04, Python 3.5, Cryptography Python Library (https://cryptography.io/en/latest/)
There are three main functions this program will execute: Target Generation, Solution Generation, and Solution Verification. If you want to generate a target for Proof of Work, simply run the following:
python pow.py target d targetPath 
(d is the difficulty you want to set from 0 to 256, i.e. 1. I also reccommend using ../data/target.txt in the targetPath parameter for convienence)
If you want to generate a solution run the following:
python pow.py solution targetPath messagePath 
(targetPath is the path to the file that contains a target; possibly generated using the target generation function earlier;) messagePath is a path to a file containing an input message to be used along with a nonce to find a solution that is less than or equal to the target) It will write to a file ../data/solution.txt and output the solution as well
If you want to verify that a solution is correct run the following:
python pow.py verify messagePath, solutionPath, targetPath 
(messagePath is a path to a file containing the message that has a solution, solutionPath is a path to the file of a solution, targetPath is a path to the file that contains a target to be compared with the solution and message) It will output 1 if the solution is valid and 0 if it is not.