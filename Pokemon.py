#!/usr/bin/python3
# pylint:disable=E0602
import random
from colorama import Fore, init
import time
import sys
import os

init()
# https://www.asciiart.eu/video-games/pokemon

pokemon_1 = {
    "nombre": "Charmander",
    "tipo": "Fuego",
    "turno": 0,
    "debilidad": ["Agua", "Tierra", "Aire"],
    "nivel": 5,
    "proximo_nivel": 1200,
    "experiencia": 500,
    "salud": 100,
    "defenza": 10,
    "ataques": {
        1: {"nombre": "Arañazo", "ataque": 40, "PP": 1},
        2: {"nombre": "Ascuas", "ataque": 40, "PP": 2},
        3: {"nombre": "Dragoaliento", "ataque": 60, "PP": 1},
        4: {"nombre": "Lanzallamas", "ataque": 90, "PP": 2},
        5: {"nombre": "Rendirse", "ataque": 0, "PP": 1},
    },
    "icono": Fore.RED
    + """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⣠⣄⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⡸⢛⣷⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⢰⣷⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⢏⡏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠁⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣦⡀⠐⠂⠠⠴⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢀⠀⠀⠀
⠀⢰⠦⣄⠈⢿⣶⡶⠤⠤⠤⠔⠒⠒⣶⠒⡫⢋⡄⠀⢸⠀⠀⠀⠀⢀⣀⠤⣤⠀⠀⠀⠀⠀⢀⡞⠉⠛⢆⠀⠀
⢰⡟⢷⠂⠉⠚⠿⣿⣄⣀⣀⣀⣠⣴⣛⣯⠔⠋⠀⠠⠼⠦⠔⠒⠊⠁⠠⡶⢧⡄⠀⠀⠀⠀⠸⣧⠀⡀⠈⣿⠀
⠀⠙⢮⡀⠀⠀⠀⠈⠉⡖⠛⠋⠉⠉⠁⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⠞⠁⠀⠀⠀⠀⠀⡏⠿⢧⢀⠈⡆
⠀⠀⠀⠙⢄⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠸⣯⠀⡿
⠀⠀⠀⠀⠀⠓⢄⣠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠐⠒⢖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠉⣶⡇
⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣴⢦⠞⠁
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⢀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠤⠤⢤⣸⠓⠢⠄⢀⠀⠤⠔⠊⠁⠀⠀⡼⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⢀⡜⠉⠉⠛⢧⠀⠀⠀⠀⠀⠀⣸⠥⣄⣀⣀⣀⠠⠖⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢸⠇⠀⠀⠀⢀⣴⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣷⣦⣀⣀⣀⡀⠤⠤⠤⠚⠁⠀⠀⠀⢸⡤⢤⡤⢤⡴⢤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠾⡷⠞⠿⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
}


pokemon_2 = {
    "nombre": "Blastoise",
    "tipo": "Agua",
    "turno": 0,
    "debilidad": ["Agua", "Tierra", "Aire"],
    "nivel": 5,
    "proximo_nivel": 1200,
    "experiencia": 500,
    "salud": 100,
    "defenza": 10,
    "ataques": {
        1: {"nombre": "Placaje", "ataque": 40, "PP": 1},
        2: {"nombre": "Pistola agua", "ataque": 40, "PP": 1},
        3: {"nombre": "Mordisco", "ataque": 60, "PP": 1},
        4: {"nombre": "Hidrobomba", "ataque": 90, "PP": 1},
        5: {"nombre": "Rendirse", "ataque": 0, "PP": 1},
    },
    "icono": Fore.BLUE
    + """
    ⠀⠀⠀⠀⠀⣠⣴⣾⣶⣿⣿⣶⣶⣶⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣼⣿⣿⣿⣋⣠⣿⣿⣿⣿⣿⡖⢶⣶⣤⣤⣀⣤⣶⣿⣷⡤⠶⢦⡀⠀
⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠘⢿⣿⣿⣿⡿⢁⣾⡀⠀⠀⣷⠀
⠀⠀⠻⣿⠟⠛⠛⠻⠟⠛⠋⢹⣿⣿⣿⢣⡆⠀⠈⠛⠛⠋⠀⢻⣿⣿⣶⠟⣻⣦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢇⣾⠃⠀⣠⣤⣴⣤⣤⣀⠉⠙⢁⣴⡿⠁
⠀⠀⠀⠀⠀⢠⠀⠀⠀⢰⣤⣿⣿⢋⣬⡄⢀⣾⣿⣿⣿⣿⣿⣿⣧⠀⢿⣿⠀⠀
⠀⠀⠀⠀⠀⣠⠻⠿⠿⠿⠿⣛⣵⣿⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣄⣼⣿⡇⠀
⠀⠀⠀⠀⣠⣿⡀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠆⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢀⣀⣴⣾⣿⣿⡇⣬⣭⣭⣭⣭⣭⣶⣶⣿⣷⡄⢈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠰⢾⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢐⣛⡻⣿⣿⣿⣿⣿⣿⠻⣿⣿⠀
⠀⠁⠀⣠⣶⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⡵⠿⢿⣿⣿⣿⢟⣄⢹⡏⠀
⠀⠀⣰⣿⣿⣿⣿⣆⢲⣶⣶⣶⣶⣶⣶⣶⣿⢇⣷⣾⣿⡏⣟⣯⣶⣿⣿⡾⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣦⠹⣿⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠋
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣷⣬⠉⠿⣛⣻⣿⣯⣥⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⣠⣶⣿⣿⣿⣿⣿⣿⠿⠿⠦⠄⠀⠀⠉⠉⠉⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⠛⠿⣿⠟⠛⠛⠀⠀
    
    """,
}


def turnos(*args):
    n = random.randrange(0, 2, 1)
    if n == 1:
        pk_1 = args[1]
        pk_2 = args[0]
        pk_1["turno"] = 1
    else:
        pk_1 = args[0]
        pk_2 = args[1]
        pk_2["turno"] = 1
    return (pk_1, pk_2)


def pelea(p_1, p_2):
    print(Fore.LIGHTYELLOW_EX + f"¿Que deberia hacer {p_1['nombre']}?")
    for id, ataq in p_1["ataques"].items():
        print(Fore.LIGHTWHITE_EX + f"{id}: {ataq['nombre']} PP[{ataq['PP']}]")
    atq = None
    j = None
    valora = True
    while valora:
        try:
            n = int(input(Fore.LIGHTBLUE_EX + "::"))
            if n >= 1 or n <= 5:
                if n == 5:
                    print(Fore.RED + f" {p_1['nombre']} se rindio \n")

                    p_1["salud"] = 0
                    j = 0
                    break

                atq = p_1["ataques"][n]
                j = atq["PP"]
                if j > 0:
                    p_1["ataques"][n]["PP"] = j - 1

                print(f" {p_1['nombre']} usa {atq['nombre']}\n")
                valora = False

            else:
                raise Exception(f"{p_1['nombre']} eh?")

        except:
            print(f"{p_1['nombre']} ¡eh!")

    salud_2 = p_2["salud"]
    salud_1 = p_1["salud"]
    if j > 0:
        ataque = p_2["defenza"] - atq["ataque"]
    else:
        ataque = 0

    if ataque > 0:
        salud_1 = salud_1 - ataque
        p_1["salud"] = salud_1 - ataque
        print(
            Fore.GREEN + f"{p_1['nombre']} resulto herido por la defenza de su rival.\n"
        )

    elif ataque < 0:
        salud_2 = salud_2 + ataque
        p_2["salud"] = salud_2
        print(Fore.LIGHTBLACK_EX + f"{p_2['nombre']} resulto herido por su rival.")
    elif j == 0 and n != 5:
        print(Fore.LIGHTBLACK_EX + f"{p_1['nombre']} ya no tienes PP en ese ataque.\n")

    elif n != 5:

        print(
            Fore.LIGHTBLACK_EX + f"{p_2['nombre']} no se vio afectado por el ataque.\n"
        )


def pelea_automativa(p_1, p_2):

    atq = None
    j = None
    valora = True
    while valora:
        try:
            n = random.randrange(1, 5)
            if n >= 1 or n <= 4:
                atq = p_1["ataques"][n]
                pp = atq["PP"]
                if pp > 0:
                    p_1["ataques"][n]["PP"] = pp - 1

                print(f" {p_1['nombre']} uso {atq['nombre']}\n")
                valora = False
            else:
                raise Exception(f"{p_1['nombre']} eh?")
        except:
            print(f"{p_1['nombre']} ¡eh!")

    salud_2 = p_2["salud"]
    salud_1 = p_1["salud"]
    if pp > 0:
        ataque = p_2["defenza"] - atq["ataque"]
    else:
        ataque = 0

    if ataque > 0:
        salud_1 = salud_1 - ataque
        p_1["salud"] = salud_1 - ataque
        print(
            Fore.GREEN + f"{p_1['nombre']} resulto herido por la defenza de su rival.\n"
        )
    elif ataque < 0:
        salud_2 = salud_2 + ataque
        p_2["salud"] = salud_2
        print(Fore.LIGHTBLACK_EX + f"{p_2['nombre']} resulto herido por su rival.")
    elif pp == 0:
        print(Fore.LIGHTBLACK_EX + f"{p_1['nombre']} ya no tienes PP en ese ataque.\n")
    else:
        print(
            Fore.LIGHTBLACK_EX + f"{p_2['nombre']} no se vio afectado por el ataque.\n"
        )
    time.sleep(0.2)


def barra_salud(pokemon):

    MAX_SALUD = 100
    porciento = (pokemon["salud"] * 100) // MAX_SALUD
    MAX_SIZE = 100
    salud = (MAX_SIZE * porciento) // MAX_SALUD
    sl = "#" * salud
    barra_salud = sl.ljust(MAX_SIZE, " ")
    nombre = pokemon["nombre"]
    barra = (
        Fore.LIGHTRED_EX
        + f"{nombre}\n "
        + Fore.LIGHTCYAN_EX
        + f"PS ["
        + Fore.LIGHTGREEN_EX
        + f"{barra_salud}"
        + Fore.LIGHTCYAN_EX
        + f"] {pokemon['salud']}/100"
    )
    print(barra)
    print("\n")
    print(pokemon["icono"])
    print("\n")


def run(pokemon_1, pokemon_2):
    logo = (
        Fore.LIGHTYELLOW_EX
        + f"""                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
    
    """
    )
    print(logo)
    turno = 1
    pk_1, pk_2 = turnos(pokemon_1, pokemon_2)
    key = pk_1
    print("\n")
    while pk_1["salud"] > 0 and pk_2["salud"] > 0:
        if turno == 1:
            barra_salud(pk_1)
            barra_salud(pk_2)
            pelea(pk_2, pk_1)
            turno -= 1
            time.sleep(5)
        elif turno == 0:
            barra_salud(pk_2)
            barra_salud(pk_1)
            pelea_automativa(pk_1, pk_2)
            turno += 1
            print("\n")
            time.sleep(3)
    else:
        if pk_1["salud"] <= 0:
            # print(Fore.GREEN + f"{pk_2['nombre']} gano el encuentro.")
            time.sleep(3)
            print(
                Fore.YELLOW
                + f"{pk_1['nombre']} no puede continuar, acude al centro pokemon mas cercano."
            )
        else:
            print(Fore.GREEN + f"{pk_1['nombre']} gano el encuentro.")
            time.sleep(3)
            print(
                Fore.YELLOW
                + f"{pk_2['nombre']} no puede continuar, acude al centro pokemon mas cercano."
            )


run(pokemon_1, pokemon_2)
