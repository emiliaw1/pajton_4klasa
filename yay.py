def cezar(tekst, k):
    zaszyfrowany = ""
    for char in range(len(tekst)):
        zaszyfrowany += szyfrowanie(tekst[char], k)
    print(zaszyfrowany)
def szyfrowanie(char, k):
    if char.isupper():
        return chr((ord(char) - 65 + k) % 26 + 65)
    elif char.islower():
        return chr((ord(char) - 97 + k) % 26 + 97)
    elif char == " ":
        return char
    else:
        return char
def odszyfrowywanie(tekst):
    for i in range(26):
        odszyfrowane = ""
        for j in range(len(tekst)):
            odszyfrowane += szyfrowanie(tekst[j], -i)
        print(f"{i+1}, {odszyfrowane}")
        odszyfrowane = ""
def przestawieniowy(tekst):
    wynik = ""
    for j in range(0, len(tekst) - 1, 2):
        wynik += tekst[j+1]
        wynik += tekst[j]
    if len(tekst) % 2 != 0:
        wynik += tekst[-1]
    return wynik


cezar("elo zelo", 5)
odszyfrowywanie("jqt ejqt")
print(przestawieniowy("miau"))
