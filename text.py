def replacel(filen, linen, text):
    with open(filen) as file:
        lines = file.readlines()
    lines[linen -1] = text
    print(lines)
filen =input("file: ")
linen =int(input("Line: "))
text =input("text: ")

replacel(filen, linen, text)