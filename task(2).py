def no_numbers():
    file_path = 'C:/Users/Александра/Desktop/homework6/file2'
    outfile_path = 'C:/Users/Александра/Desktop/homework6/output_file2'
    open_file = open(file_path)
    content = open_file.read()

    new_content = ''
    for letter in content:
        try:
            int(letter)
        except:
            new_content += letter

    out_file = open(outfile_path, 'w')
    out_file.write(new_content)
    out_file.close()
    open_file.close()


no_numbers()
