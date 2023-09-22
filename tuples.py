my_smartphone = ('Iphone', True, {'CPU': 'snapdragon8+gen1'}, 4800)
other_phone = ('Iphone', False, {'CPU': 'snapdragon8+gen2'}, 3600)
senx = (my_smartphone, other_phone)
print(my_smartphone == other_phone)
print(my_smartphone[0])
print(other_phone[3])
print(id(my_smartphone) == id(other_phone))
print(type(senx))
print(senx)

my_nums = (111, 345, 667, 888, 776)
print(type(my_nums))
print(my_nums)
my_users = (
    {
        'user_id': 100,
        'user_age': 20,
        'email': 'guest_new119pip@gmail.com',
        'password': 7587534794
    }
)


my_new_account = 'asylbekov20love@gmail.com'
my_new_password = '578937453495'
is_new = True
all_information = (my_new_account, my_new_password, is_new)
print(all_information)
print(len(all_information))

internal_ids = (123, 454, 787, 6786)
external_ids = (566, 6546, 646, 876)
in_ex_ids = internal_ids + external_ids
print(in_ex_ids)
print(internal_ids + external_ids)
print(id(internal_ids) == id(external_ids))


