myString = input()                  # Reading input from STDIN
d = dict()

for ch in myString:
    
    if ch in d.keys():
        d[ch]+=1
    else:
        d[ch]=1

odd = 0

for key in d.keys():
    if d[key]%2!=0 :
        odd+=1

if odd>1:
    print("NO")
else:
    print("YES")
