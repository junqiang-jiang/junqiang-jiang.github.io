with open("C:\\Users\\Administrator\\Desktop\\pg150.txt","r") as f:
    data = f.readlines()
    string = ""
    for line in data:
        for word in line:
            for ch in "!,.?;*-" :
                word = word.replace(ch,"")
            word = word.replace("\n","")
            string = string + word.lower()
    string = string.split()

from collections import Counter
word_counts=Counter(string)
top_100=word_counts.most_common(100)
print(top_100)
