def main():
    f = get_fuel()
    print(f)


def get_fuel():
    while True:
        try:
            fraction = input('Fraction: ')
            x, z = fraction.split('/')
            x = int(x)
            z = int(z)

            if z != 0 and x <= z and x >= 0:
                percentage = round(x/z * 100)
                if percentage <= 1:
                    return 'E'
                elif percentage >= 99:
                    return 'F'
                else:
                    return f'{percentage}%'


        except (ValueError, ZeroDivisionError):
            pass


main()