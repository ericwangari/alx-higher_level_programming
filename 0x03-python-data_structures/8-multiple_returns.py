#!/usr/bin/python3
# 8-mutiple_returns.py

def mutiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
