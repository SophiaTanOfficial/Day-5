class Product:
    def __init__(self, thisName, thisPrice):
        self.price = thisPrice     
        self.name = thisName
        self.stock = 0
    def receive(self, quantity):
        self.stock += quantity
        print("Stock received. Current stock is " + str(self.stock))
    def sell(self, quantity):
        if self.stock == 0:
            print(f"Sorry, we don't have any {self.name} in stock.")
        elif quantity > self.stock:
            print(f"Sorry, we only have {self.stock} available")
        else:
            self.stock -= quantity
            print("Sale successful")
    
#Class ends here, program begins below

product1 = Product("Colored Pencils", 4.99) #Creates object
print(product1) #Print whole object - not useful
print(product1.name) #Print name of object
print(product1.price) #Print price of object
print(product1.stock) #Print current stock of object


product1.receive(100) #Run method to add to stock
print(product1.stock) #Check the stock again

product1.sell(25)
print(product1.stock)
product1.sell(15)
print(product1.stock)

# 0) Create a new variable product2 of "pens" with a price of your choice
# 1) Receive stock of 50 pens.
# 2) Then sell off 10 of pens.
# 3) Create a third product. Receive some amount. Then sell some.
# 4) Try to sell off more of something than you have in stock and confirm that your .sell() method is not buggy.
# 5) STRETCH: Create a class for CustomerAccount on our site. Initialize the first customer (whose name is “Johnny Test”).

product2 = Product("Pens", 5.99)
product2.receive(50)
product2.sell(10)

product3 = Product("Lined paper", 10)
product3.receive(100)
product3.sell(35)
product3.sell(100)

class CustomerAccount:
    def __init__(self, thisName, thisMem):
        self.name = thisName
        self.Mem = thisMem

customer1 = CustomerAccount("Johnny Test", "Premium")
print(customer1.name, customer1.Mem)