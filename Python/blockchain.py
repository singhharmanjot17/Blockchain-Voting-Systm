# blockchain.py
from web3 import Web3, HTTPProvider

class Blockchain:
    def __init__(self):
        self.w3 = Web3(HTTPProvider('HTTP://127.0.0.1:7545'))  # Connect to a local Ethereum node
        self.contract_address = "0xCB431bE74EA6934F2A0aA3Db5cCCc73a2FBa6193"
        self.contract_abi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "voter",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "string",
        "name": "candidate",
        "type": "string"
      }
    ],
    "name": "Voted",
    "type": "event",
    "signature": "0xcb6783276e8a4347387036bbfea000268f0a4b1f8c46ac79980609f2af8d2acd"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "hasVoted",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True,
    "signature": "0x09eef43e"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True,
    "signature": "0x8da5cb5b"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "name": "votesCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True,
    "signature": "0xea445794"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "candidate",
        "type": "string"
      }
    ],
    "name": "vote",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function",
    "signature": "0xfc36e15b"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "candidate",
        "type": "string"
      }
    ],
    "name": "getVotesCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True,
    "signature": "0x13f12ec7"
  },
  {
    "inputs": [],
    "name": "isOwner",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function",
    "constant": True,
    "signature": "0x8f32d59b"
  }
] 
        self.contract_instance = self.w3.eth.contract(
        address=self.contract_address,
        abi=self.contract_abi
    )
    def deploy_contract(self):
       
        pass

    def vote(self, candidate):
       
        tx_hash = self.contract_instance.functions.vote( candidate).transact({'from': '0x1f286A615609d82BDddE859FF1f12DB6d8AEE242'})
        return tx_hash

    def get_Votes(self):
       candidate = "Candidate "
       votes_count = self.contract_instance.functions.getVotesCount(candidate).call()
       print(f"Votes count for {candidate}: {votes_count}")

    def get_results(self):
        results = self.contract_instance.functions.getVotesCount("Candidate Y").call()
        return results
