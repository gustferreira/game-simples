from random import randint

class Calcular:
    """
    Uma classe para gerar operações matemáticas aleatórias com base em uma dificuldade fornecida.
    """

    def __init__(self: object, dificuldade: int, /) -> None:
        """
        Inicializa a classe Calcular.

        Args:
            dificuldade (int): Um número que determina a dificuldade das operações geradas.

        Attributes:
            __dificuldade (int): A dificuldade das operações.
            __valor1 (float): O primeiro valor gerado aleatoriamente.
            __valor2 (float): O segundo valor gerado aleatoriamente.
            __operacao (int): O código da operação a ser executada (1 = somar, 2 = diminuir, 3 = multiplicar).
            __resultado (float): O resultado da operação.

        """
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        """
        Obtém a dificuldade atual das operações.

        Returns:
            int: A dificuldade das operações.
        """
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        """
        Obtém o primeiro valor gerado aleatoriamente.

        Returns:
            int: O primeiro valor.
        """
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        """
        Obtém o segundo valor gerado aleatoriamente.

        Returns:
            int: O segundo valor.
        """
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        """
        Obtém o código da operação atual.

        Returns:
            int: O código da operação (1 = somar, 2 = diminuir, 3 = multiplicar).
        """
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        """
        Obtém o resultado da operação.

        Returns:
            int: O resultado da operação.
        """
        return self.__resultado

    def __str__(self: object) -> str:
        """
        Retorna uma representação em string da instância da classe.

        Returns:
            str: Uma representação em string contendo informações sobre os valores, a dificuldade e a operação.
        """
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        """
        Gera um valor aleatório com base na dificuldade definida.

        Returns:
            int: Um valor aleatório com base na dificuldade.
        """
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return  randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:
        """
        Gera o resultado com base na operação especificada.

        Returns:
            int: O resultado da operação.
        """
        if self.operacao == 1:  # somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # diminuir
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        """
        Obtém o símbolo da operação atual.

        Returns:
            str: O símbolo da operação (+, - ou *).
        """
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        """
        Verifica se a resposta fornecida é correta e imprime o resultado da operação.

        Args:
            resposta (int): A resposta fornecida pelo usuário.

        Returns:
            bool: Retorna True se a resposta estiver correta, caso contrário, False.
        """
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        """
        Mostra a operação atual na forma de uma expressão matemática para o usuário.

        Returns:
            None
        """
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
