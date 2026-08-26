def read_file(file_path):
    text_in_line= []
    with open(file_path, 'r') as file:
        lines_list = file.readlines()
        for line in lines_list:
            text_in_line.append(line.strip())
    return text_in_line

def create_file(file_path, separate_list):
    with open(file_path, 'w', encoding='utf-8') as file :
        file.write(' '.join(separate_list))


input_file = 'text1.txt'
output_file = 'TextInLine.txt'
separate_list = read_file(input_file)
create_file(output_file, separate_list)