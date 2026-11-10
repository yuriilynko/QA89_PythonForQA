import numbers
from difflib import restore

empty_list = []
mixed_list = [2,'orange',4.22,True]

fruits = ['orange', 'strawberry', 'mango']
print(fruits)
print(fruits[0])

fruits[1] = 'lemon'
print(fruits)
print(fruits[1])

print()
list1 = ['orange','lemon']
list2 = ['shampoo','soap']
combo_list = list1 + list2
print(combo_list)

fruits = ['orange', 'strawberry', 'mango','apple']
first, second, third, *rest = fruits
print(first)
print(second)
print(third)
print(rest)

fruits = ['orange', 'strawberry', 'mango']
for item in fruits:
    print(f"item in fruits: {item}")

#correct_answers.lower = ['orange', 'strawberry', 'mango']
correct_answers = ['orange', 'strawberry', 'mango']
correct = [word.lower() for word in correct_answers]
user_answers = ['orange', 'strawberry', 'mango']
submitted = [word.strip().lower() for word in user_answers]

if correct == submitted:
    print("Correct answers")
else:
    print("Incorrect answers")

print(len(fruits))
max(fruits)
print(max(fruits))

numbers = [12,56,94,6]
print(max(numbers))
print(min(numbers))
print()

res = sorted(numbers)
print(res)
print(numbers)

print(sorted(numbers,reverse=True))
print(sorted(fruits))
print(sorted(fruits,reverse=True))

word = 'python'
print(sorted(word))
result= ''.join(sorted(word))
print(result)

names = ['Aleks','Kristina','Bob','Tom']
print(sorted(names))
print(sorted(names,key=len))

#по алфавиту
names.sort()
print(names)

names.sort(key=len)
print(names)

