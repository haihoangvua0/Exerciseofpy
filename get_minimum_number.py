import random
numbers = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
def tim_so_nho_nhat(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result
min_number = tim_so_nho_nhat(numbers)
print(numbers)
print("Min number:", min_number)
