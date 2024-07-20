from nada_dsl import *

def nada_main():
    # 1. Parties initialization
    contributor0 = Party(name="Contributor0")
    contributor1 = Party(name="Contributor1")
    contributor2 = Party(name="Contributor2")
    outparty = Party(name="OutParty")

    # 2. Inputs initialization
    ## Contributions from contributor 0
    c0 = SecretUnsignedInteger(Input(name="c0", party=contributor0))
    ## Contributions from contributor 1
    c1 = SecretUnsignedInteger(Input(name="c1", party=contributor1))
    ## Contributions from contributor 2
    c2 = SecretUnsignedInteger(Input(name="c2", party=contributor2))

    # 3. Computation
    ## Add all contributions
    total_contribution = c0 + c1 + c2

    # 4. Output
    total_contribution_output = Output(total_contribution, "total_contribution", outparty)

    return [total_contribution_output]
