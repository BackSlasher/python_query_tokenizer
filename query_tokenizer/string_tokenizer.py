#!/usr/bin/env python3
from typing import NamedTuple, Tuple, Union, Optional
from io import StringIO

QUOTES = {'"', "'"}
BRACKETS = {
    "(": ")",
}


class Token:
    pass


class StringToken(NamedTuple):
    s: str


class CompoundToken(NamedTuple):
    subTokens: Tuple[Token, ...]


Token = Union[StringToken, CompoundToken]


def read_compound_token(stream, bracket: Optional[str]) -> CompoundToken:
    tokens = []
    current_token = ""
    current_quote = None
    while c := stream.read(1):
        if current_quote and c == current_quote:
            current_token += c
            current_quote = None
        elif c in QUOTES:
            current_token += c
            current_quote = c
            pass
        elif c == " ":
            if current_quote:
                current_token += c
            elif current_token:
                tokens.append(StringToken(current_token))
                current_token = ""
        elif bracket and c == BRACKETS[bracket]:
            # Return
            break
        elif c in BRACKETS and not current_token:
            tokens.append(read_compound_token(stream, bracket=c))
        else:
            current_token += c
    if current_token:
        tokens.append(StringToken(current_token))
    return CompoundToken(tuple(tokens))


def tokenize(string) -> CompoundToken:
    stream = StringIO(string)
    return read_compound_token(stream, bracket=None)
