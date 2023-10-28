import math

# Function to compute the volume of a cylinder
def compute_volume(radius, height):
    return math.pi * radius ** 2 * height

# Function to compute the surface area of a cylinder
def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Function to compute and print the storage efficiency of a can
def compute_and_print_storage_efficiency(name, radius, height, cost):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area

# Function to print the results for each can size    

    print(f"{name} {storage_efficiency:.2f}")

# Main function
def main():
    # Define data for 12 can sizes with name, radius, height, and cost per can
    can_sizes = [
             {
                "name": "#1 Picnic",
                "radius": 6.83,
                "height": 10.16,
                "cost": 0.28
            },
            {
                "name": "#1 Tall",
                "radius": 7.78,
                "height": 11.91,
                "cost": 0.43
            },
            {
                "name": "#2",
                "radius": 8.73,
                "height": 11.59,
                "cost": 0.45
            },
            {
                "name": "#2.5",
                "radius": 10.32,
                "height": 11.91,
                "cost": 0.61
            },
            {
                "name": "#3 Cylinder",
                "radius": 10.79,
                "height": 17.78,
                "cost": 0.86
            },
            {
                "name": "#5",
                "radius": 13.02,
                "height": 14.29,
                "cost": 0.83
            },
            {
                "name": "#6Z",
                "radius": 5.40,
                "height": 8.89,
                "cost": 0.22
            },
            {
                "name": "#8Z short",
                "radius": 6.83,
                "height": 7.62,
                "cost": 0.26
            },
            {
                "name": "#10",
                "radius": 15.72,
                "height": 17.78,
                "cost": 1.53
            },
            {
                "name": "#211",
                "radius": 6.83,
                "height": 12.38,
                "cost": 0.34
            },
            {
                "name": "#300",
                "radius": 7.62,
                "height": 11.27,
                "cost": 0.38
            },
            {
                "name": "#303",
                "radius": 8.10,
                "height": 11.11,
                "cost": 0.42
            }
    ]

    # Compute and print the storage efficiency and cost for each can size using a loop
    for can in can_sizes:
        compute_and_print_storage_efficiency(can["name"], can["radius"], can["height"], can["cost"])

if __name__ == "__main__":
    main()
