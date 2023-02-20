import read
whatif = input("Read or enter data? ")
if whatif == "enter":
    file=open('info.txt', 'w')
    name = input("Input your name: ")
    age = str(input("Input age: "))
    file.write(name + "\n" + age + '\n')
    file.close()
else:
    rdd = input("age or name or both?: ")
    read.dread(rdd)