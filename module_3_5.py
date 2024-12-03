def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first != 0:
        return first
    else:
        return 1

result_1 = get_multiplied_digits(20504)
result_2 = get_multiplied_digits(205040)

print(result_1)
print(result_2)