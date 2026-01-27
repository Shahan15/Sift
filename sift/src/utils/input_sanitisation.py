import argparse

def verify_input(input):
    if len(input) != 11 and not input.lower() in ['q','exit']:
        print('Invalid input please provide a valid input')
        return False
    
    return True
    