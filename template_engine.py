import re

VAR_TOKEN_START = "{{"
VAR_TOKEN_END = "}}" 
BLOCK_TOKEN_START = "{%"
BLOCK_TOKEN_END = "%}"

TOK_REGEX = re.compile(r"(%s.*?%s|%s.*?%s)" % (
    VAR_TOKEN_START,
    VAR_TOKEN_END,
    BLOCK_TOKEN_START,
    BLOCK_TOKEN_END
))