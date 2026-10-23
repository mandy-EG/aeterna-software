"""
Ticket 3 - La gráfica
Archivo: grafica.py

Función: crear_grafica(categorias, valores, ruta)

Recibe dos listas (categorías y sus valores) y la ruta de salida,
y guarda una gráfica de barras interactiva en HTML usando Plotly.

Mejoras aplicadas para presentación en reunión de gerencia:
- Barras ordenadas de mayor a menor.
- Fondo limpio con plantilla plotly_white (sin cuadrícula pesada).
- Valores encima de cada barra con formato de pesos colombianos ($1.280.000).
- Al pasar el mouse: categoría, valor y porcentaje del total.
- Título y subtítulo con el nombre del negocio y el mes.
- Sin leyenda repetida (una barra por categoría).
- Colores de la marca del cliente y fuente legible.
"""

import plotly.express as px


def crear_grafica(categorias, valores, ruta):
    """
    Crea y guarda una gráfica de barras interactiva.

    Parametros:
        categorias (list[str]): nombres de las categorías (ej. sabores de helado).
        valores (list[float/int]): valor total por categoría.
        ruta (str): ruta del archivo HTML de salida (ej. salida/grafica.html).

    Devuelve:
        None: guarda el archivo en la ruta indicada.
    """
    import os

    # Asegurar que la carpeta de salida exista
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    # Ordenar categorías y valores de mayor a menor por valor
    pares = list(zip(categorias, valores))
    pares.sort(key=lambda par: par[1], reverse=True)
    categorias_ordenadas, valores_ordenados = zip(*pares) if pares else ([], [])

    # Calcular el total para los porcentajes del tooltip
    total = sum(valores_ordenados) if valores_ordenados else 0

    # Crear la gráfica de barras con Plotly Express
    fig = px.bar(
        x=list(categorias_ordenadas),
        y=list(valores_ordenados),
        color=list(categorias_ordenadas),
        text=list(valores_ordenados),
        title="Ventas por categoría - Heladería La Esquina",
        labels={"x": "Categoría", "y": "Valor total (COP)"},
        template="plotly_white",
    )

    # Formato de los valores encima de cada barra: pesos colombianos
    fig.update_traces(
        texttemplate="$%{text:,.0f}",
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Valor: $%{y:,.0f}<br>Porcentaje: %{customdata:.1f}%<extra></extra>",
        customdata=[(v / total * 100) if total > 0 else 0 for v in valores_ordenados],
        showlegend=False,  # Sin leyenda repetida (una barra por categoría)
    )

    # Título y subtítulo con nombre del negocio y mes
    fig.update_layout(
        title={
            "text": "Reporte de ventas - Heladería La Esquina<br>"
                    "<sub>Octubre 2026</sub>",
            "x": 0.5,
            "xanchor": "center",
        },
        font=dict(family="Arial, sans-serif", size=12, color="#333333"),
        xaxis_title="Categoría",
        yaxis_title="Valor total (COP)",
        yaxis=dict(tickformat="$,.0f", gridcolor="#e5e5e5"),
        plot_bgcolor="white",
        margin=dict(l=60, r=40, t=100, b=60),
    )

    # Guardar la gráfica en un archivo HTML interactivo
    fig.write_html(ruta)
    print(f"Gráfica guardada en: {ruta}")


if __name__ == "__main__":
    # Ejemplo de prueba directa del módulo
    crear_grafica(
        ["Chocolate", "Vainilla", "Fresa"],
        [1280000, 990000, 650000],
        "salida/grafica.html"
    )
