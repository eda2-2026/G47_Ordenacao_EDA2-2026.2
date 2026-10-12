
import pytest

from main import bubble_sort, merge_sort


@pytest.mark.parametrize("algoritmo", [bubble_sort, merge_sort])
def test_ordena_despesas_em_ordem_crescente(algoritmo):
    despesas = [
        {"descricao": "Livro", "valor": 80.0},
        {"descricao": "Ônibus", "valor": 5.0},
        {"descricao": "Almoço", "valor": 30.0},
    ]

    resultado = algoritmo(despesas)

    assert [d["valor"] for d in resultado] == [5.0, 30.0, 80.0]


@pytest.mark.parametrize("algoritmo", [bubble_sort, merge_sort])
def test_lista_vazia(algoritmo):
    assert algoritmo([]) == []


@pytest.mark.parametrize("algoritmo", [bubble_sort, merge_sort])
def test_lista_com_um_elemento(algoritmo):
    despesas = [{"descricao": "Café", "valor": 7.0}]

    assert algoritmo(despesas) == despesas


@pytest.mark.parametrize("algoritmo", [bubble_sort, merge_sort])
def test_valores_repetidos(algoritmo):
    despesas = [
        {"descricao": "Livro", "valor": 20.0},
        {"descricao": "Caneta", "valor": 5.0},
        {"descricao": "Caderno", "valor": 20.0},
        {"descricao": "Lápis", "valor": 5.0},
    ]

    resultado = algoritmo(despesas)

    assert [d["valor"] for d in resultado] == [5.0, 5.0, 20.0, 20.0]


@pytest.mark.parametrize("algoritmo", [bubble_sort, merge_sort])
def test_lista_ja_ordenada(algoritmo):
    despesas = [
        {"descricao": "A", "valor": 5.0},
        {"descricao": "B", "valor": 10.0},
        {"descricao": "C", "valor": 15.0},
    ]

    resultado = algoritmo(despesas)

    assert [d["valor"] for d in resultado] == [5.0, 10.0, 15.0]


@pytest.mark.parametrize("algoritmo", [bubble_sort, merge_sort])
def test_nao_modifica_lista_original(algoritmo):
    despesas = [
        {"descricao": "Livro", "valor": 80.0},
        {"descricao": "Ônibus", "valor": 5.0},
    ]
    original = [despesa.copy() for despesa in despesas]

    algoritmo(despesas)

    assert despesas == original
