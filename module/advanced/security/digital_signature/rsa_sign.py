import base64
import os
from module.util.logger_conf import logger
from cryptography.exceptions import InvalidKey, InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.serialization import Encoding, BestAvailableEncryption, \
    KeySerializationEncryption, PrivateFormat, PublicFormat, load_pem_private_key, load_pem_public_key

from module.conf import *

KEY_SIZE = 2048
PRI_PASSWD = "123456"
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
        priKey: RSAPrivateKey = rsa.generate_private_key(public_exponent=65537, key_size=KEY_SIZE)
        pubKey: RSAPublicKey = priKey.public_key()
        priKeyBytes = priKey.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=BestAvailableEncryption(password=bytes(PRI_PASSWD, encoding="utf-8"))
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


def sign(priKeyBytes: bytes, data: bytes) -> bytes:
    priKey: RSAPrivateKey = load_pem_private_key(data=priKeyBytes, password=bytes(PRI_PASSWD, encoding="utf-8"))
    signature: bytes = priKey.sign(data=data, padding=padding.PKCS1v15(), algorithm=hashes.SHA256())
    return signature


def sign_pre_hash(priKeyBytes: bytes, data: bytes) -> bytes:
    priKey: RSAPrivateKey = load_pem_private_key(data=priKeyBytes, password=bytes(PRI_PASSWD, encoding="utf-8"))
    hasher: hashes.Hash = hashes.Hash(algorithm=hashes.SHA256())
    hasher.update(data=data)
    hashResult: bytes = hasher.finalize()
    signature: bytes = priKey.sign(data=hashResult, padding=padding.PKCS1v15(), algorithm=utils.Prehashed(hashes.SHA256()))
    return signature


def verify(pubKeyBytes: bytes, signature: bytes, data: bytes) -> None:
    pubKey: RSAPublicKey = load_pem_public_key(data=pubKeyBytes)
    pubKey.verify(signature=signature, data=data, padding=padding.PKCS1v15(), algorithm=hashes.SHA256())
    pass


def verify_pre_hash(pubKeyBytes: bytes, signature: bytes, data: bytes) -> None:
    pubKey: RSAPublicKey = load_pem_public_key(data=pubKeyBytes)
    hasher: hashes.Hash = hashes.Hash(algorithm=hashes.SHA256())
    hasher.update(data=data)
    hashResult: bytes = hasher.finalize()
    pubKey.verify(signature=signature, data=hashResult, padding=padding.PKCS1v15(), algorithm=utils.Prehashed(hashes.SHA256()))
    pass


if __name__ == "__main__":
    data: bytes = b"this is data"
    priKey, pubKey = gen_key_pair()

    # logger.info(f"private key:{priKey}\npublic key:{pubKey}")
    signature: bytes = sign(priKeyBytes=priKey, data=data)
    signature2: bytes = sign_pre_hash(priKeyBytes=priKey, data=data)
    logger.info(f"signature: {base64.b64encode(s=signature).decode()} \nprehash: {base64.b64encode(s=signature2).decode()}")
    # data+=b"1"
    try:
        verify(pubKeyBytes=pubKey, signature=signature, data=data)
        verify_pre_hash(pubKeyBytes=pubKey, signature=signature, data=data)
        logger.info(f"verify: true")
        pass
    except (InvalidSignature) as ex:
        logger.info(f"verify: false")
        pass
    pass
