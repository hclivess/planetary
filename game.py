import os
import random
import json

titan_names = "Adanus", "Anchiale", "Andes", "Anytus", "Asteria", "Astraeus", "Atlas", "Aura", "Clymene", "Coeus", "Crius", "Cronus", "Curetes", "Dione", "Eos", "Epimetheus", "Eurybia", "Eurynome", "Gigantes", "Hecate", "Helius", "Hoplodamus", "Hyperion", "Iapetus", "Lelantos", "Leto", "Megamedes", "Melisseus", "Menoetius", "Metis", "Mnemosyne", "Muses Elder", "Mylinus", "Oceanus", "Olymbrus", " lympus", "Ophion", "Ostasus", "Pallas", "Perses", "Phoebe", "Phorcys", "Polus", "Prometheus", "Rhea", "Selene", "Styx", "Syceus", "Tethys", "Theia", "Themis", "Titan"


def save_planet(position, name, resources):
    file_check("planets.json")

    with open("planets.json", "r") as infile:
        planets = json.loads(infile.read())

    identificator = len(planets) + 1

    planets.append({"id": identificator,
                    "position": position,
                    "name": name,
                    "resources": resources})

    print(planets)

    with open("planets.json", "w") as outfile:
        outfile.write(json.dumps(planets))


def generate_planet_name():
    name_candidate = random.choice(titan_names)

    while True:
        if not planet_exists(name_candidate):
            return name_candidate
        else:
            name_candidate = random.choice(titan_names)


def generate(limit=1000):
    return random.randint(0, limit)


def generate_position(limit=1000):
    x_pos = generate(limit)
    y_pos = generate(limit)

    return {"x_pos": x_pos,
            "y_pos": y_pos}


def file_check(file):
    if not os.path.exists(file):
        with open(file, "w") as infile:
            infile.write(json.dumps([]))


def planet_exists(name):
    file_check("planets.json")
    with open("planets.json", "r") as infile:
        planets = json.loads(infile.read())
        for planet in planets:
            if planet["name"] == name:
                return True
            else:
                return False


def generate_resources(limit=100):
    
    farmland = generate(limit)
    bismuth = generate(limit)
    iron = generate(limit)
    gold = generate(limit)

    return ({"farmland": farmland,
             "bismuth": bismuth,
             "iron": iron,
             "gold": gold})


if __name__ == "__main__":
    print(generate_position())
    print(generate_resources())
    print(generate_planet_name())

    save_planet(name=generate_planet_name(),
                position=generate_position(),
                resources=generate_resources())

    print(planet_exists("Lelantos"))