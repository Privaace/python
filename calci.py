a=int(input("enter 1st word: "))
b=int(input("enter 2nd word: "))

need=input("operator bey: ")

if need == '+'  :
    result=a+b
    print(result)
elif need == '-' :
    result=a-b
    print(result)
elif need == '*' :
    result=a*b
    print(result)
elif need == '/' :
    result=a/b
    print(result)
else :
    print("invalid operator")

