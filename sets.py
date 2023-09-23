my_reading_mangas = {'Lookizm', 'How to fight', 'Solo leveling'}
other_mangas = {'How to fight', 'Lookizm', 'Solo leveling'}
print(id(my_reading_mangas))
print(id(other_mangas))

post_ids = [211, 312, 445, 567]
post_ids.__getitem__(2)
print(post_ids[2])


my_set = {12, 33, 12, 33, 12, 443}
my_new_set = list(my_set)
print(my_set)
print(type(my_new_set))

photo_sizes = {'1920x1080', '800x600'}
photo_sizes.add('1024x678')
photos_memory = {'11MB', '55MB', '44MB'}
print(photo_sizes.union(photos_memory))
# Intersection находит перессечение множеств тоесть находит пхожие элементы в двух наборах и выводит его в одном экземпляре
photo_s = {'1920x1080', '1024x678', '1920x1080'}
other_s = {'1920x1080', '768x360', '1190x448'}
common = photo_s.intersection(other_s)
print(common)



