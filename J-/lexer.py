import re

# Regular expression patterns for tokenizing the input text
PATTERNS = [
    (r'\bprint\b', 'PRINT'),
    (r'\bif\b', 'IF'),
    (r'\bthen\b', 'THEN'),
    (r'\belse\b', 'ELSE'),
    (r'\btrue\b', 'TRUE'),
    (r'\bfalse\b', 'FALSE'),
    (r'\d+', 'NUMBER'),
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),
    (r'[-+*/^=<>%!]', 'OPERATOR'),
    (r'[()\[\],.;]', 'PUNCTUATION'),
    (r'[ \t\r\n]+', 'WHITESPACE')
]

def tokenize(text):
    """Break a string of J- code into a list of tokens."""
    tokens = []
    while text:
        for pattern, token_type in PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(text)
            if match:
                token_text = match.group(0)
                tokens.append((token_type, token_text))
                text = text[len(token_text):]
                break
        else:
            raise ValueError(f"Unrecognized token: {text[:10]}")
    return tokens
