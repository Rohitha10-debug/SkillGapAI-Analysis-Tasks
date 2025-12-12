# 1
print("Hello SkillGapAI")
# Output: Hello SkillGapAI


# 2
name = "Your Name"
print(name)
# Output: Your Name



# 3
age = 25
city = "Chennai"
skill = "Python"
print(age, city, skill)
# Output: 25 Chennai Python


# 4
value = str(100)
print(type(value))
# Output: <class 'str'>


# 5
text = "python basics"
print(text.upper())
# Output: PYTHON BASICS


# 6
print(len("SkillGapAI"))
# Output: 10


# 7
colors = ["red", "blue", "green"]
print(colors[1])
# Output: blue


# 8
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)
# Output: ['apple', 'banana', 'orange']


# 9
items = ["apple", "banana", "orange"]
items.remove("banana")
print(items)
# Output: ['apple', 'orange']


# 10
nums = [1, 2, 3]
t = tuple(nums)
print(t)
# Output: (1, 2, 3)


# 11
resume = {'name': 'John', 'age': 25, 'skills': ['Python', 'SQL']}
print(resume)
# Output: {'name': 'John', 'age': 25, 'skills': ['Python', 'SQL']}


# 12
print(resume['skills'])
# Output: ['Python', 'SQL']


# 13
marks = 50
print('Pass' if marks > 40 else 'Fail')
# Output: Pass


# 14
num = 7
print('Even' if num % 2 == 0 else 'Odd')
# Output: Odd


# 15
for i in range(1, 6):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5


# 16
i = 5
while i >= 1:
    print(i)
    i -= 1
# Output:
# 5
# 4
# 3
# 2
# 1


# 17
def say_hello():
    print("Hello")

# No call, so:
# Output: No output (function not executed)

say_hello()   # If you want to show output
# Output: Hello


# 18
def add(a, b):
    return a + b

# No function call:
# Output: No output

print(add(2, 3))
# Output: 5


# 19
import math
print(math.pi)
# Output: 3.141592653589793


# 20
# Command: python -m venv myenv
# This is a terminal command, not Python code.
# Output: No output (creates virtual environment)

