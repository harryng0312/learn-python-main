import os
import base64
from module.util.logger_conf import logger
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers import Cipher, CipherContext, algorithms, modes
from module.conf import *

SECRET_FILE = PROJECT_DIR + "/data/keys/secret.key"

def gen_secret_key(keyLength: int, needAdd: bool) -> tuple[bytes, bytes, bytes]:
    if os.path.exists(path=SECRET_FILE):
        with open(file=SECRET_FILE, mode="rt") as f:
            key: bytes = base64.b64decode(s=f.readline())
            iv: bytes = base64.b64decode(s=f.readline())
            if needAdd:
                add: bytes = base64.b64decode(s=f.readline())
        return key, iv, add
    else:
        key: bytes = os.urandom(keyLength)
        iv: bytes = os.urandom(keyLength)
        add: bytes = None
        if needAdd:
            add = os.urandom(keyLength)
            pass
        with open(file=SECRET_FILE, mode="wt") as f:
            f.write(f"{base64.b64encode(s=key).decode()}\n")
            f.write(f"{base64.b64encode(s=iv).decode()}\n")
            f.write(f"{base64.b64encode(s=add).decode()}\n")
            pass
        return gen_secret_key(keyLength=keyLength, needAdd=needAdd)

def encrypt(key: bytes, iv: bytes, add: bytes, data: bytes) -> tuple[bytes, bytes]:
    cipher: Cipher = Cipher(algorithm=algorithms.AES(key), \
                            mode=modes.GCM(initialization_vector=iv))
    encryptor: CipherContext = cipher.encryptor()
    # result: bytearray = bytearray()
    result: list[bytes] = []
    encryptor.authenticate_additional_data(add)
    # result += encryptor.update(data=data)
    # result += encryptor.finalize()
    tmp = encryptor.update(data=data)
    logger.info(f"tmp:{len(tmp)} init:{len(result)}")
    result.append(tmp)
    logger.info(f"rs:{len(result)}")
    result.append(encryptor.finalize())
    tag: bytes = encryptor.tag
    return b"".join(result), tag

def decrypt(key: bytes, iv: bytes, add: bytes, tag: bytes, data: bytes) -> bytes:
    cipher: Cipher = Cipher(algorithm=algorithms.AES(key), \
                            mode=modes.GCM(initialization_vector=iv, tag=tag))
    decryptor: CipherContext = cipher.decryptor()
    # result: bytearray = bytearray()
    result = [b""]
    decryptor.authenticate_additional_data(add)
    # result += decryptor.update(data=data)
    # result += decryptor.finalize()
    result.append(decryptor.update(data=data))
    result.append(decryptor.finalize())
    return b"".join(result)


if __name__ == "__main__":
    plain_data: bytes = b"test try again"
    logger.info(f"plain data:{base64.b64encode(s=plain_data).decode('utf-8')}")
    key, iv, add = gen_secret_key(16, True)
    crypted_data, tag = encrypt(key=key, iv=iv, add=add, data=plain_data)
    logger.info(f"encrypted base64:{base64.b64encode(s=crypted_data).decode('utf-8')} tag:{base64.b64encode(s=tag).decode('utf-8')}")
    try:
        replain_data: bytes = decrypt(key=key, iv=iv, add=add, tag=tag, data=crypted_data)
        logger.info(f"decrypted base64:{base64.b64encode(s=replain_data).decode('utf-8')} \n|{str(object=replain_data, encoding='utf-8')}|")
        pass
    except (InvalidTag, TypeError) as ex:
        logger.error("", ex)
        pass
    pass

