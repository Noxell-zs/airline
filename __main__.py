"""Descriptions of the business process of reserve seats in the airline

Reservation of seat.
Cancel of reservation.

Run the main program:
    python -m airline


:Author:
    Замолоцкий Семен Андреевич, КИ20-17/1б

"""


from management import *


def info():
    """Output information about available commands."""
    print()
    print('EXIT для выхода из программы')
    print('RESERVE для бронирования места')
    print('CANCEL для отмены брони')


def main():
    """Main module; example of menu."""
    msg_info = 'Введите команду (INFO для списка команд): '

    while (enter := input(msg_info).lower()) not in ('exit', 'e'):
        if enter in ('info', 'i'):
            info()
        if enter in ('res', 'r'):
            res()
        elif enter in ('cancel', 'c'):
            cancel()


if __name__ == '__main__':
    main()
