# Apple , Strawberry , Banana are the object class of grocery


from Grocery import*

# Identities of all the fruits mentioned below including calories and price per kg
Apple = fruits('Kazakhstan','Red', 'No','Yes','it is not',73,5)
Strawberry = fruits('Europe','Red','yes','No','Yes it is',33,18)
Banana= fruits('Southeast asia','Yellow','No','No','it is not',89,9)


# print apple,strawbeery,banana 
print('Apple     : '+ Apple.__str__())
print('Strawberry: '+ Strawberry.__str__())
print('Banana    : '+ Banana.__str__())

for i in range(0,9):
    Apple.increase()
    Strawberry.increase()
    Banana.decrease()
    print(i)

print('Apple      : '+ Apple.__str__())
print('Strawberry : '+ Strawberry.__str__())
print('Banana     : '+ Banana.__str__())

# function that use parameters and returns some value
def calculateTotal(appleTotal):
    total= (appleTotal*Apple.price)
    return total

print(calculateTotal(5))

def calculateTotal(strawberryTotal):
    total= (strawberryTotal*Strawberry.price)
    return total

print(calculateTotal(18))

def calculateTotal(bananaTotal):
    total= (bananaTotal*Banana.price)
    return total

print(calculateTotal(9))

