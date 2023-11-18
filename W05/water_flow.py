# Function to calculate the height of the water column
def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height / 4)

# Let's test this function with the given values.
test_cases = [
    (0, 0, 0),
    (0, 10, 7.5),
    (25, 0, 25),
    (48.3, 12.8, 57.9)
]

# We will just print the results here to verify the correctness.
for tower_height, tank_height, expected in test_cases:
    result = water_column_height(tower_height, tank_height)
    print(f"water_column_height({tower_height}, {tank_height}) = {result} (Expected: {expected})")

# Function to calculate the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank
def pressure_gain_from_water_height(height):
    rho = 998.2  # density of water in kilogram / meter^3
    g = 9.80665  # acceleration due to gravity in meter / second^2
    return (rho * g * height) / 1000  # pressure in kilopascals

# Let's test this function with the given values.
pressure_test_cases = [
    (0, 0),
    (30.2, 295.628),
    (50, 489.450)
]

# We will just print the results here to verify the correctness.
for height, expected in pressure_test_cases:
    result = pressure_gain_from_water_height(height)
    print(f"pressure_gain_from_water_height({height}) = {result:.3f} kPa (Expected: {expected} kPa)")

# Function to calculate the water pressure lost because of the friction between the water and the walls of a pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2  # density of water in kilogram / meter^3
    # Calculate the lost pressure in kilopascals using the given formula
    return -(friction_factor * pipe_length * rho * fluid_velocity**2) / (2000 * pipe_diameter)

# Let's test this function with the given values.
pressure_loss_test_cases = [
    (0.048692, 0, 0.018, 1.75, 0),
    (0.048692, 200, 0, 1.75, 0),
    (0.048692, 200, 0.018, 0, 0),
    (0.048692, 200, 0.018, 1.75, -113.008),
    (0.048692, 200, 0.018, 1.65, -100.462),
    (0.28687, 1000, 0.013, 1.65, -61.576),
    (0.28687, 1800.75, 0.013, 1.65, -110.884),
]

# We will just print the results here to verify the correctness.
for diameter, length, friction, velocity, expected in pressure_loss_test_cases:
    result = pressure_loss_from_pipe(diameter, length, friction, velocity)
    print(f"pressure_loss_from_pipe(diameter={diameter}, length={length}, friction={friction}, velocity={velocity}) = {result:.3f} kPa (Expected: {expected} kPa)")

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2  # density of water in kg/m^3
    # Calculate the pressure loss due to fittings
    P = -(0.04 * rho * fluid_velocity ** 2 * quantity_fittings) / 2000
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = 998.2  # density of water in kg/m^3
    mu = 0.0010016  # dynamic viscosity of water in Pascal seconds
    # Calculate the Reynolds number
    R = (rho * hydraulic_diameter * fluid_velocity) / mu
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    rho = 998.2  # density of water in kg/m^3
    # Calculate the constant k using the first formula
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    # Calculate the lost pressure in kilopascals using the second formula
    P = -k * rho * fluid_velocity**2 / 2000
    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()