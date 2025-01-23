# reading file contents
with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

# writing to existing file by using mode = 'a' which is append
with open('my_file.txt', mode='a') as file:
    file.write('\nNew Text.')

with open('new_file.text',mode='w') as file:
    file.write('New text...')