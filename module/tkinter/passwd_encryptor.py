import tkinter as tk
from tkinter import ttk

from module.tkinter.models import PasswordFormModel
from module.tkinter.views import PasswordFormView
from module.tkinter.controllers import PasswordFormController

class App(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        return

    def __init_windows(self) -> None:
        # set wd size
        width = 500
        height = 250
        self.geometry(f"{width}x{height}")
        self.update_idletasks()
        # self.config(width=600, height=300)
        # set wd position at center of screen
        print(f"winfo height:{self.winfo_height()}")
        center_x = (self.winfo_screenwidth() - self.winfo_width())//2
        center_y = (self.winfo_screenheight() - self.winfo_height())//2
        self.geometry(f"{width}x{height}+{center_x}+{center_y}")
        return

    def __init_app(self) -> None:
        self.title("Encryptor")
        # create Model
        model: PasswordFormModel = PasswordFormModel(self)
        # create View
        view: PasswordFormView = PasswordFormView(self)
        # create Controller
        controller: PasswordFormController = PasswordFormController(model=model, view=view)
        view.controller = controller

        controller.init_view()

        return

    def start(self) -> None:
        self.__init_app()
        self.__init_windows()
        self.mainloop()
        return
    
    # end class
    pass



if __name__ == "__main__":
    app = App()
    app.start()
    pass