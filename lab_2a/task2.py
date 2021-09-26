#!/usr/bin/python3

#i
print("Перша константа", True)
print("Друга константа", False)
print("Третя константа", None)

#ii
print(f"4 в квадраті = {pow(4,2)}")
print(f"Максимальне число серед чисел 28, 20, 45, 7: {max(28,20,45,7)}")
x = 2
print(f"x + 2 = {eval('x+2')}")

#iii
for i in range(1,7):
    if i%2!=0:
        print(f"Число {i} - непарне")
    else:
        print(f"Число {i} - парне")

z = 4
while (z > 0):
    print(f"Цикл while завершиться через: {z}")
    z -= 1

#iv
x = '5'
try:
    x += 7
except TypeError as error:
    print(f"Error: {error}, occured, please check your code")
finally:
    print(f"x = {x}({type(x)})")

#v
with open("README.md", 'r') as readme_file:
    first_str = readme_file.readline()
    print(first_str)

#vi
area_of_rectangule = lambda x, y: print(f"Площа прямокутника: {x*y}")
area_of_rectangule(2,8)
