import hashlib
import json
from time import time

class lego():
	def __init__(self):
		self.chain = []
		self.new_transactions = []
		self.count = 0
		self.new_lego_brick(previous_hash="No previous hash. If you know it then let me know about it")

	def new_lego_brick(self, previous_hash=None):
		lego_brick = {
			"Block no.": self.count,
			"timestamps": time(),
			"transactions": self.new_transactions or "It seems that you dont have PhonePe.",
			"gasfee": 0.1,
			"previous_hash": previous_hash
		}
		self.count = self.count + 1
		self.chain.append(lego_brick)

		string_object = json.dumps(lego_brick)
		brick_string = string_object.encode()
		raw_hash = hashlib.sha256(brick_string)
		hex_hash = raw_hash.hexdigest()
		self.chain.append(("Current hash:", hex_hash))

		return lego_brick

blockchain = lego()

print(blockchain.chain)