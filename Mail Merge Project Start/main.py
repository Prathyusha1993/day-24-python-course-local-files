#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'
with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f'./Output/ReadyToSend/letter_to_{stripped_name}.docx', 'w') as completed_letter:
            completed_letter.write(new_letter)








# with open('Input/Letters/starting_letter.txt', 'r') as file:
#     file_content = file.read()
#
# file_content = file_content.replace('[name]', 'Aang')
#
# with open('Output/ReadyToSend/letter_to_aang.txt', 'w') as file:
#     file.write(file_content)
