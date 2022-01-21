import csv 
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str,price: float, quantity):
        # print(f"An instance created: {name}")
        
        #Run validations to the received arguments
        assert price >=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to Execute
        Item.all.append(self) 

    def calculate_total_price(self):
        return self.price*self.quantity  

    def apply_discount(self):
        self.price = self.price * Item.pay_rate 

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"  

# item1 = Item("Phone",100,1)
# item1 = Item("Laptop",1000,3)
# item1 = Item("Cable",10,5)
# item1 = Item("Mouse",50,5)
# item1 = Item("Keyboard",75,5)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)

Item.instantiate_from_csv()
print(Item.all)