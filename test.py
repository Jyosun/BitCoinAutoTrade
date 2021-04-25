import pyupbit

access = "wn7xtR6iIRm3B3KAMPGgsME7WM0aPIBJLiCIVeza"          # 본인 값으로 변경
secret = "EYbHZ9KR9wt9nEkhVdK0c8iOUAEm5x7gvgAZLZpp"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회