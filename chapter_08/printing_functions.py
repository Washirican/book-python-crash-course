# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-07
# --------------------------------------------------------------------------- #


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
