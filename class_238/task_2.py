import hashlib

text = "HI"
result = hashlib.sha3_256(text.encode())
print(result)