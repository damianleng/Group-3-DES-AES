import DES_utils

IP = DES_utils.IP
PC_1 = DES_utils.PC_1
PC_2 = DES_utils.PC_2
EP = DES_utils.EP
PF = DES_utils.PF
shift_table = DES_utils.shift_table
s_box = DES_utils.s_box
FP = DES_utils.FP

def encrypt(bits, key):
    # initial permutate the bits
    bits = permute(bits, IP, 64)

    # split the bits in halves
    left = bits[0:32]
    right = bits[32:64]

    # PC-1 permutate the bits
    key = permute(key, PC_1, 56)

    for i in range(0, 16):
        # expand permuation 
        right_EP = permute(right, EP, 48)

        # XOR round keys and expanded right key
        xor_key = xor(right_EP, key_schedule(key)[i])

        # use S-Boxes
        sbox_s = ""
        for j in range(0, 8):
            row = binary_to_decimal(int(xor_key[j*6] + xor_key[j*6+5]))
            column = binary_to_decimal(int(xor_key[j*6+1] + xor_key[j*6+2] + xor_key[j*6+3] + xor_key[j*6+4])) 
            value = s_box[j][row][column]
            sbox_s = sbox_s + decimal_to_binary(value)
        
        # permute within the f function
        sbox_s = permute(sbox_s, PF, 32)

        # xor the left and sbox_s
        result = xor(left, sbox_s)
        left = result

        if i != 15:
            left, right = right, left
        
    encrypted = left + right
    encrypted_text = permute(encrypted, FP, 64)
    return encrypted_text


def key_schedule(key):
    # split the bits in halve
    left = key[0:28]
    right = key[28:56]
    round_key = []

    for i in range(0, 16):
        # shift the bits by n shifts by checking from the shift table
        left_key = ROL(left, shift_table[i])
        right_key = ROL(right, shift_table[i])
    
        # combine the left and right shifted keys
        combined_keys = left_key + right_key	

        #PC-2 permutate the bits
        result = permute(combined_keys, PC_2, 48)

        # create a array to store key for each rounds
        round_key.append(result)
    
    return round_key

def permute(bits, type, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + bits[type[i] - 1]
    return permutation

def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

def ROL(key, n):
    result = ""
    for i in range(n):
        for j in range(1, len(key)):
            result = result + key[j]
        result = result + key[0]
        key = result 
        result = ""
    return key

def binary_to_decimal(binary): 
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def decimal_to_binary(num):
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


bits = "1001010010010010010001000100010001000100010001000100010001001010"
key = "1111111111111111111111111111111111111111111111111111111111111111"


print(len(encrypt(bits, key)))