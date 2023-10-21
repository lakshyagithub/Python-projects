import hashlib
from time import time
import json

chain = []

def lego(proof, previous_hash=None):
	transaction = {
		"sender":"Lakshya 1",
		"reciver":"Lakshya 2",
		"amount":"10 ETH"
	}
	data = {
		"index":1,
		"timestamps":time(),
		"transactions":transaction,
		"cng":0.1,
		"proof":proof,
		"previous_hash":previous_hash
	}
	chain.append(lego)
	print("Block information:", data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of block:", hex_hash)

lego(previous_hash="What are you taking about? There is no previous hash in the first block.", proof=000)
