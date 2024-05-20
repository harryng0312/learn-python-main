import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh, x448, x25519
from cryptography.hazmat.primitives.asymmetric.dh import DHPrivateKey, DHPublicKey, DHParameters
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, BestAvailableEncryption, \
    KeySerializationEncryption, PrivateFormat, PublicFormat,\
    load_pem_private_key, load_pem_public_key, load_der_private_key, load_der_public_key

from module.util.logger_conf import logger


class ExchangableSide:
    _derived_key_at_server: HKDF = None
    _privateKey: DHPrivateKey
    _publicKey: DHPublicKey
    _sharedKey: bytes

    def __init__(self) -> None:
        self._derived_key_at_server = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
        )
        pass

    def generate_keypair(self) -> bytes:
        self._privateKey = parameters.generate_private_key()
        self._publicKey = self._privateKey.public_key()
        return self._publicKey.public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo)

    def exchange(self, peer_pub_key_bytes: bytes, finalRound: bool = True) -> bytes:
        peer_pub_key: DHPublicKey = load_pem_public_key(peer_pub_key_bytes)
        if finalRound:
            self._sharedKey = self._privateKey.exchange(peer_public_key=peer_pub_key)
            return bytes()
        else:
            return self._privateKey.exchange(peer_public_key=peer_pub_key)


    @property
    def shared_key(self) -> bytes:
        return self._sharedKey  #self._derived_key_at_server.derive(self._sharedKey)

    pass


class ServerSide(ExchangableSide):
    pass


class PeerSide(ExchangableSide):
    pass


if __name__ == "__main__":
    # create peers: 1 server and 2 peers
    parameters: DHParameters = dh.generate_parameters(generator=2, key_size=2048)
    server_side: ServerSide = ServerSide()
    peer1_side: PeerSide = PeerSide()

    # generate keypairs
    server_pub_key: bytes = server_side.generate_keypair()
    peer1_pub_key: bytes = peer1_side.generate_keypair()

    # exchange final sharedkey
    server_side.exchange(peer1_pub_key)
    peer1_side.exchange(server_pub_key)

    logger.info(f"\nshared key at server:{base64.b64encode(s=server_side.shared_key).decode()}"
                f"\nshared key at peer1:{base64.b64encode(s=peer1_side.shared_key).decode()}")
    pass
