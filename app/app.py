from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion tables
conversionTable = [
    "C", "RP", "RRF", "RMF", "RIF", "RT", "RW", "RF", "RE", "RA", "RS", "RSN", "REL", "REB", "N", "LEB", "LEL", "LSN", "LS", "LA", "LE", "LF", "LW", "LT", "LIF", "LMF", "LRF", "LP"
]

letterTable = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "."
]

@app.route('/')
def home():
    return render_template('index.html')  # A simple HTML form for input

@app.route('/decode', methods=['POST'])
def decode():
    user_input = request.form['user_input']
    output = ""
    current = ""

    # Decode the input based on the script logic
    for char in user_input:
        if char == " ":
            current = current.upper()
            try:
                location = conversionTable.index(current)
                output += letterTable[location]
            except ValueError:
                output += "(MISSINPUT)"
            current = ""
        else:
            current += char

    current = current.upper()
    try:
        location = conversionTable.index(current)
        output += letterTable[location]
    except ValueError:
        output += "(MISSINPUT)"
    current = ""

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
