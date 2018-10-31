from pyparrot import Bebop

bebobAddr = "MAC ADDRESS HERE"  # todo

bop = Bebop(bebopAddr, use_wifi=True)

print("Trying to connect...")
success = bop.connect(num_retries=3)
print("connected: "+success)

if success:
    # todo
    pass
