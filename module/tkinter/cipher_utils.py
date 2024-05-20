from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, BestAvailableEncryption, NoEncryption, \
    KeySerializationEncryption, PrivateFormat, PublicFormat, load_der_private_key, load_der_public_key
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers import Cipher, CipherContext, algorithms, modes
from cryptography.hazmat.primitives.hashes import Hash, HashAlgorithm, SHA256
from cryptography.hazmat.primitives.padding import PKCS7

def generate_keypair() -> tuple:
    """
    return: private_key, public_key
    """
    private_key = ec.generate_private_key(curve=ec.SECP256R1)
    public_key = private_key.public_key()
    return private_key.private_bytes(encoding=Encoding.DER, format=PrivateFormat.PKCS8, encryption_algorithm=NoEncryption()), \
        public_key.public_bytes(encoding=Encoding.DER, format=PublicFormat.SubjectPublicKeyInfo)

def encrypt_password(my_priv_key_b: bytes, other_pub_key_b: bytes, plain_passwd_b: bytes, session_id_b: bytes, random_no_b:bytes) -> bytes:
    result = bytearray()
    my_priv_key = load_der_private_key(data=my_priv_key_b, password=None)
    other_pub_key = load_der_public_key(data=other_pub_key_b)
    shared_secret:bytes = my_priv_key.exchange(algorithm=ec.ECDH(), peer_public_key=other_pub_key)
    key_material_b = bytes().join((session_id_b, random_no_b, shared_secret,))
    # create key material
    hash_engine = Hash(algorithm=SHA256())
    hash_engine.update(data = key_material_b)
    key_material_b = hash_engine.finalize()
    
    # encrypt
    padder = PKCS7(128).padder()
    plain_passwd_b = padder.update(data=plain_passwd_b).join((padder.finalize(),))
    cipher= Cipher(algorithm=algorithms.AES(key_material_b[:len(key_material_b)//2]), \
                            mode=modes.CBC(initialization_vector=key_material_b[len(key_material_b)//2:]))
    encryptor= cipher.encryptor()
    result.extend(encryptor.update(data=plain_passwd_b))
    result.extend(encryptor.finalize())
    return bytes(result)

def decrypt_password(my_priv_key: bytes, other_pub_key: bytes, enc_passwd: bytes, session_id: bytes, random_no:bytes) -> bytes:
    result = None
    return result