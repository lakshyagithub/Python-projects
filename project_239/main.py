import hashlib
import json
from time import time

def block(proof, previous_hash=None):
    transaction = {'sender': 'Satoshi', 'receiver': 'Mike', 'amount': 5}
    data = {'block_height': 123, 'timestamp': time(), 'transaction': transaction, 'Block Reward': 10, 'Uncles Reward': 2, 'Difficulty': 12345, 'Total Difficulty': 54321, 'Size': 256, 'Gas Used': 20000, 'Gas Limit': 30000}
    data['proof'] = proof
    data['previous hash'] = previous_hash
    sha = hashlib.sha512()
    json_data = json.dumps(data, sort_keys=True)
    encoded_data = json_data.encode()
    sha.update(encoded_data)
    block_hash = sha.hexdigest()
    print("Block Hash:", block_hash)
    return block_hash

proof = 12345
previous_hash = "some_previous_hash"
block_hash = block(proof, previous_hash)