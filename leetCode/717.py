def q717(bits):
    if len(bits) == 1:
        return True
    if bits[len(bits) - 2] == 1 and bits[len(bits) - 1] == 0:
        return False
    if bits[len(bits) - 2] == 1 and bits[len(bits) - 1] == 1:
        return False
    return True
print(q717([1, 1, 1, 0,0,0]))