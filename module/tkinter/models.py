from __future__ import annotations
import tkinter as tk

class PasswordFormModel(object):
    def __init__(self, master: tk.Tk) -> None:
        self.client_pubkey = tk.StringVar(master=master, value="")
        self.server_pubkey = tk.StringVar(master=master, value="")
        self.session_id = tk.StringVar(master=master, value="")
        self.random_no = tk.StringVar(master=master, value="")
        self.plain_passwd = tk.StringVar(master=master, value="")
        self.enc_passwd = tk.StringVar(master=master, value="")
        return

    @property
    def client_pubkey(self) -> tk.StringVar:
        return self.__client_pubkey

    @client_pubkey.setter
    def client_pubkey(self, val: tk.StringVar):
        self.__client_pubkey = val
        return
    
    @property
    def server_pubkey(self) -> tk.StringVar:
        return self.__server_pubkey
    
    @server_pubkey.setter
    def server_pubkey(self, val: tk.StringVar):
        self.__server_pubkey = val
        return
    
    @property
    def session_id(self) -> tk.StringVar:
        return self.__session_id
    
    @session_id.setter
    def session_id(self, val: tk.StringVar):
        self.__session_id = val
        return
    
    @property
    def random_no(self) -> tk.StringVar:
        return self.__random_no
    
    @random_no.setter
    def random_no(self, val: tk.StringVar):
        self.__random_no = val
        return
    
    @property
    def plain_passwd(self) -> tk.StringVar:
        return self.__plain_passwd
    
    @plain_passwd.setter
    def plain_passwd(self, val: tk.StringVar):
        self.__plain_passwd = val
        return

    @property
    def enc_passwd(self) -> tk.StringVar:
        return self.__enc_passwd

    @enc_passwd.setter
    def enc_passwd(self, val: tk.StringVar):
        self.__enc_passwd = val
        return
    
    @property
    def priv_key_b(self) -> bytes:
        return self.__priv_key_b

    @priv_key_b.setter
    def priv_key_b(self, val: bytes):
        self.__priv_key_b = val
        return

    @property
    def pub_key_b(self) -> bytes:
        return self.__pub_key_b

    @pub_key_b.setter
    def pub_key_b(self, val: bytes):
        self.__pub_key_b = val
        return

    # end class
    pass