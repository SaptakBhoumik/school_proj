'''
10. WAP to read a file and display the contents of the file.
'''
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"
name=input("Enter the file name: ")
print(read_file(name))