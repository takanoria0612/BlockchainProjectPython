from flask import Flask, jsonify, request
from flask_cors import CORS

from blockchain import BlockChain  # import your blockchain class

app = Flask(__name__)
CORS(app)  # this is to handle CORS

block_chain = BlockChain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = block_chain.chain
    return jsonify({"length": len(chain_data), "chain": chain_data}), 200

@app.route('/block', methods=['POST'])
def create_block():
    nonce = request.form['nonce']
    previous_hash = request.form['previous_hash']
    block_chain.create_block(nonce, previous_hash)
    return jsonify({"message": "Block created"}), 201

if __name__ == "__main__":
    app.run(port=5000)
# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
