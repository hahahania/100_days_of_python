import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

word = input("Enter the word you want to translate to nato alphabet : ").upper()

output = [row.code for char in word for (index,row) in data.iterrows() if row.letter == char ]
print(output)

