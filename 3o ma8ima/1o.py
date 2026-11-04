class Kathigitis:
    def __init__(self,onoma,eponymo,ilikia,mathima):
        self.onoma=onoma
        self.eponymo=eponymo
        self.ilikia=ilikia
        self.mathima=mathima
    def milao(self):#μπορούμε να κάνουμε μέθοδο όπου τα print γίνονται μόνα τους
        print("το όνομα μου είναι: "+self.onoma)
        print("το επίθετό μου είναι: "+self.eponymo)
        print("Μαζί θα κάνουμε το μάθημα: "+self.mathima)
k1=Kathigitis("giorgos","pipjsfdi :",43,"mathimatika")
k2=Kathigitis("panos","curry :",51,"ypologistes")
k3=Kathigitis("petros","petra :",66,"arxaia")
#del k2.ilikia #το del διαγράφει το atribute ilikia απο το σημείο που το γράφουμε και μετά
#print(k1.onoma,k1.eponymo,k1.ilikia,k1.mathima)
#print(k2.onoma,k2.eponymo,k2.ilikia,k2.mathima)
#print(k3.onoma,k3.eponymo,k3.ilikia,k3.mathima) 
k1.milao()
k2.milao()
k3.milao()