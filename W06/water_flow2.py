from water_flow import pressure_loss_from_fittings

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)



def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2  # Density of water in kilogram / meter^3
    # Calculate the lost pressure in kilopascals using the given formula
    return -0.04 * rho * fluid_velocity**2 * quantity_fittings / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = 998.2  # Density of water in kilogram / meter^3
    mu = 0.0010016  # Dynamic viscosity of water in Pascal seconds
    # Calculate the Reynolds number using the given formula
    return (rho * hydraulic_diameter * fluid_velocity) / mu

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    rho = 998.2  # Density of water in kilogram / meter^3
    # Calculate the constant k using the first formula
    k = 0.1 + (50 / reynolds_number) * (larger_diameter / smaller_diameter)**4 - 1
    # Calculate the lost pressure in kilopascals using the second formula
    return -k * rho * fluid_velocity**2 / 2000

