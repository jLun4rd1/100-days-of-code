import pandas

#TODO 1. Create a dictionary in this format:    
alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Type a word: ').upper()
nato_translation = [alphabet_dict[letter] for letter in user_word]
# nato_translation = []
# for letter in user_word:
#     nato_translation.append(alphabet_dict[letter])
print(nato_translation)
