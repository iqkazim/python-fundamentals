amount_due= 50

while amount_due > 0:
    print ('Amount Due:', amount_due)
    insert_coin = int(input('Insert Coin: '))
    if insert_coin in [5, 10, 25]:
        amount_due = amount_due - insert_coin

print('Change Owed:', abs(amount_due))

