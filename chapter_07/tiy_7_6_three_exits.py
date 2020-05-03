# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #


prompt = '\nWhat toppings would you like in your pizza?'
prompt += '\n(Enter \'done\' when finished.) '

# Use activate variable to control how the loop runs.
active = True

while active:
    ingredient = input(prompt)

    if ingredient == 'done':
        # Use conditional test in the while loop to stop the lop.
        active = False

    if active is False:
        # Use a break statement to exit the loop when the user enters a
        # 'quit' value
        break

    print(f'\nI will add {ingredient.title()} to your pizza!')

