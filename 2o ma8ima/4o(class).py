class Mathitis:
    def __init__(self,onoma,ilikia):
        self.onoma=onoma
        self.ilikia=ilikia
class Kathigitis:
    def __init__(self,onoma,eponymo,ilikia,mathima):
        self.onoma=onoma
        self.eponymo=eponymo
        self.ilikia=ilikia
        self.mathima=mathima
m1=Mathitis("kostas :",25)
m2=Mathitis("mhtsos :",24)
m3=Mathitis("bill :",20)
print(m1.onoma,m1.ilikia)
print(m2.onoma,m2.ilikia)
print(m3.onoma,m3.ilikia)
k1=Kathigitis("giorgos","pipjsfdi :",43,"mathimatika")
k2=Kathigitis("panos","curry :",51,"ypologistes")
k3=Kathigitis("petros","petra :",66,"arxaia")
print(k1.onoma,k1.eponymo,k1.ilikia,k1.mathima)
print(k2.onoma,k2.eponymo,k2.ilikia,k2.mathima)
print(k3.onoma,k3.eponymo,k3.ilikia,k3.mathima)