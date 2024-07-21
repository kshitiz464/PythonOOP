from item import Item

item1 = Item("MyItem",750,6)
# After using property name is set to read-only attribute
# But we can still set the name by using name.setter decorator in class
item1.send_email()
print(item1.name)