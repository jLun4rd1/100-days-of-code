#TODO: Create a letter using starting_letter.txt 
with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    
with open('Input/Names/invited_names.txt') as names_file:
    names_list = names_file.readlines()

for name in names_list:
    stripped_name = name.strip("\n")
    new_letter = letter.replace('[name]', stripped_name)
    with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', 'w') as new_letter_file:
        new_letter_file.write(new_letter)
        
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp