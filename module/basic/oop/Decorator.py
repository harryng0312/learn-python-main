from functools import wraps


def wrap_dec(loopcount: int):
    def my_decorator(func):
        # @wraps(func)
        def wrapper(name: str, *args, **kwargs):
            print("Something is happening before the function is called.")
            for i in range(0, loopcount):
                func(name)
            print("Something is happening after the function is called.")
        return wrapper
    return my_decorator

@wrap_dec(loopcount=4)
def say_whee(name:str):
    print(f"Whee! {name}")


if __name__ == "__main__":
    # say_whee = my_decorator(say_whee)
    say_whee("jas")
    pass