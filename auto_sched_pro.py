import random
import os  # Mantive a importação de 'os' porque a função 'clear_screen' usa 'os'

nomes = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hank", "Ivy", "Jack",
         "Karen", "Leo", "Mia", "Nathan", "Olivia", "Paul", "Quinn", "Ryan", "Sophia", "Tom"]

cargos = ["Atendente", "Cozinheiro", "Caixa", "Gerente", "Garçom", "Auxiliar"]

# Mapeamento das folgas fixas por cargo
folgas_fixas = {
    "Atendente": "Segunda",
    "Cozinheiro": "Terça",
    "Caixa": "Quarta",
    "Gerente": "Quinta",
    "Garçom": "Sexta",
    "Auxiliar": "Sexta"
}

num_funcionarios = 20
senha_gerente_padrao = "password123"
tentativas_senha_gerente = 3


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_employee_data():
    # Gera dados aleatórios para os funcionários
    funcionarios = []
    for nome in nomes[:num_funcionarios]:
        cargo = random.choice(cargos)
        turno = random.choice(["Abertura", "Intermediário", "Fechamento"])
        folga_fixa = folgas_fixas[cargo]
        folga_extra_domingo = distribute_folgas(nome, cargo, folga_fixa)

        funcionario = {
            'Nome': nome,
            'Cargo': cargo,
            'Folga': folga_fixa,
            'Turno': turno,
            'Folga_Extra_Domingo': folga_extra_domingo
        }

        funcionarios.append(funcionario)

    return funcionarios


def distribute_folgas(nome, cargo, folga_fixa):
    # Distribui as folgas extras nos quatro domingos com base no cargo e folga fixa
    if folga_fixa == "Segunda":
        return "Primeiro Domingo"
    elif folga_fixa == "Terça":
        return "Segundo Domingo"
    elif folga_fixa == "Quarta":
        return "Terceiro Domingo"
    elif folga_fixa == "Quinta":
        return "Quarto Domingo"
    else:
        return "Primeiro Domingo"


def print_employee_table(funcionarios):
    # Imprime uma tabela com os dados dos funcionários
    print("\n{:<15} {:<15} {:<15} {:<15} {:<20}".format("Nome", "Cargo", "Folga", "Turno", "Folga Extra Domingo"))
    for funcionario in funcionarios:
        print("{:<15} {:<15} {:<15} {:<15} {:<20}".format(funcionario['Nome'], funcionario['Cargo'],
                                                            funcionario['Folga'], funcionario['Turno'],
                                                            funcionario['Folga_Extra_Domingo']))


def alterar_funcionario(funcionario):
    # Permite ao gerente alterar dados de um funcionário específico
    print(f"\nAlterando dados para o funcionário {funcionario['Nome']}:\n")
    print_employee_info(funcionario)

    try:
        novo_cargo = input("Novo cargo: ")
        novo_turno = input("Novo turno: ")
        nova_folga = input("Nova folga: ")
        nova_folga_extra_domingo = input("Nova folga extra de domingo do mês: ")

        funcionario['Cargo'] = novo_cargo
        funcionario['Turno'] = novo_turno
        funcionario['Folga'] = nova_folga
        funcionario['Folga_Extra_Domingo'] = nova_folga_extra_domingo

        print("\nAlterações aplicadas com sucesso!\n")
    except Exception as e:
        print(f"Erro: {e}")
        print("Não foi possível realizar a alteração.")


def print_employee_info(funcionario):
    # Imprime informações específicas de um funcionário
    print("{:<15} {:<15} {:<15} {:<15} {:<20}".format("Nome", "Cargo", "Folga", "Turno", "Folga Extra Domingo"))
    print("{:<15} {:<15} {:<15} {:<15} {:<20}".format(funcionario['Nome'], funcionario['Cargo'],
                                                        funcionario['Folga'], funcionario['Turno'],
                                                        funcionario['Folga_Extra_Domingo']))


def verificar_senha_gerente():
    # Verifica a senha do gerente antes de permitir o acesso
    tentativas = 0
    while tentativas < tentativas_senha_gerente:
        senha_inserida = input("Insira a senha de gerente para continuar (padrão: password123): ")
        if senha_inserida == senha_gerente_padrao:
            return True
        else:
            tentativas += 1
            print(f"Senha incorreta. Tentativas restantes: {tentativas_senha_gerente - tentativas}")

    print("Número máximo de tentativas excedido. Encerrando o programa.")
    return False


