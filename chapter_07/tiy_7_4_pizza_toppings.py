# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-02
# --------------------------------------------------------------------------- #

prompt = '\nWhat toppings would you like in your pizza?'
prompt += '\n(Enter \'done\' when finished.) '

active = True

while active:
    ingredient = input(prompt)

    if ingredient == 'done':
        break

    print(f'\nI will add {ingredient.title()} to your pizza!')
