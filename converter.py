characters_per_row = 15

fictional_alphabet = {
    
    "a": ['   ',
          '---',
          '  /'],
    
    "b": ['| *',
          '|--',
          '|  '],

    "c": ['   ',
          '\\ /',
          ' V '],

    "d": ['* |',
          '--|',
          '  |'],
    
    "e": ['   ',
          '-/-',
          '   '],

    "f": ['   ',
          ' ^ ',
          '/ \\'],

    "g": [' |*',
          '-+-',
          ' | '],

    "h": [' ^ ',
          '< >',
          ' ˘ '],

    "i": ['/  ',
          '---',
          '   '],

    "j": ['\\ /',
          ' //',
          '//\\'],

    "k": [' | ',
          '-+-',
          ' | '],

    "l": ['  /',
          ' / ',
          '/  '],

    "m": ['---',
          ' | ',
          ' | '],

    "n": ['---',
          ' | ',
          '---'],

    "o": ['   ',
          '---',
          '   '],

    "p": ['|  ',
          '|--',
          '|  '],

    "q": [' | ',
          '-+-',
          ' | '],

    "r": ['   ',
          '/V\\',
          '   '],

    "s": ['\\  ',
          ' \\ ',
          '  \\'],

    "t": ['  |',
          '--|',
          '  |'],

    "u": ['/  ',
          '---',
          '  /'],

    "v": ['   ',
          '/ /',
          '   '],

    "w": ['   ',
          '///',
          '   '],

    "x": [' \\ ',
          '-|\\',
          ' | '],

    "y": ['--/',
          ' //',
          '// '],

    "z": ['\\ *',
          ' \\ ',
          '  \\']
    }

extra_characters = {

    " ": ['   ',
          '   ',
          '   '],

    ".": ['   ',
          '   ',
          ' ° '],

    ",": ['   ',
          '   ',
          ' , '],
    }


input_text = input("Input text : ")
input_text = input_text.lower()


output_rows = [['', '', '']]
row_index = 0
characters_in_row = 0

for character in input_text:
    
    if character in fictional_alphabet:
        converted_character = fictional_alphabet[character]
        for i in range(3):
            output_rows[row_index][i] += converted_character[i] + " "
        characters_in_row += 1

    elif character in extra_characters:
        converted_character = extra_characters[character]
        print(converted_character)
        for i in range(3):
            output_rows[row_index][i] += converted_character[i] + " "
        characters_in_row += 1

    if character == " " and characters_in_row >= characters_per_row:
        output_rows.append(['', '', ''])
        row_index += 1
        characters_in_row = 0

print("\nConverted to fictional alphabet:\n")

for row in output_rows:
    for i in range(3):
        print(row[i])
    print("")
