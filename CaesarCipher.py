Parray=[]
Carray=""
NewParray=""

P=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
C=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
PlainText=input("Enter your String :  ")
Key=int(input("Enter key value:  "))
Parray=PlainText
for i in range(0,len(Parray)):  
    Element=Parray[i]
    if Element==" " :
        Carray+=" "
    else:
        for J in range(0,26):
            if Element==P[J]:
                sum=(J+Key)%26
                break
            else:
                continue
            break
        Value=C[sum]
        Carray+=Value
print(Carray)

for i in range(0,len(Carray)):  
    Element=Carray[i]
    if Element==" " :
        NewParray+=" "
    else:
        for J in range(0,26):
            if Element==C[J]:
                sum=(J-Key)%26
                break
            else:
                continue
            break
        Value=P[sum]
        NewParray+=Value   
print(NewParray)