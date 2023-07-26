class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to cart", self.name, self.lastName, self.age)

customer1 = Customer()
customer1.name = "Chekchon"
customer1.lastName = "Sriprasert"
customer1.age = 26
customer1.addCart()

customer1 = Customer()
customer1.name = "Panalee"
customer1.lastName = "Amatawat"
customer1.age = 17
customer1.addCart()

customer1 = Customer()
customer1.name = "Kankanok"
customer1.lastName = "Thesruang"
customer1.age = 28
customer1.addCart()