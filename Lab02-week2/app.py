from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# CAESAR CIPHER
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = int(data.get('key', 0))
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = int(data.get('key', 0))
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

# VIGENERE CIPHER
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = data.get('key', '')
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = data.get('key', '')
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

# RAIL FENCE CIPHER
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = int(data.get('key', 0))
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = int(data.get('key', 0))
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

# PLAYFAIR CIPHER
playfair_cipher = PlayfairCipher()

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = data.get('key', '')
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = data.get('key', '')
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

# TRANSPOSITION CIPHER
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    try:
        data = request.json
        plain_text = data.get('plain_text', '')
        key = int(data.get('key', 0))
        encrypted_text = transposition_cipher.encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    try:
        data = request.json
        cipher_text = data.get('cipher_text', '')
        key = int(data.get('key', 0))
        decrypted_text = transposition_cipher.decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
