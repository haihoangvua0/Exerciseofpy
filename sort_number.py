def sort_numbers(num1, num2, num3):
    """
    Sắp xếp ba số nguyên theo thứ tự tăng dần.

    Args:
        num1 (int): Số nguyên thứ nhất.
        num2 (int): Số nguyên thứ hai.
        num3 (int): Số nguyên thứ ba.

    Returns:
        tuple: Ba số đã sắp xếp theo thứ tự tăng dần.
    """
    if num2 < num1:
        num1, num2 = num2, num1
    if num3 < num1:
        num1, num3 = num3, num1
    if num3 < num2:
        num2, num3 = num3, num2
    return num1, num2, num3

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

x, y, z = sort_numbers(a, b, c)
print("Các số ban đầu: ", a, b, c)
print("Các số đã sắp xếp: ", x, y, z)
