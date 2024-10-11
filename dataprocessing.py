# Matthew Sanchez - CPSC 323

import os

# read data from an input file
def read_file(filename):
    # Open the file and return content
    with open(filename, 'r') as file:
        return file.readlines()

# Remove whitespace
def scrub_lines(lines):
    scrubbed_lines = []
    
    for line in lines:
        # remove comments if there are any
        comment_index = line.find('#')
        if comment_index != -1:
            line = line[:comment_index]
        # elimanate more white space
        line = line.strip()
        # check empty lines
        if len(line) > 0:
            scrubbed_lines.append(line)
    
    return scrubbed_lines

# tokenize the code
def tokenize(lines):
    keywords = ['False', 'await', 'else', 'import', 'pass', 'None', 'break', 'except', 'in', 'raise',
        'True', 'class', 'finally', 'is', 'return', 'and', 'continue', 'for', 'lambda', 'try',
        'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del', 'global', 'not', 'with', 'async',
        'elif', 'if', 'or', 'yield']
    operators = ['=', '+', '-', '*', '%', '<', '<=', '>', '>=', '==', '!=', 'AND', 'OR', 'NOT', '&',
        '|', '<<', '>>', '^', '+=', '-=', '*=', '%=']
    delimiters = ['(', ')', ':', ',', '[', ']', '{', '}', ';', '@']

    tokens = {
        "Keywords": [],
        "Identifiers": [],
        "Operators": [],
        "Delimiters": [],
        "Literals": []
    }

    for line in lines:
        current_token = ""  # to collect characters for identifiers or literals
        
        for char in line:
            if char.isalnum() or char == '_':  # If it's part of an identifier or literal
                current_token += char
            else:
                # categorize the tokens
                if current_token:
                    if current_token in keywords:
                        tokens["Keywords"].append(current_token)
                    elif current_token.isdigit():
                        tokens["Literals"].append(current_token)
                    else:
                        tokens["Identifiers"].append(current_token)
                    current_token = ""

                # check if the character is an operator or delimiter
                if char in operators:
                    tokens["Operators"].append(char)
                elif char in delimiters:
                    tokens["Delimiters"].append(char)
        
        # if there's any token left at the end of the line
        if current_token:
            if current_token in keywords:
                tokens["Keywords"].append(current_token)
            elif current_token.isdigit():
                tokens["Literals"].append(current_token)
            else:
                tokens["Identifiers"].append(current_token)

    return tokens

# print the clean code
def print_clean_code(lines):
    print("Cleaned Code:")
    for line in lines:
        print(line)
    print()

# print the tokenized code
def print_tokens(tokens):
    print("Tokenized Code:")
    for category, token_list in tokens.items():
        print(f"{category}: {', '.join(token_list)}")
    print()

# main func
def main():
    filename = input('What is the filename?\n')
    
    lines = read_file(filename)
    clean_lines = scrub_lines(lines)
    tokens = tokenize(clean_lines)
    print_clean_code(clean_lines)
    print_tokens(tokens)

# Run the program
if __name__ == "__main__":
    main()
