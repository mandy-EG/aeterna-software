# Cómo trabajamos en aeterna software

Reglas acordadas por el equipo para mantener este repositorio ordenado y revisable.

## Ramas

Nombramos las ramas con la convención `tipo/descripcion-breve`, en minúsculas y con guiones.

| Tipo | Para qué |
| --- | --- |
| `docs/` | Documentación |
| `chore/` | Configuración y mantenimiento |
| `feat/` | Funcionalidad nueva |
| `fix/` | Corrección de errores |

Ejemplo: `docs/reglas`, `chore/estructura`, `feat/automatizacion-inventario`.

Toda rama nace desde `main`. Nunca se trabaja directamente sobre `main`.

## Commits

Escribimos los commits como `tipo: qué hiciste`, en minúscula y en presente.

| Tipo | Para qué |
| --- | --- |
| `feat` | Funcionalidad nueva |
| `fix` | Corregir un error |
| `docs` | Documentación |
| `chore` | Configuración y mantenimiento |

Ejemplo: `docs: agrega reglas del equipo`. Evitamos mensajes como `arreglos varios`.

## Revisión de Pull Requests

Quién revisa a quién: un Pull Request lo revisa siempre un integrante distinto al que lo creó. Cada integrante revisa al menos un Pull Request por tarea.

Qué miramos antes de aprobar:

- El título y la descripción resumen el cambio.
- El cambio resuelve el issue que lo origina.
- Solo incluye lo necesario para la tarea (sin cambios ajenos).
- No hay archivos generados, pesados ni secretos (revisamos el `.gitignore`).
- El estilo y la organización siguen lo acordado en este documento.

## Cuándo se aprueba un Pull Request

Un Pull Request se aprueba cuando cumplen:

- Tiene al menos la aprobación de otro integrante (nadie aprueba su propio Pull Request).
- Nace de una rama con la convención y trae al menos un commit bien escrito.
- La rama está al día con `main`.
- Cierra o referencia el issue correspondiente.

Con eso cumplido, el Pull Request se fusiona a `main`.