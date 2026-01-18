word = "swiss"
freq={}
for ch in word:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in word:
    if freq[ch]==1:
        print([ch])
        break
