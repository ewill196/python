path = '/home/ewill/python/rebrain_python/06/'
#with open(path+'file01.txt', 'a') as f1, open(path+'file02.txt') as f2:
#    text = f2.read()
#    f1.write('\n' + text)

#path = '/home/ewill/experements/files/'
#f = open(path+'file01.txt')
#text = f.read()
#print(text)
#f.close()

#w_file = open(path+'out.txt', 'w')
#w_file.writelines(['line1\n','line2\n', 'line3\n']) #список строк
#w_file.close()

with open(path+'in.txt') as f:
    words = f.read()
    words = words.split()
    print(words)

frequency = {}
for w in words:
    for ch in w:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 0
#print(frequency)

print(*sorted([(i[1], i[0]) for i in frequency.items()], reverse=True), sep='\n')