#-----------------------------
#Lessons from lesson 019 to 020
#------------------------------


num=10
print("num is :  {:.10f}" .format(num))

print("=" * 50)

num= 159.650
print(int(num))
print(type(int(num)))

print("=" * 50)

#integer
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print("=" * 50)

myComplexNumber = 1+2j
print(f"Real Part Is: {myComplexNumber.real}")
print(f"Imaginary Part Is: {myComplexNumber.imag}")

print("=" * 50)

print(100 - 115 ) #-15
print(50 * 30 ) #1500
print(21 % 4 ) #1
print(110 // 11 ) #10
print(97 // 20 ) #4

#-----------------------------
#Lessons from lesson 021 to 023
#------------------------------

friends =["mostafa","yousef","maraw","mohaned","momen"]
print(friends[0])  # mostafa
print(f"my name is {friends[0]}")  # mostafa
print(friends[4])  # momen
print(f"my name is {friends[4]}")  # momen

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]

even_index = friends[::2]  # [0, 2, 4]
odd_index = friends[1::2]  # [1, 3]
print(f"Even-indexed friends: {even_index}")
print(f"Odd-indexed friends: {odd_index}")

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]

print(friends[1:4])  # ['yousef', 'maraw', 'mohaned']
print(friends[-2:])   # [ 'mohaned', 'momen']

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]

friends[3:5] = ["ahmed", "ali"]
print(friends)  # ['mostafa', 'yousef', 'maraw', 'ahmed', 'ali']

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]
friends.insert(0, "ahmed")
print(friends)  # ['ahmed', 'mostafa', 'yousef', 'maraw', 'mohaned', 'momen']
friends.insert(6, "essam")
print(friends)  # ['ahmed', 'mostafa', 'yousef', 'maraw', 'mohaned', 'momen', 'essam']

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]
del friends[0:2] # ['maraw', 'mohaned', 'momen']
print(friends)  # ['maraw', 'mohaned', 'momen']
del friends[2] # ['maraw', 'mohaned']
print(friends)  # ['maraw', 'mohaned']

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]
employees = ["abdel elsayed", "mohamed"]
school = ["abdel elmalkey", "yahia"]

friends.extend(employees)
friends.extend(school)
print(friends)

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]
friends.sort(reverse=False)
print(friends)  # ['maraw', 'mohaned', ' momen', 'mostafa', 'yousef']

friends =["mostafa","yousef","maraw","mohaned","momen"]
friends.sort(reverse=True)
print(friends)  # ['yousef', 'mostafa', ' momen', 'mohaned', 'maraw']

print("=" * 50)

friends =["mostafa","yousef","maraw","mohaned","momen"]
count =  len(friends)
print(f"Number of friends: {count}")
print(f"Number of friends: {len(friends)}")
print(count)

print("=" * 50)

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])  # Django
print(technologies[4][2])  # Web

print("=" * 50)

#-----------------------------
#Lessons from lesson 024 to 025
#------------------------------

my_name = "mostafa",
print(f"Hello, my name is {my_name}.")  # Hello, my name is ('mostafa').
print(type(my_name))  # <class 'tuple'>

print("=" * 50)

friends =("mostafa","yousef","maraw")
friends = ("disha",) + friends[1:]
print(friends)  # ('disha', 'yousef', 'maraw']
print(type(friends))  # <class 'tuple'>
print(f"Number of friends: {len(friends)}")  # Number of friends: 3

print("=" * 50)

nums = (1, 2, 3)
letters = ("A", "B", "C")
n = nums + letters
print(n)  # (1, 2, 3, 'A', 'B', 'C')
print(len(n))  # 6

print("=" * 50)

my_tuple = ("A", "B", 4, "C")

x, y, _, z = my_tuple

print(x)
print(y)
print(z)

print("=" * 50)

#-----------------------------
#Lessons from lesson 026 to 032
#------------------------------

my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))
print(unique_list)  # [1, 2, 3, 4, 5]
print(type(unique_list))
print(unique_list[:4])

print("=" * 50)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

m = nums | letters
o = nums.union(letters)
nums.update(letters)
print(m)  # {1, 2, 3, 'A', 'B', 'C'}
print(o)  # {1, 2, 3, 'A', 'B', 'C'}
print(nums)  # {1, 2, 3, 'A', 'B', 'C'}

print("=" * 50)


my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)  # {1, 2, 3}
my_set.clear()
print(my_set)  # set()
my_set.add("a")
my_set.add("b")
print(my_set)  # {'a', 'b'}
my_set.discard("c")  # No error if the element doesn't exist

print("=" * 50)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))  # True
print(set_two.issuperset(set_one))  # True

print("=" * 50)

skills ={ 
    "HTML": "90%",
    "CSS": "80%",
    "JS": "70%"

}
print(f'"html progress is {skills["HTML"]}"')  # "progress is 90%"
print(f'"css progress is {skills["CSS"]}"')  # "progress is 80%"
print(f'"js progress is {skills["JS"]}"')  # "progress is 70%"

skills["Python"] = "60%"
print(f'"python progress is {skills["Python"]}"')  # "progress is 60%"

print("=" * 50)
