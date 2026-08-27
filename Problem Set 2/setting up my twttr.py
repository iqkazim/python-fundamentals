user_input = input('Input: ')
output = ''
for i in user_input:
    if i in['a','e','i','o','u','A','E','I','O','U']:
        pass
    else:
        output = output + i

print('Output:',output)
