# Program written By Declan Ross
# This program takes a number as input and prints it in Base 27 Format

# Conversion table, first is base 10 number, second is the base 27* base 28
conversionTable = [
    "Chest",                  # 0
    "Right Pinky",            # 1
    "Right Ring Finger",      # 2
    "Right Middle Finger",    # 3
    "Right Index Finger",     # 4
    "Right Thumb",            # 5
    "Right Wrist",            # 6
    "Right Forearm",          # 7
    "Right Elbow",            # 8
    "Right Arm",              # 9
    "Right Shoulder",         # 10
    "Right Side of Neck",     # 11
    "Right Ear Lobe",         # 12
    "Right Eye",              # 13
    "Nose",                   # 14
    "Left Eye",               # 15
    "Left Ear Lobe",          # 16
    "Left Side of Neck",      # 17
    "Left Shoulder",          # 18
    "Left Arm",               # 19
    "Left Elbow",             # 20
    "Left Forearm",           # 21
    "Left Wrist",             # 22
    "Left Thumb",             # 23
    "Left Index Finger",      # 24
    "Left Middle Finger",     # 25
    "Left Ring Finger",       # 26
    "Left Pinky"              # 27
]

# This method checks if the input is a number or not
def checkInput(baseTenInput):
    try:
        int(baseTenInput)
        return True
    except:
        return False

# This converts the base 10 number into a Opsakmin
def convertToOpsakmin(baseTenInput):
    baseTenAsNumber = int(baseTenInput)
    listLength = len(conversionTable)
    if (baseTenAsNumber < listLength):
        return conversionTable[baseTenAsNumber]
    else:
        multiple = baseTenAsNumber // listLength
        remainder = baseTenAsNumber % listLength
        if (multiple > listLength):
            output = recursiveMethod(output, multiple, remainder, listLength)
            return output
        else:
            return (conversionTable[multiple] + ", " + conversionTable[remainder])
    
def recursiveMethod(output, multiple, remainder, listLength):
    print("Looped")
    if (multiple == 0):
        output = conversionTable[remainder] + ", " + output
        return output
    if (multiple > listLength):
        multiple = multiple // listLength
        remainder = multiple % listLength
        output = conversionTable[remainder] + ", " + output
        recursiveMethod(output, multiple, remainder, listLength)
        

# This method converts the input into just the first letter
def shortenOpsakmin(opsakminInput):
    opsakminInput = ''.join([char for char in opsakminInput if not char.islower()])
    opsakminInput = opsakminInput.replace(" ", "")
    opsakminInput = opsakminInput.replace(",", ", ")
    return opsakminInput

while(True):
    print("Please enter a base 10 number to convert to Opsakmin:")
    userInput = input()

    if (checkInput(userInput)):
        print("____________________\n")
        print("Base 10 Input:")
        print(userInput + "\n")
        print("Base 28 Opsakmin Output:")
        opsakminOutput = convertToOpsakmin(userInput)
        print(opsakminOutput + "\n")
        print("Base 28 Opsakmin Output (Shortened):")
        print(shortenOpsakmin(opsakminOutput))
        print("____________________")
    else:
        print("Please enter a number")