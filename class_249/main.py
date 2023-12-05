import hashlib
PB_current_hash = "573de6af99199bdc7ae9534891d512afbc2b1473f2f6a5784e0c078d67a60bf9"

str_1 = "Someone gave 1 eth to someone"

result_1 = hashlib.sha256(str_1.encode())
CB_previous_hash = result_1.hexdigest()

if PB_current_hash == CB_previous_hash:
	print("Hash matched!")
else:
	print("Hash unmatched!")