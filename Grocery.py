# This program will tell us about grocery and its sub classes
# grocery is the main class.


class Grocery(): 
    def __init__(self,origin,colour,seasonal,calories,price):
        self.origin   = origin
        self.colour   = colour
        self.seasonal = seasonal
        self.calories = calories
        self.price    = price

# Similar properties in fruits and vegetables

    def __str__(self):
        return f'{self.origin} {self.colour} {self.seasonal}'

    def increase(self):
         self.price = self.price+1

    def decrease(self):
        self.price = self.price-1

            

# Fruits= Class
# Different properties of fruits by which we can identify the fruit

class fruits(Grocery):
    def __init__(self,origin,colour,seasonal,seeds,riped,calories,price):
        super().__init__(origin,colour,seasonal,calories,price)
        self.seeds = seeds
        self.riped = riped

    def __str__(self):
        return super().__str__() + f' {self.seeds} seeds,'\
               f' {str(self.riped)} riped,'\
               f' {str(self.calories)} kcal,'\
               f'current price is  aed {self.price} /kg'
        
