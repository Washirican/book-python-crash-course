# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #


def make_shirt(size, text):
    print(f'\nWe will print a t-shirt size "{size.title()}" with the following '
          f'text: {text.title()}')


if __name__ == '__main__':
    make_shirt('s', 'the world is female')
    make_shirt(text='carpe diem, motherfucker', size='l')

