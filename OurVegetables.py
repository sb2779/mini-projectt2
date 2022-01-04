# Brinjal , Tomato , Broccoli are the object class  

from Vegetables import*

# Identities of all the vegetables including calories in kcal and price per kg
Brinjal = Vegetables('India','Purple','Yes', 'Root',25,'Bitter',8)
Tomato =  Vegetables('America','Red','No', 'Stem',22,'Tarty',7)
Broccoli= Vegetables('Asia','Green','Yes', 'Stem',33,'Grassy',9)



# print brinjal,tomato,broccoli

print('Brinjal :'+ Brinjal.__str__())
print('Tomato  :'+  Tomato.__str__())
print('Broccoli:'+ Broccoli.__str__())


# functions that take parameters and return some value

def calculateTotal(brinjalTotal):
    total=(brinjalTotal*Brinjal.price)
    return total

print(calculateTotal(8))

def calculateTotal(tomatoTotal):
    total=(tomatoTotal*Tomato.price)
    return total

print(calculateTotal(7))

def calculateTotal(broccoliTotal):
    total=(broccoliTotal*Broccoli.price)
    return total

print(calculateTotal(9))


