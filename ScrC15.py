myFile = open('filename.txt')
myFile = open('filename.txt', 'rt')
myFile = open('filename.txt', 'rt', encoding="utf8")
myFile = open('filename.txt')
print(myFile.read(15))

myFile = open('filename.txt')
print(myFile.readlines())

myFile = open('filename.txt')
for line in myFile:
    print(line)

myFile = open('namefile.txt', 'w')
myFile.write('tttt')
print('zzzz', file=myFile)

with open("namefile.txt") as myFile:
    for line in myFile:
        print(line)
