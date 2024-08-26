def custom_write(file_name, strings):
    strings_pos = {}
    file = open(file_name, "w", encoding="utf-8")

    line_number = 1
    for string in strings:
        bite_start = file.tell()
        file.write(string + "\n")
        strings_pos[(line_number, bite_start)] = string
        line_number += 1
    file.close()
    return strings_pos

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)