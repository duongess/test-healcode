# test_error.py
import os
import sys

def complex_function(a, b):
    """
    (ENGLISH) This is a docstring to test extraction.
    """
    c = a + b
    print(f"Result: {c}")
    

    old_name = "test"
    
    print(old_name)
    return c
    
global_var = 123
if __name__ == "__main__":
    complex_function(global_var, 1)