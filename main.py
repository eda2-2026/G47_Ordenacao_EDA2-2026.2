
def exibir_menu():
    print("\n===== ORGANIZADOR DE DESPESAS PESSOAIS =====")
    print("1. Cadastrar despesa")
    print("2. Listar despesas")
    print("3. Ordenar despesas por valor (Bubble Sort)")
    print("4. Mostrar total gasto")
    print("0. Sair")


def cadastrar_despesa(despesas):
    descricao = input("Descrição da despesa: ").strip()

    if not descricao:
        print("A descrição não pode ficar vazia.")
        return

    try:
        valor = float(input("Valor da despesa: R$ ").replace(",", "."))

        if valor <= 0:
            print("O valor deve ser maior que zero.")
            return

        despesa = {
            "descricao": descricao,
            "valor": valor
        }

        despesas.append(despesa)
        print("Despesa cadastrada com sucesso!")

    except ValueError:
        print("Valor inválido. Digite um número, como 35.50.")


def listar_despesas(despesas):
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return

    print("\n===== LISTA DE DESPESAS =====")

    for despesa in despesas:
        print(
            f'{despesa["descricao"]}: '
            f'R$ {despesa["valor"]:.2f}'
        )


def bubble_sort(despesas):
    lista_ordenada = despesas.copy()
    tamanho = len(lista_ordenada)

    for i in range(tamanho):
        houve_troca = False

        for j in range(tamanho - i - 1):
            if lista_ordenada[j]["valor"] > lista_ordenada[j + 1]["valor"]:
                lista_ordenada[j], lista_ordenada[j + 1] = (
                    lista_ordenada[j + 1],
                    lista_ordenada[j]
                )
                houve_troca = True

        if not houve_troca:
            break

    return lista_ordenada


def ordenar_despesas(despesas):
    if not despesas:
        print("\nNenhuma despesa cadastrada.")
        return

    despesas_ordenadas = bubble_sort(despesas)

    print("\n===== DESPESAS ORDENADAS POR VALOR =====")

    for despesa in despesas_ordenadas:
        print(
            f'{despesa["descricao"]}: '
            f'R$ {despesa["valor"]:.2f}'
        )


def mostrar_total(despesas):
    total = sum(despesa["valor"] for despesa in despesas)
    print(f"\nTotal gasto: R$ {total:.2f}")


def main():
    despesas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        print(f"\nOpção recebida pelo programa: [{opcao}]")

        if opcao == "1":
            cadastrar_despesa(despesas)

        elif opcao == "2":
            listar_despesas(despesas)

        
        
        elif opcao == "3":
            ordenar_despesas(despesas)
            input("\nPressione Enter para voltar ao menu...")



        elif opcao == "4":
            mostrar_total(despesas)

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
