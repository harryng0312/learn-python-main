from __future__ import annotations
import binascii
import tkinter as tk
import module.tkinter.cipher_utils as cu
from module.tkinter.models import PasswordFormModel
from module.tkinter.views import PasswordFormView

class PasswordFormController(object):
    
    def __init__(self, model: PasswordFormModel, view: PasswordFormView) -> None:
    # def __init__(self, model: PasswordFormModel, view) -> None:
        self.model = model
        self.view = view
        return
    
    def init_view(self) -> None:
        self.view.init_view(self.model)
        print(f"model in controller:{id(self.model)}")
        self.model.priv_key_b, self.model.pub_key_b = cu.generate_keypair()
        self.model.client_pubkey.set(binascii.hexlify(self.model.pub_key_b).decode())
        return

    def encrypt_passwd(self) -> None:
        return
    
    def btn_encrypt_passwd(self, evt:tk.Event) -> None:
        # print(f"model in event:{id(self.model)}")
        # import json
        # attributes = vars(self.model)
        # serialized_dict = {}
        # for key, value in attributes.items():
        #     if isinstance(value, tk.StringVar):
        #         serialized_dict[key] = value.get()
        # print(f"model:{json.dumps(obj=serialized_dict)}")
        priv_key_b, pub_key_b = self.model.priv_key_b, self.model.pub_key_b #cu.generate_keypair()
        self.model.client_pubkey.set(binascii.hexlify(pub_key_b).decode())
        other_pub_key_b = binascii.unhexlify(self.model.server_pubkey.get())
        enc_passwd = cu.encrypt_password(\
            my_priv_key_b=priv_key_b, other_pub_key_b=other_pub_key_b, plain_passwd_b=bytes(self.model.plain_passwd.get(), "utf-8"), \
            session_id_b=bytes(self.model.session_id.get(), "utf-8"), random_no_b=bytes(self.model.random_no.get(), "utf-8"))
        self.model.enc_passwd.set(binascii.hexlify(enc_passwd).decode())
        # print(f"Enc passwd:{binascii.hexlify(enc_passwd).decode()}")
        return

    pass