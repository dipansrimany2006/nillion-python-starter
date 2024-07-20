from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    # Define inputs from different parties
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))
    
    # Perform operations
    addition_result = a + b
    subtraction_result = a - c
    multiplication_result = b * c
    
    # Return results to a party
    return [
        Output(addition_result, "addition_output", party4),
        Output(subtraction_result, "subtraction_output", party4),
        Output(multiplication_result, "multiplication_output", party4)
    ]
