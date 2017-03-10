def int_to_negabinary(n):
    bits = 32
    return bin(n & int("1"*bits, 2))[2:]
