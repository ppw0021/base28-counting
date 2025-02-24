# Base 28 Encoding Program

## Overview

The **Base 28 Encoding Program** is a unique and engaging numerical encoding system inspired by anthropological research on the Papua New Guineans' use of **body parts** for counting instead of conventional numerical systems. This program takes a **Base 10 number** as input and converts it into a **Base 28 representation** using a set of predefined body part names.

This project was suggested by my partner, and I was excited to work on this project as it demonstrates **recursion** and **numerical encoding techniques**.

## Features

- Converts **Base 10 numbers** into an equivalent **Base 28 representation**.
- Uses **body parts** instead of traditional numerical symbols.
- Implements **recursive algorithms** to handle large numbers efficiently.
- Provides both a **full text** and a **shortened** version of the encoded number.
- Ensures input validation to handle incorrect inputs gracefully.

## Implementation

The program follows a structured approach:

### **1. Conversion Table**
A predefined **list of body parts** represents numbers from **0 to 27**. Each position in the list corresponds to a unique body part name.

### **2. Recursive Conversion Process**
- If the input number is **less than 28**, it directly maps to the corresponding body part.
- If the input number is **28 or greater**, the program recursively determines the quotient and remainder when divided by 28.
- The recursive function builds the final Base 28 representation by repeatedly breaking down the input number until all components fit within the **Base 28 range**.

### **3. Input Validation**
- The program checks if the user input is a valid **integer** before processing.
- If an invalid input is detected, it prompts the user to enter a valid number.

### **4. Shortened Representation**
- The program provides an additional **shortened output format**, where only the first letter of each body part is retained, creating a compact encoded string.

## Code Snippet

The core of the recursive conversion process is handled by:
```python
# This method recursively calls itself until the multiple is smaller than the table size
def recursiveMethod(output, multiple, remainder, listLength):
    if multiple < (listLength - 1):  # Base case
        return conversionTable[multiple] + output + ", " + conversionTable[remainder]
    else:  # Recursive case
        new_multiple = multiple // listLength
        new_remainder = multiple % listLength
        output = output + ", " + conversionTable[new_remainder]
        return recursiveMethod(output, new_multiple, remainder, listLength)  # Recursive call
```

## Usage Instructions

### **1. Run the Program**
Ensure you have Python installed, then execute the script in a terminal:
```bash
python number_to_opsakmin.py
```

### **2. Enter a Number**
The program prompts for a **Base 10 number**. Enter any positive integer.

### **3. View the Output**
- The program displays:
  - The **Base 10 input**.
  - The corresponding **Base 28 representation using body parts**.
  - The **shortened version** of the Base 28 output.
