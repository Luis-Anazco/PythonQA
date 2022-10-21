#Exercise 1
print(len('hive'))

#Exercise 2
full_name = 'Luis Fernando Anazco Anazco'
lower_name = full_name.lower()
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency(lower_name)) 

#Exercise 3
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('helloworld'))
print(string_both_ends('hi'))
print(string_both_ends('h'))

#Exercise 4
