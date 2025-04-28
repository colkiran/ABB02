
def bank_flow(fnc):
    print("-" * 60)
    print("Logging in......")
    fnc()
    print("Logging out......")
    print("-" * 60)

def deposit():
    print("Debitted.......")

def withdraw():
    print("Credited.......")

def transfer():
    print("Transfered......")


bank_flow(deposit)
bank_flow(withdraw)
bank_flow(transfer)
