def string_to_hex(string):
    # Encode string to bytes
    string_bytes = string.encode('utf-8')

    key = string_bytes.hex()

    return key

def check_string_encrypt(key):
    if len(key) < 32:
      global pad
      global flag
      pad = 32 - len(key)
      flag = True

      for i in range(pad):
        key = "0" + key

    return key

def check_string_decrypt(key):
  if flag:
    return key[pad:]
  return

def hex_to_string(hex_str):
    # Convert hex string to bytes
    byte_str = bytes.fromhex(hex_str)

    # Decode bytes to string using UTF-8 encoding
    return byte_str.decode('utf-8')

text = "Hello, World!"

text_hex = check_string_encrypt(string_to_hex(text))

print(text_hex)

hex_text = hex_to_string(check_string_decrypt(text_hex))
print(hex_text)