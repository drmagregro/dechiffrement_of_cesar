def chiffre_cesar(mot, decalage):
    return "".join([chr((ord(char) - 97 + decalage) % 26 + 97) for char in mot])

def dechiffre_cesar(mot, decalage):
    return "".join([chr((ord(char) - 97 - decalage) % 26 + 97) for char in mot])


message_chiffre = "ndbdn"


for decalage in range(1, 26):
    message_dechiffre = dechiffre_cesar(message_chiffre, decalage)
    print(f"Décalage {decalage} → {message_dechiffre}")