def adicionar_funcionario(funcionarios):
    # Adiciona um novo funcionário com informações fornecidas pelo gerente
    nome_novo_funcionario = input("\nDigite o nome do novo funcionário: ")
    cargo_novo_funcionario = input("Digite o cargo do novo funcionário: ")
    turno_novo_funcionario = input("Digite o turno do novo funcionário (Abertura/Intermediário/Fechamento): ")
    folga_fixa_novo_funcionario = input("Digite a folga fixa do novo funcionário: ")
    folga_extra_domingo_novo_funcionario = input("Digite a folga extra no domingo do novo funcionário: ")

    novo_funcionario = {
        'Nome': nome_novo_funcionario,
        'Cargo': cargo_novo_funcionario,
        'Folga': folga_fixa_novo_funcionario,
        'Turno': turno_novo_funcionario,
        'Folga_Extra_Domingo': folga_extra_domingo_novo_funcionario
    }

    funcionarios.append(novo_funcionario)
    print(f"\nNovo funcionário {nome_novo_funcionario} adicionado com sucesso!\n")
    print_employee_table(funcionarios)


def remover_funcionario(funcionarios):
    # Remove um funcionário da lista
    print_employee_table(funcionarios)
    nome_funcionario_remover = input("\nDigite o nome do funcionário que deseja remover (ou 'sair' para cancelar): ")

    if nome_funcionario_remover.lower() != 'sair':
        for funcionario in funcionarios:
            if funcionario['Nome'].lower() == nome_funcionario_remover.lower():
                funcionarios.remove(funcionario)
                print(f"\nFuncionário {nome_funcionario_remover} removido com sucesso!\n")
                print_employee_table(funcionarios)
                return

        print(f"\nFuncionário {nome_funcionario_remover} não encontrado. Nenhum funcionário removido.\n")


def main():
    if verificar_senha_gerente():
        print("\nBem-vindo ao Sistema de Organização de Escala de Funcionários\n")

        funcionarios = generate_employee_data()

        while True:
            clear_screen()
            print("Menu:")
            print("1. Iniciar o processo de organização do mês atual")
            print("2. Alterar dados de funcionário")
            print("3. Adicionar ou Remover Funcionário")
            print("4. Sair")

            opcao = input("Escolha uma opção (1, 2, 3 ou 4): ")

            if opcao == '1':
                clear_screen()
                print_employee_table(funcionarios)

                satisfaction = input("\nO gerente está satisfeito com a distribuição de folgas no domingo? (Digite 'sim' ou 'nao'): ").lower()

                if satisfaction.lower() == 'nao':
                    while True:
                        for funcionario in funcionarios:
                            folga_extra_domingo_options = ["Segundo Domingo", "Terceiro Domingo", "Quarto Domingo", "Primeiro Domingo"]
                            funcionario['Folga_Extra_Domingo'] = random.choice(folga_extra_domingo_options)

                        print("\nProcesso de reorganização concluído.")
                        print_employee_table(funcionarios)

                        satisfaction_new = input("\nO gerente está satisfeito com esta nova distribuição de folgas no domingo? (Digite 'sim' ou 'nao'): ").lower()

                        if satisfaction_new == 'sim':
                            break
                        else:
                            clear_screen()

                print("\nProcesso de organização concluído.")
            elif opcao == '2':
                clear_screen()
                print_employee_table(funcionarios)
                while True:
                    nome_funcionario = input("\nDigite o nome do funcionário que deseja alterar (ou 'sair' para sair): ")
                    if nome_funcionario.lower() == 'sair':
                        break
                    else:
                        funcionario_encontrado = False
                        for funcionario in funcionarios:
                            if funcionario['Nome'].lower() == nome_funcionario.lower():
                                alterar_funcionario(funcionario)
                                print_employee_table(funcionarios)
                                funcionario_encontrado = True
                                break

                        if not funcionario_encontrado:
                            print(f"\nFuncionário {nome_funcionario} não encontrado. Tente novamente.\n")
            elif opcao == '3':
                clear_screen()
                print("Opções de Adicionar ou Remover Funcionário:")
                print("1. Adicionar Funcionário")
                print("2. Remover Funcionário")
                print("3. Voltar ao Menu Principal")

                opcao_adicionar_remover = input("Escolha uma opção (1, 2 ou 3): ")

                if opcao_adicionar_remover == '1':
                    adicionar_funcionario(funcionarios)
                elif opcao_adicionar_remover == '2':
                    print_employee_table(funcionarios)
                    remover_funcionario(funcionarios)
                elif opcao_adicionar_remover == '3':
                    pass  # Volta ao menu principal
                else:
                    print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")
            elif opcao == '4':
                print("\nSaindo do programa. Até logo!")
                break
            else:
                print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
