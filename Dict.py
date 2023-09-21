user_1 = {
    'name': 'Arstan',
    'sur_name': 'Asylbekov',
    'age': '19',
    'education': 'High'
}

user_2 = {
    'name': 'Ali',
    'sur_name': 'Aliev',
    'age': '18',
    'education': 'High'
}

print(id(user_1), (id(user_2)))
print(user_1 == user_2)
print(user_1)
print(user_2)


my_car_first = {
    'brand': 'Lexus',
    'price': 30000,
    'engine_vol': 5.8
}

my_car_second = {
    'brand': 'BMW',
    'price': 44000,
    'engine_vol': 4.5
}

print(my_car_first['price'])
print(my_car_second['brand'])
my_car_second['price'] = 100_000
print(my_car_second['price'])

my_car_first['is_new'] = True
print(my_car_first)

corp_pc_1 = {
    'label': 'lenovo',
    'model': 'Gaming Pad',
    'CPU': 'intel core i7',
    'GPU': '3090TI'
}

corp_pc_2 = {
    'label': 'Asus',
    'model': 'Rog Strix',
    'CPU': 'Intel core i5',
    'GPU': 'GTX 1050TI'
}

corp_pc_1['ОЗУ'] = '8gb'
corp_pc_2['ОЗУ'] = '16gb'
del my_car_first['is_new']
print(my_car_first, my_car_second, corp_pc_1, corp_pc_2)






