from flask import Flask, jsonify, request
from uuid import uuid4
from classes.Blockchain import Blockchain

app         = Flask(__name__)
blockchain  = Blockchain()
node_identifier = str(uuid4()).replace('-', '') # Generate a globally unique address for this node

# #################################################################### #
#
#                              GET /mine
#
# #################################################################### #
@app.route('/mine', methods=['GET'])
def mine():
  
  last_block    = blockchain.last_block
  last_proof    = last_block['proof']
  proof         = blockchain.proof_of_work(last_proof)

  blockchain.new_transaction(
    sender="0",
    reciever=node_identifier,
    amount=1,
  )
  
  previous_hash = blockchain.hash(last_block)
  block         = blockchain.new_block(proof, previous_hash)

  response = {
    'message': "New Block Forged",
    'index': block['index'],
    'transactions': block['transactions'],
    'proof': block['proof'],
    'previous_hash': block['previous_hash'],
  }

  return jsonify(response), 200
  
# #################################################################### #
#
#                        POST /transactions/new
#
# #################################################################### #

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
  values      = request.get_json()
  # required    = ['sender', 'reciever', 'amount']
  required    = ['sender', 'amount']
  
  if not all(field in values for field in required):
    return 'Missing values', 400
  
  index       = blockchain.new_transaction(values['sender'], node_identifier, values['amount'])
  response    = {'message': f'transaction will be added to Block {index}'}

  return jsonify(response), 201

# #################################################################### #
#
#                        GET /chain
#
# #################################################################### #
@app.route('/chain', methods=['GET'])
def full_chain():
  response = {
    'chain': blockchain.chain,
    'length': len(blockchain.chain),
  }
  return jsonify(response), 200


# #################################################################### #
#
#                        POST /nodes/register
#
# #################################################################### #

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
  values      = request.get_json()
  nodes       = values['nodes']
  
  if nodes is None:
    return 'Error: Please supply with a valid list of nodes', 400
  
  for node in nodes:
    blockchain.register_node(node)

  response = {
    'message': 'New nodes have been added',
    'total_nodes': list(blockchain.nodes)
  }

  return jsonify(response), 201


# #################################################################### #
#
#                        GET /nodes/resolver
#
# #################################################################### #
@app.route('/nodes/resolve', methods=['GET'])
def consenious():
  replaced    = blockchain.resolve_conflict()

  if replaced: 
    response = {
      'message': 'Our chain has been replaced',
      'new_chain': blockchain.chain
    }

  else:
    response = {
      'message': 'Our chain is authoritative',
      'chain': blockchain.chain
    }

  return jsonify(response), 200


# #################################################################### #
#
#                               RUN PROGRAM
#
# #################################################################### #
if __name__ == '__main__':
  from argparse import ArgumentParser

  parser = ArgumentParser()
  parser.add_argument('-p', '--port', default=5000, type=int, help='port to run the program.')
  args = parser.parse_args()
  port = args.port

  app.run(host='0.0.0.0', port=port)