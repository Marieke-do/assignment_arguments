# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Part 1: Greet Template

def greet(name, greeting="Hello, <name>!"):
    return greeting.replace("<name>", name)


print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))


# Part 2: Force
# g is acceleration due to gravity
# force: to hold a mass against gravity

def force(mass, body="earth"):

    g_planet = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus":8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7, 
        "moon": 1.6,
        "pluto": 0.6
        }
    body = body.lower()
    
    if body in g_planet:
        force = (mass * g_planet[body])

        return force

    else:
        return False

print(force(1, "uranus"))
print(force(1, "Uranus"))
print(force(1, "apple"))


# Part 3: Gravity
# Gravitiational attraction: F = G * (mass1 * mass2 / distance^2)
# G = gravitionial constant = 6,674×10-11 N m^2/kg^2
# m1 = mass1 (kg, float), m2 = mass2 (kg, float), d = distance (m, float)

def pull(m1=1, m2=1, d=1):
    G = 6.674 * 10**-11
    pull = G * (m1 * m2 / d**2)
    
    return pull

pull_apple_moon = pull(0.1, (5.972 * 10**24) , (6.371 * 10**6))
pull_moon_earth = pull((7.342 * 10**22), (5.972 * 10**24), (384 * 10**6))
print(pull_apple_moon)
print(pull_moon_earth)