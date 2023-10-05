# python imports
from enum import Enum

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

# Classes
# Command list Enum
class EngineCommands(Enum):
	EXIT = "\exit"

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
	
	#print(EngineCommands(rawInput))
	if(rawInput in EngineCommands._value2member_map_):
		match EngineCommands(rawInput):
			case EngineCommands.EXIT:
				print("Engine Command for exit detected")
				isRunning = False	
	else: # if it is not an engine command pass to app logiv
		print("No Engine Command detected")
		# App Logic comes here

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