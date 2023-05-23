path = '/Users/haniazwolinska/Desktop/100days_of_python/intermediate_level/Mail Merge Project Start/Input/Letters/starting_letter.txt'
path2 = '/Users/haniazwolinska/Desktop/100days_of_python/intermediate_level/Mail Merge Project Start/Input/Names/invited_names.txt'


with open(path, 'r') as pattern:
    lines = pattern.read()

with open(path2, 'r') as name_file:
    names = name_file.read().split('\n')



for name in names:
    letter = lines.replace('[name]',name)
    with open(f'/Users/haniazwolinska/Desktop/100days_of_python/intermediate_level/Mail Merge Project Start/Output/{name}_invitation','w') as file:
        file.write(letter)
