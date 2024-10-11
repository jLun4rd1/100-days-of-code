# OPENING FILES
with open('../../../../../Área de Trabalho/my_file.txt') as file:
    contents = file.read()
    print(contents)
    
    # C:\Users\joaoc\OneDrive\Documentos\Meus Projetos Python\100 Days of Python\100-days-of-code
# # CREATE A NEW FILE    
# with open('new_file.txt', mode='w') as file:
#     file.write("New text on a new file!")
    
# RELATIVE FILE PATH
# If you're in a folder called 'Project' and you
# want to access a file called 'talk.ppt', the 
# relative path to it would be:
# './talk.ppt' <<< './' means look in the current folder