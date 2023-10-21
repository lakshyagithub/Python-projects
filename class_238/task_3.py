import hashlib

text1 = "HI"
result1 = hashlib.sha3_256(text1.encode())
print(result1)

text2 = "Bye"
result2 = hashlib.sha3_256(text2.encode())
print(result2)

text3 = "Ok"
result3 = hashlib.sha3_256(text3.encode())
print(result3)

text4 = "minecraft"
result4 = hashlib.sha3_256(text4.encode())
print(result4)