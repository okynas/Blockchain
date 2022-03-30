# BLOCKCHAIN

<!-- link -->
[GITHUB](https://www.github.com/okynas)

## requirements:
- flask
- requests
- argparse 


## About crypto:

### What does a "Block" look like:

This is a block: 

```
block = {
  'index': 1,
  'timestamp': 1506057125.900785,
  'transactions': [
    {
      'sender': "8527147fe1f5426f9dd545de4b27ee00",
      'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
      'amount': 5,
    }
  ],
  'proof': 324984774000,
  'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```

Each of them have an index, timestamp, list of transactions, proof and hash.

That means that each new block contains within itself, hash of the previous block.
THIS is what gives blockchain immutability, can't be changed.

That means, if a block is corrupted, then all blocks that follows will be corrupt.

### How does the proof work:

Proof of Work (PoW) algorithm, is the way that new block is being created, or mined.
The meaning by PoW is to discover a number, that solves a problem.

It should be easily verified, but not so easy to find.

In Bitcoin the algorithm is called Hashcash.

### Our Algorithm:

Find a number "p" that when hashed with the previous block’s solution a hash with 4 leading '0s' is produced.

### Problem of Consensus
Problem of Consensus is a problem that occur when a blockchain is decentralized, as it should, and should point to the same chain. 
The problem occur when we have more than one node.

### URLS:

- GET /mine
- POST /transactions/new
- GET /chain
- POST /nodes/register
- GET /nodes/resolve

### Function descriptions

new_block()
new_transaction()
register_node()
- add a new node to the network / list of nodes

valid_chain()
- check that the hash of all block is correct
- check that the PoW works for all blocks

resolve_conflict()

proof_of_work()

last_block() - method

hash() - static

verify_proof() - static

### TO DO
  [ ] Transaction Validation
  [ ] Productionize 
