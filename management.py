"""Operations with seat reservation.

Functions:
    res
        Reservation of seat.
    cancel
        Cancel of reservation.

"""


from zones import *
from planes import *


my_planes = {}
my_reserves = {}
my_zones = {}
my_rates = []


def res():
    """Reservation of seat.

    Return:
        None
    """
    msg_seat = 'Введите свободное место (EXIT для выхода): '
    place = input('Введите пункт назначения (EXIT для выхода): ')

    if place in ('exit', 'e'):
        return None

    if place not in my_planes:
        my_planes[place] = Plane()
    if place not in my_zones:
        my_zones[place] = Zone(my_planes[place].seats)
    if place not in my_reserves:
        my_reserves[place] = Reserve(my_planes[place].seats)

    print(my_planes[place])
    my_rates.append(Rate(place, input('Выберите тариф: ')))

    print(my_zones[place])
    print(my_reserves[place])

    while True:
        num = input(msg_seat)
        if num in ('exit', 'e'):
            return None
        elif num.isdigit():
            num = int(num)
        else:
            continue

        my_rates[-1].num = num

        if my_reserves[place].take(num):
            break

    my_zones[place].coefficient = num
    my_rates[-1].price = my_zones[place].coefficient

    if input(f'Стоимость билета {my_rates[-1].price:.2f}, оплатить? '
             f'(YES для подтверждения) ') in ('y', 'yes'):

        print(f'{my_planes[place]} Пункт назначения {place}. Место '
              f'{num}. Стоимость билета {my_rates[-1].price:.2f} руб.')

    else:
        my_reserves[place].cancel(num)
        del my_rates[-1]


def cancel():
    """Cancel of reservation.

    Return:
        None
    """
    if not my_rates:
        print('Нет забронированных билетов')
        return None

    for n, i in enumerate(my_rates):
        print(f'Билет {n}. {my_planes[i.place]} Пункт назначения {i.place}.'
              f' Место {i.num}. Стоимость билета {i.price:.2f} руб.')

    n = input('Ведите номер билета для отмены брони (EXIT для выхода): ')
    if n.isdigit() and 0 <= (n := int(n)) < len(my_rates):
        my_reserves[my_rates[n].place].cancel(my_rates[n].num)
        del my_rates[n]
