from datetime import datetime

uniStr: str = f"hi server máy chủ at:{ datetime.now() }"
uniBytes: bytes = bytes(uniStr, "utf-8")
print(f"result:{uniBytes.decode('utf-8')} len:{len(uniBytes)}")

total: int =0

print(f"start:{datetime.now()}")
for i in range(0, 10000000):
    total += i
    pass
print(f"end:{datetime.now()}")