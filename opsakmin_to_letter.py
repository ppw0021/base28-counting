# Program written By Declan Ross
# This program takes a number as input and prints it in Base 27 Format

# Conversion table
conversionTable = [
    "C",                  # 0
    "RP",            # 1 a
    "RRF",      # 2 b
    "RMF",    # 3 c
    "RIF",     # 4 d
    "RT",            # 5 e 
    "RW",            # 6 f
    "RF",          # 7 g
    "RE",            # 8 h
    "RA",              # 9 i
    "RS",         # 10 j
    "RSN",     # 11 k 
    "REL",         # 12 l
    "REB",              # 13 m
    "N",                   # 14 n
    "LEB",               # 15 o 
    "LEL",          # 16 p 
    "LSN",      # 17 q
    "LS",          # 18 r
    "LA",               # 19 s
    "LE",             # 20 t
    "LF",           # 21 u
    "LW",             # 22 v
    "LT",             # 23 w
    "LIF",      # 24 x
    "LMF",     # 25 y
    "LRF",       # 26 z
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


# While true, loop over
while(True):
    print("Welcome to the Opsakmin decoder, please enter the first letter of each symbol, with each body part seperated by a space.")
    print('For example: "Right Eye Right Thumb Right Ear Lobe Right Ear Lobe Left Eye Ball" will be entered as "re rt rel rel leb"')
    userInput = input()

    output = ""
    current = ""


    for char in userInput:
        if char == " ":
            #print(current)
            current = current.upper()
            try:
                location = conversionTable.index(current)
                output += letterTable[location]
            except ValueError:
                output += "(SYMBOL ENTERED INCORRECTLY)"
            current = ""
        else:
            current += char

    #end case
    current = current.upper()
    try:
        location = conversionTable.index(current)
        output += letterTable[location]
    except ValueError:
        output += "(SYMBOL ENTERED INCORRECTLY)"
    current = ""

    print("Decoded message: ")
    print("____________________\n")
    print(output)

    print("\n____________________")