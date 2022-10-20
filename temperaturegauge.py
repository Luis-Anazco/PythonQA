#Exercise 4
temperature = 40
if (temperature > 30):
    print('too hot')
    print('aagh')
    if (temperature > 50):
        print('AAH')
print('too cold')

temperature = float(input('Please enter the temperature here: '))
if (temperature > 30):
    print('too hot')
    print('aagh')
elif (temperature > 50):
    print('AAH')
else: 
    print('too cold')


#Exercise 5
temperature = 40
if (temperature > 30):
    print('too hot')
    print('aagh')
if (temperature < 0):
    print('too cold')
if (temperature > 0):
    print('perfect')

#temperature = 20 -> prints 'perfect'
#temperature = 40 -> prints 'too hot', 'aagh', 'perfect'
#temperature = -10 -> prints 'too cold'

#Exercise 6
temperature = 40
if (temperature > 30):
    print('too hot')
    print('aagh')
if (temperature < 0):
    print('too cold')
else:
    print('perfect')

#it will print the same strings for the same values but using an else-statement at the end
#which will be part of the second evaluation it is conducting (second if-statement)


#Exercise 7
temperature = 40
if (temperature > 30):
    print('too hot')
    print('aagh')
elif (temperature < 0):
    print('too cold')
else:
    print('perfect')

#This implementation is better than using multiple if-statements or two if-statements and 
#an else-statement because it will evaluate all of the code together as opposed to 
#conducting separate evaluations for the separate if-statements

