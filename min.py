def min(number):
    smallest = number[0]
    for num in number:
        if smallest> num:
            smallest = num
    return(smallest)

number = input('Nhập 1 dãy số: ')
print(min(number))
