import os
import base64
from module.util.logger_conf import logger
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers import Cipher, CipherContext, algorithms, modes
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey, generate_private_key
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15, OAEP
from cryptography.hazmat.primitives.serialization import Encoding, BestAvailableEncryption, \
    PrivateFormat, PublicFormat, load_pem_private_key, load_pem_public_key

from module.conf import *

KEY_SIZE = 2048
PRI_PASSWD = b"123456"
PRI_FILE = PROJECT_DIR + "/data/keys/rsa_pri.pem"
PUB_FILE = PROJECT_DIR + "/data/keys/rsa_pub.pem"


def gen_key_pair() -> tuple[bytes, bytes]:
    priKeyBytes: bytes = None
    pubKeyBytes: bytes = None
    if os.path.isfile(PRI_FILE) and os.path.isfile(PUB_FILE):
        with open(file=PRI_FILE, mode="rb") as priFile, open(file=PUB_FILE, mode="rb") as pubFile:
            priKeyBytes = priFile.read(os.path.getsize(filename=PRI_FILE))
            pubKeyBytes = pubFile.read(os.path.getsize(filename=PUB_FILE))
            pass
        pass
    else:
        priKey: RSAPrivateKey = generate_private_key(public_exponent=65537, key_size=KEY_SIZE)
        pubKey: RSAPublicKey = priKey.public_key()
        priKeyBytes = priKey.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=BestAvailableEncryption(password=PRI_PASSWD)
        )
        pubKeyBytes = pubKey.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo,
        )
        with open(file=PRI_FILE, mode="wb") as priFile, open(file=PUB_FILE, mode="wb") as pubFile:
            priFile.write(priKeyBytes)
            pubFile.write(pubKeyBytes)
            pass
        pass
    return priKeyBytes, pubKeyBytes

def encrypt(key: bytes, data: bytes) -> bytes:
    pub_key: RSAPublicKey = load_pem_public_key(data=key)
    result: bytes = pub_key.encrypt(plaintext=data, padding=PKCS1v15())
    return result

def decrypt(key: bytes, data: bytes) -> bytes:
    pri_key: RSAPrivateKey = load_pem_private_key(data=key, password=PRI_PASSWD)
    result: bytes = pri_key.decrypt(ciphertext=data, padding=PKCS1v15())
    return result


if __name__ == "__main__":
    plain_data: bytes = b"test try again"
    logger.info(f"plain data:{base64.b64encode(s=plain_data).decode('utf-8')}")
    pri_key, pub_key = gen_key_pair()

    crypted_data = encrypt(key=pub_key, data=plain_data)
    logger.info(f"encrypted base64:{base64.b64encode(s=crypted_data).decode('utf-8')}")
    try:
        replain_data: bytes = decrypt(key=pri_key, data=crypted_data)
        logger.info(f"decrypted base64:{base64.b64encode(s=replain_data).decode('utf-8')}")
        pass
    except (InvalidTag, TypeError) as ex:
        logger.error("", ex)
        pass
    pass

