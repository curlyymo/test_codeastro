def weight_on_planet(mass_kg, planet='Mars'):
    surface_gravity = {
        'Mercury': 3.7,
        'Venus': 8.87,
        'Earth': 9.81,
        'Mars': 3.71,
        'Jupiter': 24.79,
        'Saturn': 10.44,
        'Uranus': 8.69,
        'Neptune': 11.15,
        'Pluto': 0.62
    }

    if planet not in surface_gravity:
        raise ValueError(f"Unknown planet: {planet}")

    return mass_kg * surface_gravity[planet]
