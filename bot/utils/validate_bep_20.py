

def validate_bep_20(address: str):
    if address.startswith("0x"):
        return True
    return False