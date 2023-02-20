def dread(rdf):
    if rdf == "name":
        line = 0
    elif rdf == "age":
        line = 1
    file=open('info.txt', 'r')
    text = file.readlines()
    file.close()
    text = text[line]
    print(text)