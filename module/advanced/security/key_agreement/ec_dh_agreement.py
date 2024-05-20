import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, BestAvailableEncryption, \
    KeySerializationEncryption, PrivateFormat, PublicFormat, load_pem_private_key, load_pem_public_key

from module.util.logger_conf import logger

class ExchangableSide:
    _derived_key_at_server: HKDF = None
    _privateKey: EllipticCurvePrivateKey
    _publicKey: EllipticCurvePublicKey
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
        self._privateKey = ec.generate_private_key(curve=ec.SECP256R1)
        self._publicKey = self._privateKey.public_key()
        return self._publicKey.public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo)

    def exchange(self, peer_public_key_bytes: bytes) -> None:
        peer_pub_key: EllipticCurvePublicKey = load_pem_public_key(peer_public_key_bytes)
        self._sharedKey = self._privateKey.exchange(algorithm=ec.ECDH(), peer_public_key=peer_pub_key)
        pass

    @property
    def shared_key(self) -> bytes:
        return self._derived_key_at_server.derive(self._sharedKey)

    pass

class ServerSide(ExchangableSide):
    pass

class PeerSide(ExchangableSide):
    pass


if __name__ == "__main__":
    server_side: ServerSide = ServerSide()
    peer_side: PeerSide = PeerSide()

    server_pub_key: bytes = server_side.generate_keypair()
    peer_pub_key: bytes = peer_side.generate_keypair()

    server_side.exchange(peer_pub_key)
    peer_side.exchange(server_pub_key)

    shared_key_at_server: bytes = server_side.shared_key
    shared_key_at_peer: bytes = peer_side.shared_key

    logger.info(f"\nshared key at server:{base64.b64encode(s=shared_key_at_server).decode()}"
                f"\nshared key at peer:{base64.b64encode(s=shared_key_at_peer).decode()}")
    pass