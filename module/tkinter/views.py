from __future__ import annotations
import tkinter as tk
from tkinter import Misc, ttk
from tkinter.scrolledtext import ScrolledText

class PasswordFormView(ttk.Frame):

    def __init__(self, master: Misc | None = None, **kw) -> None:
        super().__init__(master, **kw)
        return

    def __add_controls(self, model: PasswordFormModel) -> None:
        self.master.grid_rowconfigure(index=0, weight=1)
        self.master.grid_columnconfigure(index=0, weight=1)
        style = ttk.Style(master=self)
        # style.theme_use("default")
        # lb_style.theme_use("default")
        # Create style used by default for all Frames
        style.configure(style='tf.TFrame')
        lb_style = ttk.Style(master=self).configure(style='tf.TLabel')
        txt_style = ttk.Style(master=self).configure(style='tf.TEntry')
        # add frame
        self.config(style="tf.TFrame")
        # self.config(style="tf.TWidget")
        # create layout
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(index=1, weight=1)
        # self.grid_configure(ipadx=15, ipady=15, sticky="nsew")
        # self.pack(fill=tk.BOTH, expand=True)
        # frm.pack(expand=True)
        # add controls
        lb_client_pub_key = ttk.Label(master=self, style="tf.TLabel", text="Client Public Key:")
        lb_session_id = ttk.Label(master=self, state="tf.TLabel", text="Session ID:")
        lb_random_no = ttk.Label(master=self, state="tf.TLabel", text="Random ID:")
        lb_server_pub_key = ttk.Label(master=self, style="tf.TLabel", text="Server Public Key:")
        lb_plain_passwd = ttk.Label(master=self, style="tf.TLabel", text="Plained Password:")
        lb_encrypted_passwd = ttk.Label(master=self, style="tf.TLabel", text="Encrypted Password:")
        
        txt_client_pub_key_val = ttk.Entry(master=self, style="tf.TEntry", textvariable=model.client_pubkey, state="readonly")
        txt_session_id = ttk.Entry(master=self, style="tf.TEntry", textvariable=model.session_id)
        txt_random_no = ttk.Entry(master=self, style="tf.TEntry", textvariable=model.random_no)
        txt_server_pub_key = ttk.Entry(master=self, style="tf.TEntry", textvariable=model.server_pubkey)
        txt_plain_passwd = ttk.Entry(master=self, style="tf.TEntry", textvariable=model.plain_passwd)
        txt_encrypted_passwd_val = ttk.Entry(master=self, style="tf.TLabel", textvariable=model.enc_passwd, state="readonly")
        
        btn_enc = ttk.Button(master=self, text="Encrypt")

        # layout
        lb_client_pub_key.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        lb_session_id.grid(row=1, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        lb_random_no.grid(row=2, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        lb_server_pub_key.grid(row=3, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        lb_plain_passwd.grid(row=4, column=0, padx=(0, 5), pady=(0, 5), sticky="e")
        lb_encrypted_passwd.grid(row=5, column=0, padx=(0, 5), pady=(0, 5), sticky="e")

        txt_client_pub_key_val.grid(row=0, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        txt_session_id.grid(row=1, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        txt_random_no.grid(row=2, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        txt_server_pub_key.grid(row=3, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        txt_plain_passwd.grid(row=4, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")
        txt_encrypted_passwd_val.grid(row=5, column=1, padx=(0, 5), pady=(0, 5), sticky="ew")

        btn_enc.grid(row=6, column=1, columnspan=2, padx=(0, 5), pady=(0, 5), sticky="w")
        # lb_client_pub_key.grid(row=0, column=0, sticky="e")
        # lb_client_pub_key_val.grid(row=0, column=1, sticky="ew")
        # lb_server_pub_key.grid(row=1, column=0, sticky="e")
        # txt_server_pub_key.grid(row=1, column=1, sticky="ew")
        # txt_session_id.grid(row=2, column=1, sticky="ew")
        # btn_enc.grid(row=5, column=1, columnspan=2, sticky="w")
        
        # self.pack()
        # bind events
        btn_enc.bind('<Return>', self.btn_enc_return)
        btn_enc.bind('<Button-1>', self.btn_enc_return)
        # add
        print(f"model in view:{id(model)}")
        return
    
    def init_view(self, model:PasswordFormModel) -> None:
        self.__add_controls(model)
        return


    @property
    def controller(self) -> PasswordFormController:
        return self.__controller
    
    @controller.setter
    def controller(self, controller: PasswordFormController):
        self.__controller = controller
        return

    def btn_enc_return(self, evt: tk.Event) -> None:
        if self.controller:
            self.controller.btn_encrypt_passwd(evt)
            pass
        return

    # end class
    pass

from module.tkinter.models import PasswordFormModel
from module.tkinter.controllers import PasswordFormController