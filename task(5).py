def my_file():
    f_path = 'C:/Users/Александра/Desktop/homework6/file2'
    out_path = 'C:/Users/Александра/Desktop/homework6/shifr_file'
    open_file = open(f_path)
    file_read = open_file.read()
    my_date = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    key = int(input("Please, enter your key(number from 1-25): "))
    encrypted = ""
    for letter in file_read:
        position = my_date.find(letter)
        new_position = position + key
        if letter in my_date:
            encrypted = encrypted + my_date[new_position]
        else:
            encrypted = encrypted + letter
    print("Your cipher is: ", encrypted)

    out_file = open(out_path, 'w')
    out_file.write(encrypted)
    out_file.close()
    open_file.close()


my_file()
