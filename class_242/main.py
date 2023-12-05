import hashlib
import json
from time import time


class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous_hash="No previous Hash. Since this is the first block.")

    def new_block(self, previous_hash=None):
        block = {
            'Block No': self.count,
            'timestamp': time(),
            'transactions': self.new_transactions or 'No Transactions First Genesis Block',
            'gasfee': 0.1,
            'previous_hash': previous_hash
        }
        self.new_transactions = []
        self.count = self.count + 1
        self.chain.append(block)

        return block

    def last_block(self):
    	return self.chain[-1]
    def transaction(self, sender, recipient, amount):
    	sender_encoder = hashlib.sha256(sender.encode())
    	sender_hash = sender_encoder.hexdigest()
    	recipient_encoder = hashlib.sha256(recipient.encode())
    	recipient_hash = recipient_encoder.hexdigest()

    	transaction_data = {
    		'sender': sender_hash,
    		'recipient': recipient_hash,
    		'amount': amount
    	}
    	self.new_transactions.append(transaction_data)
    	return self.last_block
    def hash(self, block):
        string_object = json.dumps(block)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        self.chain.append(("Current Hash: ", hex_hash))
        return hex_hash

blockchain = Block()
transaction1 = blockchain.transaction("Sam", "Micro", "5 eth")
transaction2 = blockchain.transaction("Micro", "Sam", "100 eth")
transaction3 = blockchain.transaction("Robets", "Ruskin Bond", "10 eth")
transaction4 = blockchain.transaction("Lakshya1", "Lakshya 2", "1 eth")
transaction5 = blockchain.transaction("Lakshya", "Yug", "50 eth")
blockchain.new_block()

print(blockchain.chain)
