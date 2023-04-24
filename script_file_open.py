file = open('new_file', 'w')
file.write('new row')
file.close()

file = open('new_file', 'r')
print(file.read())

with open('new_file_2', 'w') as file2:
    file2.write('this is new file 2')

with open('new_file_with_a', 'a') as file_a:
    file_a.write('A')

with open('new_file_with_x', 'x') as file_x:
    file_x.write('I am the chosen one')
