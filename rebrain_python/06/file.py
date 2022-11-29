#with open('file01.txt', 'a') as f1, open('file02.txt') as f2:
#    text = f2.read()
#    f1.write('\n' + text)

f = open('./file01.txt')
text = f.read()
print(text)
f.close()