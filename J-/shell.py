import sys
from lexer import tokenize
from compiler import compile_expression, compile_statement

def run_command(tokens):
    """Execute a J- command from a list of tokens."""
    if tokens:
        command = tokens[0]
        if command == 'PRINT':
            print(tokens[1])
        else:
            print(f"Unrecognized command: {command}")

def main():
    """Main function for the J- shell."""
    while True:
        try:
            line = input('Code> ')
        except EOFError:
            break
        tokens = tokenize(line)
        run_command(tokens)

if __name__ == '__main__':
    main()

