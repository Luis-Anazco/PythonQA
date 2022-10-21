a = int(input('Enter the date you were born: '))
b = int(input('Enter the month you were born: '))
c = int(input('Enter the year you were born: '))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)
