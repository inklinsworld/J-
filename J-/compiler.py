import sys
from lexer import tokenize

def compile_expression(tokens):
    """Compile a J- expression into machine code."""
    if tokens[0] == 'NUMBER':
        return ['LOAD_CONST', int(tokens[1])]
    elif tokens[0] == 'IDENTIFIER':
        return ['LOAD_VAR', tokens[1]]
    elif tokens[0] == 'OPERATOR':
        operator = tokens[1]
        if operator == '+':
            return ['ADD']
        elif operator == '-':
            return ['SUB']
        elif operator == '*':
            return ['MUL']
        elif operator == '/':
            return ['DIV']
        elif operator == '^':
            return ['POW']
        elif operator == '=':
            return ['STORE_VAR', tokens[2]]
        else:
            raise ValueError(f"Unrecognized operator: {operator}")
    else:
        raise ValueError(f"Unrecognized token: {tokens[0]}")

def compile_statement(tokens):
    """Compile a J- statement into machine code."""
    if tokens[0] == 'PRINT':
        return compile_expression(tokens[1:]) + ['PRINT']
    el
