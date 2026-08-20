def read_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    return content

def count_words(file_content):
    return len(file_content.split())

def main():
    content = read_file("text2.txt")
    count = count_words(content)
    print(f"Este archivo contiene {count} palabras")

main()