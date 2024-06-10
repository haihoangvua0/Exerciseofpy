temp = 0
def sort_numbers(num1, num2, num3):
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
        if num3 < num2:
            temp = num2
            num2 = num3
            num3 = temp
    return (num1, num2, num3)
a = int(input("Enter first integer: "))
b = int(input("Enter Second integer: "))
c = int(input("Enter third integer: "))

x, y, z = sort_numbers(a, b, c)
print("Original numbers: ", a, b, c)
print("Sorted numbers: ", x, y, z )
