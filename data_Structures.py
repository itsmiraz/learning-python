# # Data structures and with their methods

# # String

# name = 'Mirajul'


# s = 'hello world'


# # Methods of string

# # print(s.upper()) # HELLO WORLD
# # print(s.lower()) # hello world
# # print(s.title()) # Hello World
# # print(s.strip()) # removos leading/trailingwhitespace
# # print(s.replace('l','-')) # he--0 wor-d
# # print(s.split(" ")) # ['hello', 'world']
# # print(s.find('o')) # 4
# # print(s.count("l"))# 3
# # print(len(s))


# # Arrays /lists

# fruits =['banana','apple','cherry']


# # fruits.append('orange')
# # print(fruits)

# # fruits.insert(1,'grep')
# # print(fruits)
# # fruits.remove('banana')
# # print(fruits)
# # fruits.pop()
# # print(fruits)

# # fruits.sort()
# # print(fruits)

# # fruits.reverse()
# # print(fruits)

# # # fruits.clear()
# # # print(fruits)


# # print(fruits.index('grep'))
# # print(len(fruits))

# numbers =[1,2,3,4,5]

# # print(numbers[1:4])
# # print(numbers[:2])
# # print(numbers[::2])
# # print(numbers.reverse())
# # print(numbers)


# # Tuples
# point=(10,20)

# print(point.index(10))
# print(point.index(20))
# print(len(point))



# # Dictionaries /objects


# person = { 'name':"Miraj", "age":24}

# person["age"] = 23
# person.get('age')

# person["city"] = "Dhaka"

#  Sets (set())
nums = {1, 2, 3, 2}
print(nums)   # {1
nums.add(4)
nums.remove(2)
nums.discard(100)   # doesn't error
nums.pop()          # removes random element
nums.clear()

#  Set Operations:
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)        # {1, 2, 3, 4, 5}
a.intersection(b) # {3}
a.difference(b)   # {1, 2}


# ⚡ 6. List Comprehensions
# Squares of numbers 0 to 4
squares = [x**2 for x in range(5)]
# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
#  Nested Comprehensions:
pairs = [(x, y) for x in range(3) for y in range(3)]

