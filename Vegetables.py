# This is the second class of the library in this vegetables is a class with all its basic properties



from Grocery import *

# root/stem/leaves and taste make vegetables different from fruits

class Vegetables(Grocery):
    def __init__(self,origin,colour,seasonal, root_stem_leaves,calories,taste,price,):
        super().__init__(origin,colour,seasonal,calories,price)
        self.root_stem_leaves = root_stem_leaves
        self.taste = taste
        
         
        
    def __str__(self):
        return super().__str__() + f'{str(self.root_stem_leaves)} ,'\
               f' {str(self.calories)} kcal,'\
               f' taste is {str(self.taste)} ,'\
               f' current price is aed {str(self.price)} \kg,'\
               
