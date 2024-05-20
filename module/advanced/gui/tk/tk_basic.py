from module.util.logger_conf import logger
from tkinter import ttk, Tk, Misc
import asyncio

async def create_frame(master: Misc) -> None:
    frm = ttk.Frame(master=master, padding=100)
    frm.grid()
    ttk.Label(master=frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(master=frm, text="Quit", command=master.destroy).grid(column=1, row=0)
    return

async def create_windows() -> None:
    root: Misc = Tk()
    await create_frame(master=root)
    root.mainloop()
    return

if __name__ == "__main__":
    logger.info("dev")
    asyncio.run(create_windows())
    pass