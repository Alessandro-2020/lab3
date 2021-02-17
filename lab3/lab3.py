def shifrovka (word, key):
        result = ''
        for l,k in zip(word,word):
                new_l = ord(l)
                result+=chr(key[new_l])
        return result

def deshifrovka (word, key):
    result = ''
    for l,k in zip(word, word):
            new_l = ord(l)
            if new_l in key:
                new_l2=new_l
            else:
                continue
            result+=chr(key.index(new_l2))
    return result
a=5
y0=3091
m=(16384)
wo = open('Source.txt','rt', encoding='utf-8')
for line in wo:
    word=line
key = [((a * y0) % m)]
for i in range(1, 100000):
    key.append((a * key[i-1]) % m)
coded=open('Coded.txt','w', encoding='utf-8')
decoded=open('DeCoded.txt','w', encoding='utf-8')
s=(shifrovka (word, key))
d=(deshifrovka (word, key))
for index in s:
        coded.write(index)
coded.close()
for index in d:
        decoded.write(index)
coded.close()
