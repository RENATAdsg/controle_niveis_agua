
from colorama import Fore, Style, init
init(autoreset=True)

niveis = [
    Fore.LIGHTRED_EX + "Nível 1: Muito baixo(Crítico)",  # Posição 1##
    Fore.LIGHTYELLOW_EX + "Nível 2: Baixo",  # Posição 2##
    Fore.LIGHTGREEN_EX + "Nível 3: Médio",  # Posição 3##
    Fore.LIGHTCYAN_EX + "Nível 4: Alto",  # Posição 4##
    Fore.LIGHTBLUE_EX + "Nível 5:Muito alto(Alerta)"  # Posição 5##
]


def exibir_nivel(nivel):
    print(niveis[nivel - 1])


print("---Monitoramento do reservatório---")
exibir_nivel(1)
exibir_nivel(2)
exibir_nivel(3)
exibir_nivel(4)
exibir_nivel(5)
