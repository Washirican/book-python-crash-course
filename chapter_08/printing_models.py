# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# No functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f'\nPrinting model: {current_design.title()}')
#     completed_models.append(current_design)
#
#
# # Display all completed models
# print('\nThe following models have been printed:')
# for model in completed_models:
#     print(f'\t{model.title()}')


# Same thing but with functions

def print_models(unprinted_designs, completed_models):
    """Print each design."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design.title()}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show printed models."""
    print('\nThe following models have been printed:')
    for model in completed_models:
        print(f'\t{model.title()}')


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



