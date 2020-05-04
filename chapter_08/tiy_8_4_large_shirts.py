# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #


def make_shirt(size='l', text='i love python'):
    print(f'\nWe will print a t-shirt size "{size.title()}" with the '
          f'following text: {text.title()}')


if __name__ == '__main__':
    make_shirt()
    make_shirt(size='m')
    make_shirt('s', 'the world is female')


