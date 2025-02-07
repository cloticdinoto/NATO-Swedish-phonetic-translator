bokstaveringsalfabet = {
    "A": "ADAM", "B": "BERTIL", "C": "CESAR", "D": "DAVID", "E": "ERIK",
    "F": "FILIP", "G": "GUSTAV", "H": "HELGE", "I": "IVAR", "J": "JOHAN",
    "K": "KALLE", "L": "LUDVIG", "M": "MARTIN", "N": "NIKLAS", "O": "OLOF",
    "P": "PETTER", "Q": "QVINTUS", "R": "RUDOLF", "S": "SIGURD", "T": "TORE",
    "U": "URBAN", "V": "VIKTOR", "W": "WILHELM", "X": "XERXES", "Y": "YNGVE",
    "Z": "ZÄTA", "Å": "ÅKE", "Ä": "ÄRLIG", "Ö": "ÖSTEN", "0": "NOLLA", "1": "ETT",
    "2": "TVÅA", "3": "TREA", "4": "FYRA", "5": "FEMMA", "6": "SEXA", "7": "SJU",
    "8": "ÅTTA", "9": "NIA"
}

print("SKRIV IN DITT ORD:")
ord = input()

def bokstaveraOrd(text):
    text = text.upper()
    bokstavsOrden = []
    for bokstav in text:
        kodord = bokstaveringsalfabet.get(bokstav, bokstav)
        bokstavsOrden.append(kodord)
    print(" - ".join(bokstavsOrden))
    
bokstaveraOrd(ord)