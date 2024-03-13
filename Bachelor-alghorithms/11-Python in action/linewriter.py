def writeTextToFile(param):
    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    STATICKY_TEXT += str(param)
    with open("soubor.txt", "w", encoding="utf-8") as f:
        f.write(STATICKY_TEXT)
    return "soubor.txt"
