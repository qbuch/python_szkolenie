coins = (5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.02)
coins_to_change = [0, 0, 0, 0, 0, 0, 0, 0, 0]

cash = 20
total_value = 8.30
change = cash - total_value
idx = 0

for coin in coins:
    if change > 0 and change >= coin:
        quantity = change // coin    #2
        value_of_coins = quantity * coin    # 2 * 5
        change = round(change - value_of_coins, 2)    # 11.70 - (2*5)''

        coins_to_change[idx] = quantity

    idx +=1

print(coins_to_change)
