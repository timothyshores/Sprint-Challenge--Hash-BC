import sys
import random
import hashlib
import requests

from uuid import uuid4
from timeit import default_timer as timer

def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    - Note:  We are adding the hash of the last proof to a number/nonce for the new proof
    """

    previous_hash = hashlib.sha256(f'{last_proof}'.encode()).hexdigest()
    start = timer()

    print("Searching for next proof")
    proof = 0

    while valid_proof(last_proof, proof) is False:
        proof += random.randint(1, 10001)

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the proof?

    IE:  last_hash: ...AE9123456, new hash 123456888...
    """

    proof = str(proof).encode()
    last_hash = str(last_hash).encode()
    guess_hash = hashlib.sha256(proof).hexdigest()
    last_guess = hashlib.sha256(last_hash).hexdigest()
    return guess_hash[:6] == last_guess[-6:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        # set data to response JSON
        data = r.json()
        # print data
        print(data)
        # get new proof
        new_proof = proof_of_work(data.get('proof'))
        post_data = {"proof": new_proof, "id": id}
        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
