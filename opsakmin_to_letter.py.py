# Program written By Declan Ross
# This program takes a number as input and prints it in Base 27 Format

# Conversion table
conversionTable = [
    "C",                  # 0
    "RP",            # 1
    "RRF",      # 2
    "RMF",    # 3
    "RIF",     # 4
    "RT",            # 5
    "RW",            # 6
    "RF",          # 7
    "RE",            # 8
    "RA",              # 9
    "RS",         # 10
    "RSN",     # 11
    "REL",         # 12
    "RE",              # 13
    "N",                   # 14
    "LE",               # 15
    "LEL",          # 16
    "LSN",      # 17
    "LS",          # 18
    "LA",               # 19
    "LE",             # 20
    "LF",           # 21
    "LW",             # 22
    "LT",             # 23
    "LIF",      # 24
    "LMF",     # 25
    "LRF",       # 26
    "LP"              # 27
]

letterTable = [
    " ",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
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
        #print("Multiple: " + str(multiple) + " Remainder: " + str(remainder))
        if (multiple > (listLength-1)):
            recursiveOutput = recursiveMethod("", multiple, remainder, listLength)
            #print("Recursive Output: " + recursiveOutput)
            return recursiveOutput
        else:
            return (conversionTable[multiple] + ", " + conversionTable[remainder])
    
# This method recursively calls itself until the multiple is smaller than the table size
def recursiveMethod(output, multiple, remainder, listLength):
    #print("Looped")
    if multiple < (listLength - 1):  # Base case
        sendBack = conversionTable[multiple]+output + ", " + conversionTable[remainder] 
        #print("Sending: " + str(sendBack))
        return sendBack
    else:  # Recursive case
        new_multiple = multiple // listLength
        new_remainder = multiple % listLength
        output = output + ", " + conversionTable[new_remainder]
        #print("Recursed: " + str(output))
        return recursiveMethod(output, new_multiple, remainder, listLength)  # Return the recursive result
        

# This method converts the input into just the first letter
def shortenOpsakmin(opsakminInput):
    opsakminInput = ''.join([char for char in opsakminInput if not char.islower()])
    opsakminInput = opsakminInput.replace(" ", "")
    opsakminInput = opsakminInput.replace(",", ", ")
    return opsakminInput

# While true, loop over
while(True):
    print("Please enter message to encrypt")
    userInput = input()

    output = ""

    for char in userInput:
        opsakminNumber = letterTable.index(char)
        concat = convertToOpsakmin(opsakminNumber)
        output += concat + ", "

    print("Long output: ")
    output = output[:-2]
    print(output)

    print("Short output: ")
    shortenedOutput = shortenOpsakmin(output)
    print(shortenedOutput)
#    if (checkInput(userInput)):
#        print("____________________\n")
#        print("Base 10 Input:")
#        print(userInput + "\n")
#        print("Base 28 Opsakmin Output:")
#        opsakminOutput = convertToOpsakmin(userInput)
#        print(opsakminOutput + "\n")
#        print("Base 28 Opsakmin Output (Shortened):")
#        print(shortenOpsakmin(opsakminOutput))
#        print("____________________")
#    else:
#        print("Please enter a number")