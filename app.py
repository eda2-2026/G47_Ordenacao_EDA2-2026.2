from flask import Flask, render_template, request, redirect, url_for
from main import bubble_sort, merge_sort
from time import perf_counter

app = Flask(__name__)

despesas = [
    {"descricao": "Almoço estágio", "valor": 36.00},
    {"descricao": "Transporte Mobilidade", "valor": 25.00},
    {"descricao": "Natação", "valor": 99.90},
]


@app.route("/", methods=["GET", "POST"])
def index():
    algoritmo = request.args.get("algoritmo", "merge")

    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        valor_texto = request.form.get("valor", "").strip().replace(",", ".")

        try:
            valor = float(valor_texto)
            if descricao and valor > 0:
                despesas.append({
                    "descricao": descricao,
                    "valor": valor
                })
        except ValueError:
            pass

        return redirect(url_for("index"))

    inicio = perf_counter()

    if algoritmo == "bubble":
        ordenadas = bubble_sort(despesas)
        nome_algoritmo = "Bubble Sort"
    else:
        ordenadas = merge_sort(despesas)
        nome_algoritmo = "Merge Sort"

    tempo = perf_counter() - inicio
    total = sum(despesa["valor"] for despesa in despesas)

    return render_template(
        "index.html",
        despesas=ordenadas,
        total=total,
        algoritmo=algoritmo,
        nome_algoritmo=nome_algoritmo,
        tempo=tempo
    )


if __name__ == "__main__":
    app.run(debug=True)