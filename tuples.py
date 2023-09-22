my_smartphone = ('Iphone', True, {'CPU': 'snapdragon8+gen1'}, 4800)
other_phone = ('Iphone', False, {'CPU': 'snapdragon8+gen2'}, 3600)
senx = (my_smartphone, other_phone)
print(my_smartphone == other_phone)
print(my_smartphone[0])
print(other_phone[3])
print(id(my_smartphone) == id(other_phone))
print(type(senx))


