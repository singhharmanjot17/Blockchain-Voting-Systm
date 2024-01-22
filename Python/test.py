
from blockchain import Blockchain

blockchain = Blockchain()


voter_id = "126"
candidate = "Candidate Y"
tx_hash = blockchain.vote(candidate)
print(f"Transaction Hash: {tx_hash}")


results = blockchain.get_results()
print(f"Voting Results: {results}")
