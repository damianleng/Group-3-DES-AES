s_box = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]


def byte_substitution_helper(byte1, byte2):
    byte_value = int(byte1 + byte2, 16)
    row = byte_value // 16
    col = byte_value % 16
    result = s_box[row][col]
    return result

def byte_substitution(byte):
    result = ""
    for i in range(0, len(byte), 2):
        byte1 = byte[i]
        byte2 = byte[i+1]
        a = byte_substitution_helper(byte1, byte2)
        result += a
    return result

def string_to_matrix(input_string):
    # convert a string of bytes to a matrix as an array
    matrix = []
    for i in range(0, len(input_string), 8):
        row = []
        for j in range(4):
            row.append(input_string[i+2*j:i + 2*j + 2])
        matrix.append(row)
    return matrix # return the transposed version of the matrix

def transpose_matrix(matrix):
    return [list(x) for x in zip(*matrix)]

def matrix_to_string(matrix):
    output_string = ''
    for row in matrix:
        for char in row:
            output_string += char
    return output_string

def shift_rows(matrix):
    matrix = transpose_matrix(string_to_matrix(matrix))
    for i in range(1, 4):
        matrix[i] = matrix[i][i:] + matrix[i][:i]
    return matrix_to_string(transpose_matrix(matrix))

def bin_to_hex(binary):
    hex = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'
        }
    result = ""
    for i in range(0, len(binary), 4):
        n = ""
        n = n + binary[i]
        n = n + binary[i+1]
        n = n + binary[i+2]
        n = n + binary[i+3]
        result = result + hex[n]
    return result

def hex_to_bin(hex):
    binary = {
            '0': "0000",
            '1': "0001",
            '2': "0010",
            '3': "0011",
            '4': "0100",
            '5': "0101",
            '6': "0110",
            '7': "0111",
            '8': "1000",
            '9': "1001",
            'A': "1010",
            'B': "1011",
            'C': "1100",
            'D': "1101",
            'E': "1110",
            'F': "1111"         
         }
    result = ""
    for i in hex:
        result += binary[i.upper()]
    return result

def add(A, B):
    # make sure A, B have the same length
    while len(A) > len(B):
        B = '0' + B
    while len(B) > len(A):
        A = '0' + A
    C = ''
    for i in range(len(A)):
        if A[i] == B[i]:
            C += '0'
        else:
            C+= '1'
    # Get rid of zeros in front of C
    i = 0
    while i<len(C) and C[i] == '0':
        i += 1
    if i == len(C):
        C = '0' # all 0s
    else:
        C = C[i:]
    return C

# multiplication function
# first do multiplication without mod
def multiply(A, B):
    C = '0' # result
    for i in range(len(B)-1, -1, -1):
        if B[i] == '1':
            C = add(C, A)
        A = A + '0'
    return C

def mod(A, P):
    # 101110 substr -> 10111 then add 10111 + P, then addpend it to the leftover substr
    # use substr, then add it, and then append it to the leftover substr
    result = A
    while len(result) >= len(P):
        left = add(result[:len(P)], P)
        right = result[len(P):]
        result = left + right
    return result

def matrix_multiplication(column):
    one = "00000001"
    two = "00000010"
    three = "00000011"
    GF = "100011011"
    MATRIX = [[two, three, one, one], [one, two, three, one], [one, one, two, three], [three, one, one, two]]

    result = []
    for i in range(4):
        total = "00000000"
        for j in range(4):
            multiplied = mod(multiply(MATRIX[i][j], column[j]), GF)
            total = add(total, multiplied)
        result.append(total)
    return result

def mix_columns(hex):
    a = string_to_matrix(hex)
    binary = []
    for i in a:
        n = []
        for j in i:
            n.append(hex_to_bin(j))
        binary.append(n)   

    result = []
    for k in binary:
        result.append(matrix_multiplication(k))
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            while len(result[i][j]) < 8:
                result[i][j] = "0" + result[i][j]
                
    return bin_to_hex(matrix_to_string(result)) 

# xor two 128-bits in hexadecimal
def xor(a, b):
    a = hex_to_bin(a)
    b = hex_to_bin(b)

    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    
    return bin_to_hex(result)


hex_string = '00112233445566778899aabbccddeeff'
substituted_string = byte_substitution(hex_string) # substitute the string
shifted_rows = shift_rows(substituted_string) # shift the rows and return as string
mixed_columns = mix_columns(shifted_rows)

print("Original String: " + hex_string)
print("Substituted String: " + substituted_string)
print("Shifted Rows: " + shifted_rows)
print("Mixed Columns: " + mixed_columns)
