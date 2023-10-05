# python imports

# globals
#user defined classes

# variables
global initSuccessful
initSuccessful: bool
initSuccessful = False
global cleanSuccessful
cleanSuccessful: bool
cleanSuccessful = False
global isRunning
isRunning: bool
global rawInput
rawInput: str
global output
output: str

def Initate():

	global isRunning
	global initSuccessful
	global rawInput
	global output
	
	rawInput = ''
	output = ''
	
	isRunning = True
	initSuccessful = True

def Input():
	
	global rawInput
	
	rawInput = str(input("Enter Input: "))

def Output():
	
	global output
	print(output)

def Execute():

	print("Executing Engine Logic")
	
	global isRunning
	global rawInput
	global output
	
	output = rawInput
	
	match rawInput:
		case "exit":
			print("Engine Command for exit detected")
			isRunning = False	
		case _:
			print("No Engine Command detected")

def Clean_Up():

	global cleanSuccessful
	
	cleanSuccessful = True
	

def App():

	print("Hey I'm working here")
	
	global isRunning
	global initSuccessful
	global cleanSuccessful
	
	Initate()
	
	if(initSuccessful == True):
		print("Initate was successful")
	
	while isRunning == True:
	
		Input()
		
		Execute()
		
		Output()
	
	Clean_Up()
	
	if(cleanSuccessful == True):
		print("Clean_Up was successful")

App()