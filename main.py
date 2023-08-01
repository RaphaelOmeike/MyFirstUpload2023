from item import Item
# from phone import Phone

item1 = Item("MyItem", 750)
# Setting an Attribute
item1.name = "OtherItem" 
#item1.__Item__name_ = "yeag"
print(item1.name) # Encapsulation

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)



# # Item.instantiate_from_csv()
# # print(Item.all)
# # print(Item.is_integer(2.5))
# phone1 = Phone("jscPhonev10", 500, 5, 1)
# # jcbf = Item("RA", 243)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700, 5, 1)
# print(Item.all)
# print(Phone.all)

'''item1 = Item("Raphael", 100, 1)
print(item1.name)
print(item1.price)
print(item1.calculate_total_price())
print(Item.__dict__) # All the attributes for Class level 
print(item1.__dict__) # All the attributes for the instance level
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)'''

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)
# CSV - Comma Separated Values.