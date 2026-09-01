months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
      date = input('Date: ')
      if '/' in date:
         x,y,z = date.split('/')
         x = int(x)
         y = int(y)
         z = int(z)

         if 1 <= x <= 12 and 1 <= y <= 31 and z > 0:
            print (f'{z}-{x:02}-{y:02}')
            break
      elif ' ' in date:
         x,y,z = date.split(' ')
         x = months.index(x) + 1
         y = int (y.strip(','))
         z = int (z)

         if 1 <= x <= 12 and 1 <= y <= 31 and z > 0:
                     print (f'{z}-{x:02}-{y:02}')
                     break


    except ValueError:
       pass

