import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
         x = generate_integer(level)
         y = generate_integer(level)
         for j in range (3):
              ans = int(input(f'{x} + {y} = '))
              if ans == (x + y):
                   score += 1
                   break
              else:
                   print ('EEE')
         if ans != (x+y):
            print (x+y)

    print ('Score:',score)


def get_level():
    while True:
        try:
            level = int(input ('Level: '))
            if level in [1,2,3]:
                    return level
        except ValueError:
            pass


def generate_integer(level):
     if level == 1:
          rand = random.randint(0,9)
     elif level == 2:
          rand = random.randint(10,99)
     elif level == 3:
          rand = random.randint(100,999)
     else:
          raise ValueError

     return rand


if __name__ == "__main__":
    main()
