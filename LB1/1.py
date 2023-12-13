listEnigma=[1,2,6,4,2,8,4,8,'l',4,6,21,4,68,7]
for i in range(len(listEnigma)):
    if not type(listEnigma[i])==int:
        b=i
listEnigma[b]=0
Summa=sum(listEnigma)
Dlina=len(listEnigma)
average=Summa/Dlina
listEnigma[b]=average
print(listEnigma)