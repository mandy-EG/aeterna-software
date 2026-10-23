# Reporte automático - Heladería La Esquina

## Cliente
**Heladería La Esquina** — local de helados en Itagüí.

## Qué pidió el cliente
Laura Restrepo, Gerente de operaciones, necesita automatizar el reporte del mes. Cada mes reciben un archivo con todos los registros de ventas y lo revisan a mano en Excel: cuentan, suman, separan por categoría y casi siempre se les escapa algún error. Necesitan un programa que:

- Lea el archivo de registros y entregue un reporte con lo principal.
- Muestre cuántos registros hay, cómo se reparten por categoría, cuánto suman.
- Genere una gráfica para mostrar en la reunión de gerencia.
- No se detenga si hay filas incompletas, valores mal escritos o fechas raras; debe separarlas y decir cuántas fueron.
- Permita cambiar fácilmente el nombre del archivo o la columna que se suma, sin abrir el código.

## Cómo ejecutar paso a paso

1. Clonar este repositorio.
2. Dentro de `reporte-automatico/`, instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Generar los datos de ejemplo:

   ```bash
   python generar_datos.py
   ```

   Esto crea `datos/registros.csv` con 100 filas simuladas (incluye 5 filas dañadas a propósito).

4. Ejecutar el reporte:

   ```bash
   python reporte.py
   ```

   Esto lee `datos/registros.csv`, calcula los números, descuenta las filas dañadas y escribe `salida/reporte.md` y `salida/grafica.html`.

5. Abrir `salida/grafica.html` en el navegador para ver la gráfica interactiva.

## Ejemplo de reporte generado

```
# Reporte del mes: Heladería La Esquina
Generado el: 2026-10-23
## Resumen
| Dato | Valor |
|---|---|
| Filas leídas | 105 |
| Registros válidos | 100 |
| Filas descartadas | 5 |
| Valor total | $4.350.000 |
## Por categoría
| Categoría | Registros | Valor |
|---|---|---|
| Chocolate | 32 | $1.280.000 |
| Vainilla | 25 | $990.000 |
## Gráfica
Ver `salida/grafica.html`
```
