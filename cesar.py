def nettoyer_texte(texte:str, strict:bool) -> str:
    accents = {
            "À": "A", "Â": "A", "Ä": "A",
            "É": "E", "È": "E", "Ê": "E", "Ë": "E",
            "Î": "I", "Ï": "I",
            "Ô": "O", "Ö": "O",
            "Ù": "U", "Û": "U", "Ü": "U",
            "Ç": "C"
    }
    texte = texte.upper()
    for accent, sans_accent in accents.items():
        texte = texte.replace(accent, sans_accent)

    if strict:
        texte = "".join([c for c in texte if "A" <= c <= "Z"])
    return texte

def code_cesar(message:str,cle:int,mode:str="chiffrer",strict:bool=False) -> str:
    resultat = []
    message = nettoyer_texte(message,strict)

    if mode == "dechiffrer":
        cle = -cle

    for c in message:
        if "A" <= c <= "Z":
            x = ord(c) - ord("A")
            y = (x + cle) % 26
            resultat.append(chr(y + ord("A")))
        else:
            resultat.append(c)
    return "".join(resultat)

x = (code_cesar("J'adore Adrien Davidoubibou",3))
(code_cesar(x,3,"dechiffrer"))