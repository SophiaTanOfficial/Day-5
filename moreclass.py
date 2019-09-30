class Product:
    def __init__(self,thisName,thisPrice):
        self.name=thisName
        self.price=thisPrice
        self.stock=0 #this is NOT a parameter value - we are saying ANY new object instance starts at 0
        
    def receive(self, quantity):
            self.stock +=quantity
            print(f"Received {quantity} {self.name}.")
            
#PRODUCT CLASS ENDS HERE
class Cart:
    def __init__(self, discount = 0.0):
        self.items = [] #List of Product objects
        self.discount = discount
        self.total = 0
        print("New cart created!")
        
    def getTotal(self):
        for item in self.items:
            self.total += item.price #self.total talks about the cart object #item.price is talking about an item in cart which is a Product object
        return self.total
        
    def addItem(self, product, quantity): #Product is taking in an object
        if product.stock ==0:               #.stock is a property of product object
            print("Sorry, we out.")
            return False
        elif product.stock < quantity:
            print(f"You can only buy {self.stock} of this item.")
            return False
        else:
            for each in range(quantity):
                self.items.append(product)
            print("Item(s) added successfully!")
            self.getTotal() #Calculate total after adding items
            print("Your new total is " + str(self.total))
#Cart class ends here

#Program begins here
faceMask = Product("face mask",4.99)
pokeball = Product("pokeball",10)

faceMask.receive(10)
pokeball.receive(10)
shoppingCart = Cart()
shoppingCart.addItem(pokeball,10)

