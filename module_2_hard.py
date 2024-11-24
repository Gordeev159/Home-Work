import  random
numbers = list(range(3, 21)) # исходный диапазон возможных чисел от 3 до 20
password = []
num = random.choice(numbers) # случайно выпавшее число
print('Выпало число: ' ,num)
for i in range(1, num): # условие для подбора пароля
    for j in range(i + 1, num):
        if num % (i + j) == 0:
            password.append([i, j])
output = ''
for x in password:
    output += str(x[0]) + str(x[1])
print('Пароль: ', output)