import keyword

def print_source_without_comments(filename):
    with open(filename, 'r') as file:
        in_multiline_comment = False
        in_singleline_comment = False
        prev_char = ""
        
        while True:
            char = file.read(1)
            if not char:
                break

            # handle multiline comments
            if in_multiline_comment:
                if char == '"' and prev_char == '"' and file.peek(1) == '"':
                    file.read(1)  # skip last closing quote
                    in_multiline_comment = False
                    prev_char = ""
                prev_char = char
                continue

            # handle single-line comments
            if in_singleline_comment:
                if char == '\n':
                    in_singleline_comment = False
                continue

            # detect start of multiline comment (either ''' or """)
            if char == '"' and prev_char == '"' and file.peek(1) == '"':
                file.read(1)  # Skip the third quote
                in_multiline_comment = True
                prev_char = ""
                continue

            # detect start of single-line comment #
            if char == '#':
                in_singleline_comment = True
                continue

            # print the character if not in a comment
            print(char, end='')
            prev_char = char

# specify filename to read
filename = '1.py'
print_source_without_comments(filename)

'''
a. Create a program in your favourite programming language that reads
the source code CHARACTER by CHARACTER and prints it out to the screen

(code above)
'''

'''
b. Using the same program that prints only the python keywords,
Provide a menu to let users choose whether to print per character or
print all the keywords
'''

def print_per_character():
    with open(__file__, 'r') as file:
        while (char := file.read(1)):
            print(char, end='')

def print_keywords():
    with open(__file__, 'r') as file:
        content = file.read()
        words = content.split()

        keywords_in_file = [word for word in words if word in keyword.kwlist]
        print("\nPython Keywords found in the file:")
        for kw in set(keywords_in_file):
            print(kw)

def menu():
    print("choose an option:")
    print("1. print source code character by character")
    print("2. print all Python keywords in the source code")

    choice = input("enter your choice (1 or 2): ")

    if choice == '1':
        print_per_character()
    elif choice == '2':
        print_keywords()
    else:
        print("invalid choice, please try again.")

if __name__ == "__main__":
    menu()
