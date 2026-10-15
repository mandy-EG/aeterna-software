# Cómo trabajamos en aeterna software

Reglas acordadas por el equipo para mantener este repositorio ordenado y revisable.

La regla de la empresa: **un issue, una rama, un Pull Request.**

## Ramas

Nombramos las ramas con el número del issue y unas palabras cortas, en minúsculas y con guiones:

```text
numero-palabras-cortas
```

Ejemplos: `1-readme-empresa`, `2-reglas-del-equipo`, `5-perfil-mocheche16`.

| Tipo de cambio | Tipo de commit que le pone |
| --- | --- |
| Documentación | `docs` |
| Configuración y mantenimiento | `chore` |
| Funcionalidad nueva | `feat` |
| Corrección de errores | `fix` |

Toda rama nace desde `main`. Nunca se trabaja directamente sobre `main`.

## Commits

Escribimos los commits como `tipo: qué hiciste`, en minúscula y en presente.

| Tipo | Para qué |
| --- | --- |
| `feat` | Funcionalidad nueva |
| `fix` | Corregir un error |
| `docs` | Documentación |
| `chore` | Configuración y mantenimiento |

Ejemplo: `docs: agrega las reglas del equipo`. Evitamos mensajes como `arreglos varios`.

## Revisión de Pull Requests

Quién revisa a quién: la revisión va en cadena, A revisa a B, B revisa a C, y el último revisa a A. En nuestro equipo de dos nos revisamos entre sí.

El ciclo de revisión es siempre este:

1. Quien revisa entra a **Files changed**, compara con lo que pide el issue y deja al menos un comentario pidiendo una mejora, sobre una línea, con el botón **+**.
2. El autor corrige en la misma rama, vuelve a subir y responde el comentario contando qué cambió, y luego da clic en **Resolve conversation**.
3. Quien revisa aprueba con **Review changes → Approve**.

No se aprueba de una: primero el comentario, después la corrección y al final la aprobación.

Qué miramos cuando revisamos:

- ¿El archivo tiene todo lo que pide el issue?
- ¿Los commits siguen la convención `tipo: qué hiciste`?
- ¿Se entiende? ¿Tiene errores de ortografía?
- ¿Solo incluye lo necesario para la tarea, sin archivos generados, pesados ni secretos?

## Cuándo se aprueba un Pull Request

Un Pull Request se aprueba cuando cumplen:

- Tiene al menos la aprobación de 1 revisor, que nunca es su propio autor.
- Nace de una rama creada desde `main`, con el nombre correcto y commits bien escritos.
- La descripción incluye la línea `Closes #numero-del-issue` para que el issue se cierre solo al fusionar.
- Cierra o referencia el issue que lo origina.

Con eso cumplido, el autor fusiona el Pull Request, borra la rama en GitHub y todos actualizamos `main` con `git pull`.

## Cuándo se hace git pull

Solo en dos momentos, y siempre estando en `main`:

1. Antes de crear una rama nueva, para que la rama arranque con lo último del equipo.
2. Después de cada fusión de un Pull Request, porque `main` cambió en GitHub.

Los issues no se traen con `pull`: viven en la página de GitHub, no dentro del repositorio.

## Cómo se cierra un issue

El issue se cierra automáticamente cuando se fusiona el Pull Request que lo resuelve. Para eso, la descripción del Pull Request debe incluir `Closes` seguido de un espacio, el símbolo `#` y el número del issue, todo junto:

```text
Closes #4
```

Si un Pull Request resuelve dos issues, van en líneas separadas:

```text
Closes #3
Closes #5
```

No cerramos los issues a mano con el botón **Close issue**. Si el issue quedó cerrado solo, es la prueba de que el trabajo entró por Pull Request.