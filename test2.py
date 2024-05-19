
file_name = 'text2.txt'

with open(file_name, mode='r', encoding='utf8') as file:
    print(file_name)
    file_cont = file.read()
    print(file_cont)