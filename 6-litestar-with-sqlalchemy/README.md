# Tarea Práctica: CRUD de Libros

**Duración:** ~60 minutos

## Objetivo

Implementar un CRUD completo para gestionar **Libros**, siguiendo los mismos patrones que ya están implementados en el repositorio [https://github.com/dialvarezs/learning-litestar-bd2-2025](https://github.com/dialvarezs/learning-litestar-bd2-2025).

## Especificación del Modelo

El modelo `Book` debe tener estos campos:

| Campo            | Tipo     | Restricciones    | Descripción                   |
| ---------------- | -------- | ---------------- | ----------------------------- |
| `id`             | BigInt   | PK, Auto         | Heredado de `BigIntAuditBase` |
| `title`          | String   | Requerido, Único | Título del libro              |
| `author`         | String   | Requerido        | Autor del libro               |
| `isbn`           | String   | Requerido, Único | ISBN del libro                |
| `pages`          | Integer  | Requerido        | Número de páginas             |
| `published_year` | Integer  | Requerido        | Año de publicación            |
| `created_at`     | DateTime | Auto             | Heredado de `BigIntAuditBase` |
| `updated_at`     | DateTime | Auto             | Heredado de `BigIntAuditBase` |

## 1: Modelo

En `app/models.py`, crea la clase `Book` que herede de `BigIntAuditBase`:

- Define `__tablename__ = "books"`
- Usa `Mapped` con `mapped_column` para cada campo
- Aplica las restricciones necesarias (`unique=True` para `title` e `isbn`)

Revisa cómo está implementado `User` como referencia.

## 2: DTOs

En `app/dtos.py`, crea tres DTOs usando `SQLAlchemyDTO`:

**BookReadDTO**: Para respuestas (sin exclusiones)

**BookCreateDTO**: Para crear libros

- Excluye: `id`, `created_at`, `updated_at`

**BookUpdateDTO**: Para actualizar libros, soportando actualizaciones parciales

- Excluye: `id`, `created_at`, `updated_at`

## 3: Repositorio

En `app/repositories.py`, crea:

- Clase `BookRepository` que herede de `SQLAlchemySyncRepository[Book]`
- Define `model_type = Book`
- Función provider `provide_book_repo` con `auto_commit=True`

## 4: Controlador

En `app/controllers.py`, implementa `BookController` con estos endpoints:

| Método | Ruta          | Descripción             |
| ------ | ------------- | ----------------------- |
| GET    | `/books/`     | Listar todos los libros |
| GET    | `/books/{id}` | Obtener un libro por ID |
| POST   | `/books/`     | Crear un nuevo libro    |
| PATCH  | `/books/{id}` | Actualizar un libro     |
| DELETE | `/books/{id}` | Eliminar un libro       |

Configura el controlador con:

- `path = "/books"`
- `return_dto = BookReadDTO`
- `dependencies = {"books_repo": Provide(provide_book_repo)}`
- `exception_handlers` para `NotFoundError` y `DuplicateKeyError`

Implementa los métodos correspondientes siguiendo el patrón de `UserController`.

## 5: Registrar el Controlador

En `app/__init__.py`, importa y agrega `BookController` a la lista de `route_handlers`.

## 6. Rutas personalizadas

1. **Buscar por título parcial**: `GET /books/search?title=...`

   - Retorna libros cuyo título contenga el texto buscado (case-insensitive)

2. **Filtrar por rango de años**: `GET /books/filter?from=1990&to=2000`

   - Retorna libros publicados entre los años especificados

3. **Estadísticas generales**: `GET /books/stats`

   - Retorna: total de libros, promedio de páginas, año más antiguo, año más reciente

4. **Validar año de publicación**:

   - Debe estar entre 1000 y el año actual
   - Retornar error 400 si está fuera de rango

5. **Libros recientes**: `GET /books/recent?limit=10`

   - Retorna los últimos N libros agregados (ordenados por `created_at`)
