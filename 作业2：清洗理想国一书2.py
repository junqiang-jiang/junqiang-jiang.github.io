def getText():
    txt=open("C:\\Users\\Administrator\\Desktop\\pg150.txt","r").read()
    txt=txt.lower()
    for ch in '~!@$#%^&*(),./;\][]{}|:><?=-_+"':
        txt=txt.replace(ch," ")
    return txt

myTxt=getText()

words=myTxt.split()

counts={}

for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())

items.sort(key=lambda x:x[1],reverse=True)

for i in range(100):
    word,count=items[i]
    print("{0:<100}{1:>5}".format(word,count))
