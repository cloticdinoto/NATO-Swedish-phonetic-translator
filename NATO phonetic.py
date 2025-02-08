bokstaveringsalfabet = {
    "A": "ALPHA", "B": "BRAVO", "C": "CHARLIE", "D": "DELTA", "E": "ECHO",
    "F": "FOXTROT", "G": "GOLF", "H": "HOTEL", "I": "INDIA", "J": "JULIETT",
    "K": "KILO", "L": "LIMA", "M": "MIKE", "N": "NOVEMBER", "O": "OSCAR",
    "P": "PAPA", "Q": "QUEBEC", "R": "ROMEO", "S": "SIERRA", "T": "TANGO",
    "U": "UNIFORM", "V": "VICTOR", "W": "WHISKEY", "X": "XRAY", "Y": "YANKEE",
    "Z": "ZULU", "0": "ZERO", "1": "ONE","2": "TWO", "3": "THREE", "4": "FOUR",
    "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE",  " ": "(space)" 
}

print("ENTER WORD OR SENTENCE:")
ord = input()

def bokstaveraOrd(text):
    text = text.upper()
    bokstavsOrden = []
    for bokstav in text:
        kodord = bokstaveringsalfabet.get(bokstav, bokstav)
        bokstavsOrden.append(kodord)
    print("---")
    print(" - ".join(bokstavsOrden))
    
bokstaveraOrd(ord)