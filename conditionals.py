#name = input('Please enter your name: ')

#if name == 'Dave':
#    print('No thanks!')
#else:
#    print(f'Hello {name}!')


#if name > 'Dave':                   #the > sign makes it evaluate the number of characters in the input string
#    print('No thanks!')             #it will only print this if the name is 5 or more characters long
#else:
#    print(f'Hello {name}!')         #it will only print this if the name is 4 or less characters long


eng_mark = float(input('Please enter your English mark here: '))

#Exercise 1
if eng_mark > 65:
    print('Pass')
elif eng_mark <= 65:
    print('Fail')

#Exercise 2
if eng_mark > 65:
    print('Pass')
else:
    print('Fail')


#Exercise 3
if eng_mark < 40:
    print('Fail')
elif 40 <= eng_mark < 50:
    print('Pass')
elif 50 <= eng_mark < 60:
    print('Merit')
elif 60 <= eng_mark <= 100:
    print('Distinction')
else: 
    print('Incorrect score. The score must be between 0 and 100')