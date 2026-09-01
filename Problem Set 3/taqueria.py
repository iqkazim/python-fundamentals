menu = {
    'baja taco': 4.25,
    'burrito': 7.50,
    'bowl': 8.50,
    'nachos': 11.00,
    'quesadilla': 8.50,
    'super burrito': 8.50,
    'super quesadilla': 9.50,
    'taco': 3.00,
    'tortilla salad': 8.00
}
total = 0
while True:
    try:
      i = input('Item: ').lower()
      if i in menu:
         total = total + menu[i]
         print(f'Total: ${total:.2f}')
    except EOFError:
       print('\n')
       break