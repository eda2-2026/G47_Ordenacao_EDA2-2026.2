
def exibir_menu():
    print("\n=== ORGANIZADOR DE DESPESAS ===")
    print("1. Cadastrar gastos")
    print("2. Listar gastos")
    print("3. Ordenar gastos por valor")
    print("4. Mostrar total gasto")
    print("0. Sair")


def main():
    despesas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da despesa: ")

            try:
                valor = float(input("Valor da despesa: R$ "))

                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue

                despesas.append({
                    "descricao": descricao,
                    "valor": valor
                })

                print("Despesa cadastrada com sucesso!")

            except ValueError:
                print("Digite um valor numérico válido.")

        elif opcao == "2":
            if not despesas:
                print("Nenhuma despesa cadastrada.")
            else:
                for despesa in despesas:
                    print(
                        f'{despesa["descricao"]}: '
                        f'R$ {despesa["valor"]:.2f}'
                    )

        elif opcao == "3":
            print("A ordenação será implementada na próxima etapa.")

        elif opcao == "4":
            total = sum(despesa["valor"] for despesa in despesas)
            print(f"Total gasto: R$ {total:.2f}")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
