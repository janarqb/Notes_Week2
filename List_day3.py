nums = 1, 2, 3
# print(type(words))

# print(words[:2])

# one, two, three = num(s
# print(two)


# a = ()
# b = ()
# print(a is b) 
# print(id(a))
# print(id(b))

# a = (1, 2, 3)
# print(id(a))
# del a
# b = (1, 2, 3)
# print(id(b))

countries = (
    ('Germany', 80.2, (('Berlin', 3.326), ('Huburg', 1.718))),
    ('France', 66, (('Paris', 2.2, ('Marsel', 1.6))))
)
for country in countries:
    country_name, country_population, cities = country
    print('\nCountry: {} population: {}'.format(country_name, country_population))
    for city in cities:
        city_name, city_population = city
        print('City: {} population: {}'.format(city_name, city_population))
    print(country)
    print(country_name)
    print(country_population)
    print(cities)
    print('===============')


# nested = (1, [1, 2, 4], 'do', ('param', 10, 20))
# nested[3].append('new')
# print(nested)


users = {1: 'Tom', 2: 'Bob', 3: 'Bill'}
objects = {}
elements = {'Au': 'Gold', 'Fe': 'Железо', 'H':'Водород', 'O': 'Oxygen'}
new = ((1, True), (2, False), (3, 'Echo'))
# new_ = dict(new)
# print(type(new_dict))
# print(type(users))
# print(type(objects))

# new = dict(a=1, b=2, c=3)
# print(new)

# # elements['Au'] = 'Золото'
# # print(elements)
# users[4] = 'Aybek'
# print(users)

# print(users.get(10))

# del users [2]
# print(users.fromkeys(range(1,9), ['one', 'two']))

# print(users.items())

# print(users.pop(3))

# print(users.popitem())

# for id_, user in users.items():
#     print(id_, "*****", user)