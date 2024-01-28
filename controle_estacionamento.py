import datetime

class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.hora_entrada = datetime.datetime.now()
        self.valor = 0
        self.duracao = None

class Estacionamento:
    def __init__(self):
        self.carros = {}
        self.carros_saida = {}
        self.total = 0

    def entrada(self):
        placa = input("Digite a placa do carro: ")
        if placa not in self.carros:
            print("Carro não estacionado no momento, deseja estacionar?")
            resposta = input("Digite 'sim' para estacionar, 'não' para cancelar: ")
            if resposta.lower() == 'sim':
                carro = Carro(placa)
                self.carros[placa] = carro
                print("Carro estacionado com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Carro já estacionado.")

    def saida(self):
        placa = input("Digite a placa do carro: ")
        carro = self.carros.pop(placa, None)
        if carro:
            duracao = datetime.datetime.now() - carro.hora_entrada
            minutos = duracao.seconds // 60
            carro.duracao = f"{minutos} minutos"
            if minutos <= 15:
                valor = 10
            elif minutos <= 20:
                valor = 15
            elif minutos <= 30:
                valor = 20
            elif minutos <= 60:
                valor = 50
            else:
                valor = 70
            self.total += valor
            carro.valor = valor
            self.carros_saida[placa] = carro
            print(f"Carro de placa {placa} saiu. Tempo de estacionamento: {carro.duracao}. Valor a pagar: R$ {valor}")
        else:
            print("Carro não encontrado.")

    def encerrar_plantao(self):
        print("\nResumo do plantão:")
        for placa, carro in self.carros_saida.items():
            print(f"Carro de placa {placa} ficou estacionado por {carro.duracao} e pagou: R$ {carro.valor}")
        print(f"Total de carros: {len(self.carros_saida)}")
        print(f"Valor total do plantão: R$ {self.total}")
        self.carros = {}
        self.carros_saida = {}
        self.total = 0

    def valores(self):
        print("até 15 minutos R$ 10,00")
        print("até 20 minutos R$ 15,00")
        print("até 30 minutos R$ 20,00")
        print("até 60 minutos R$ 50,00")
        print("até 120 minutos R$ 70,00")

    def carros_estacionados(self):
        print("\nCarros estacionados:")
        for placa in self.carros:
            print(f"Carro de placa {placa}")

estacionamento = Estacionamento()

while True:
    print("\n1. Registrar entrada de carro")
    print("2. Registrar saída de carro")
    print("3. Encerrar o plantão")
    print("4. Exibir tabela de valores")
    print("5. Exibir carros estacionados")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        estacionamento.entrada()
    elif opcao == '2':
        estacionamento.saida()
    elif opcao == '3':
        estacionamento.encerrar_plantao()
    elif opcao == '4':
        estacionamento.valores()
    elif opcao == '5':
        estacionamento.carros_estacionados()
    elif opcao == '6':
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
