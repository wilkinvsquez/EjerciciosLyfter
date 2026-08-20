def read_file(file_name):
    with open(file_name, 'r')as file:
        lines = file.readlines()
    return lines


def create_file_uppercase(file_name, lines):
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line.upper())

def main():
    file_lines = read_file("text3.txt")
    create_file_uppercase("text3_uppercase.txt", file_lines)

main()