#Head or tails 
import random
random_side = random.randint(0, 1)
coin = ""

if random_side == 0:
  coin = "Heads"
else:
  coin = "Tails"

print(coin)