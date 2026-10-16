
from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

for nivel in range(1, 6):
    cor = definir_cor(nivel)
    situacao = niveis[nivel - 1]
    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)
