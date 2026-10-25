class pizza:
    ingredients = 3
    flavour = "margarita"
    def order(self):
        print("Your order consists of")
    def order_details(self):
        print("number of ingredients", self.ingredients)
        print("flavour of pizza", self.flavour)
ob = pizza()
ob.order()
ob.order_details() 