
ilha_esq = ['missionario', 'missionario',
            'missionario', 'canibal', 'canibal', 'canibal']
ilha_dir = []
barco = []
barco_posi = 1  # Se for 1 o barco está na esquerda, se for 2, o barco está na direita


def m_entra_barco(barco_posi, ilha_esq, ilha_dir):
    """
    Missionário entra no barco

    :param barco_posi: Posição que o barco se encontra
    :param ilha_esq: Lista com os elementos que estão na ilha esquerda
    :param ilha_dir: Lista com os elementos que estão na ilha direita
    :return: None
    """
    if barco_posi == 1:
        # Se não tiver missionarios desse lado para entrar no barco
        if ilha_esq.count('missionario') >= 1:
            ilha_esq.remove('missionario')
            barco.insert(0, 'missionario')
        else:
            print("Não tem missionarios nesse lado")
    else:
        # Se não tiver missionarios desse lado para entrar no barco
        if ilha_dir.count('missionario') >= 1:
            ilha_dir.remove('missionario')
            barco.insert(0, 'missionario')
        else:
            print("Não tem missionarios nesse lado")


def m_sai_barco(barco_posi):
    """
    Missionário sai do barco

    :param barco_posi: Posição que o barco se encontra
    :return: None
    """
    if barco_posi == 1:
        barco.remove('missionario')
        ilha_esq.insert(0, 'missionario')
    else:
        barco.remove('missionario')
        ilha_dir.insert(0, 'missionario')


def c_entra_barco(barco_posi, ilha_esq, ilha_dir):
    """
    Canibal entra no barco

    :param barco_posi: Posição que o barco se encontra
    :param ilha_esq: Lista com os elementos que estão na ilha esquerda
    :param ilha_dir: Lista com os elementos que estão na ilha direita
    :return: None
    """
    if barco_posi == 1:
        # Se não tiver canibais desse lado para entrar no barco
        if ilha_esq.count('canibal') >= 0:
            ilha_esq.remove('canibal')
            barco.insert(0, 'canibal')
        else:
            print("Não tem canibais desse lado")
    else:
        # Se não tiver canibais desse lado para entrar no barco
        if ilha_dir.count('canibal') >= 0:
            ilha_dir.remove('canibal')
            barco.insert(0, 'canibal')
        else:
            print("Não tem canibais desse lado")


def c_sai_barco(barco_posi):
    """
    Canibal sai do barco

    :param barco_posi: Posição que o barco se encontra
    :return: None
    """
    if barco_posi == 1:
        barco.remove('canibal')
        ilha_esq.insert(0, 'canibal')
    else:
        barco.remove('canibal')
        ilha_dir.insert(0, 'canibal')


# Se de um lado houverem mais canibais do que missionários acabou o jogo
def regra1(barco_posi, barco, ilha_esq, ilha_dir):
    """
    Regra para perder se houverem mais canibais que missionarios de um lado

    :param barco_posi: Posição que o barco se encontra
    :param barco: Lista com os elementos que estão no barco
    :param ilha_esq: Lista com os elementos que estão na ilha esquerda
    :param ilha_dir: Lista com os elementos que estão na ilha direita
    :return: Retorna se você perdeu o jogo
    """
    cani_esquerda = ilha_esq.count('canibal')
    missi_esquerda = ilha_esq.count('missionario')
    cani_direita = ilha_dir.count('canibal')
    missi_direita = ilha_dir.count('missionario')

    if barco_posi == 1:
        cani_esquerda = cani_esquerda + barco.count('canibal')
        missi_esquerda = missi_esquerda + barco.count('missionario')
    else:
        cani_direita = cani_direita + barco.count('canibal')
        missi_direita = missi_direita + barco.count('missionario')

    print("Canibais na esquerda ", cani_esquerda,
          "Canibais direita ", cani_direita)
    print("Missionarios esquerda ", missi_esquerda,
          "Missionarios direita ", missi_direita)

    if cani_esquerda > missi_esquerda:
        if missi_esquerda != 0:
            return 'Você perdeu o jogo'
    if cani_direita > missi_direita:
        if missi_direita != 0:
            return 'Você perdeu o jogo'


def get_int_value_with_range(message: str, min_value: int, max_value: int) -> int:
    """
    Valida dados inteiros em um determinado range

    :param message: A mensagem a ser exibida
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna a opção escolhida dentro do range
    """
    while True:
        try:
            # recebe o número da opção escolhida
            op = int(input(message + ": "))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print("Opção inválida: escolha um número de",
                  min_value, "a", max_value)
        else:
            return op


def menu():
    """
    Menu com as opções

    :return: retorna a opção
    """
    print("*** Missionários e Canibais ***")
    print("1. Colocar um canibal no barco")
    print("2. Colocar um missionario no barco")
    print("3. Retirar um canibal do barco")
    print("4. Retirar um missionário do barco")
    print("5. Mover o barco")
    print("***************************************\n")
    return get_int_value_with_range("Digite uma das opções", 1, 5)


def main():
    """
    Ponto de entrada do módulo

    :return: None
    """

    barco_posi = 1
    while True:
        if regra1(barco_posi, barco, ilha_esq, ilha_dir) == 'Você perdeu o jogo':
            print("Você perdeu. Os canibais comeram os missionários.")
            break
        if len(ilha_dir) == 6:  # Se a ilha da direita tiver 6 elementos, você ganha
            print("Você ganhou o jogo")
            break
        else:
            print(f"barco {barco}\n")
            if barco_posi == 1:  # Se o barco está na direita ou esquerda
                print("O barco está na esquerda\n")
            else:
                print("O barco está na direita\n")

            op = menu()
            if op == 1:  # Colocar um canibal no barco
                if len(barco) >= 2:
                    print("Você só pode adicionar 2 pessoas em um barco\n")
                else:
                    c_entra_barco(barco_posi, ilha_esq, ilha_dir)
            elif op == 2:  # Colocar um missionario no barco
                if len(barco) >= 2:
                    print("Você só pode adicionar 2 pessoas em um barco\n")
                else:
                    m_entra_barco(barco_posi, ilha_esq, ilha_dir)
            elif op == 3:  # Retirar um canibal do barco
                if barco.count('canibal') == 0:
                    print("Não tem nenhum canibal no barco\n")
                else:
                    c_sai_barco(barco_posi)
            elif op == 4:  # Retirar um missionário do barco
                if barco.count('missionario') == 0:
                    print("Não tem nenhum missionario no barco\n")
                else:
                    m_sai_barco(barco_posi)
            elif op == 5:  # Mover o barco
                if len(barco) == 0:  # Se o barco estiver vazio ele não anda
                    print("Você não pode mover o barco se ele estiver vazio")
                else:
                    if barco_posi == 1:
                        barco_posi += 1
                    else:
                        barco_posi -= 1


if __name__ == '__main__':
    main()
