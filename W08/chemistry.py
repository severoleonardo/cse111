class FormulaError(ValueError):
    """FormulaError is the type of error that the parse_formula
    function will raise if a formula is invalid.
    """


def make_periodic_table():
    """Create and return the periodic table dictionary.

    Return: a dictionary containing information about chemical elements.
        The keys are chemical symbols, and the values are lists
        with the element name and atomic mass.
    """
    # periodic table list
    periodic_table_list = [
        # [symbol, name, atomic_mass]
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        # ... (other elements)
    ]

    # Convert the list into a dictionary
    periodic_table_dict = {symbol: [name, atomic_mass] for symbol, name, atomic_mass in periodic_table_list}
    return periodic_table_dict


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule.

    Parameters:
        formula (str): a string that contains a chemical formula.
        periodic_table_dict (dict): the compound dictionary returned
            from make_periodic_table.

    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        f"Wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        f"Wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        f"but must be a dictionary"

    # Rest of the code remains the same...


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters:
        symbol_quantity_list (list): a compound list returned
            from the parse_formula function.
        periodic_table_dict (dict): the compound dictionary
            returned from make_periodic_table.

    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    """
    # Rest of the code remains the same...


def main():
    # Get a chemical formula for a molecule from the user.
    formula = input("Enter the molecular formula of the sample: ")

    # Get the mass of a chemical sample in grams from the user.
    mass = float(input("Enter the mass in grams of the sample: "))

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)

    # Compute the number of moles in the sample.
    moles = mass / molar_mass

    # Print the molar mass.
    print(f"{molar_mass:.5f} grams/mole")

    # Print the number of moles.
    print(f"{moles:.5f} moles")


if __name__ == "__main__":
    main()
