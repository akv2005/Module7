

file_name = 'txt1.txt'
file = open(file_name, mode='r')
file_cont = file.read()
file.close()
print(file_cont)
