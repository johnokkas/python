def artioi(arithmoi):
    lista=[]
    for x in arithmoi:
        if x%2==0:
            lista.append(x)
    return lista
lista1=[8,1,16,3,10,5,6]
y=artioi(lista1)
print("artioi :",y)
artioi= list(filter(lambda x: x%2!=0,lista1))
print("peritoi :",artioi)
lista2=[2,-1,-4,-7,8,-9]
thetikoi= list(filter(lambda x: x>0,lista2))
print("thetikoi :",thetikoi)