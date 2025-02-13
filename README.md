### Menú interactivo:

El programa tiene un menú interactivo que se muestra en la consola cuando lo ejecutas. Te permite hacer varias cosas:

1. **Crear registros (Create):**
   - Puedes añadir nuevos datos a las tablas. Por ejemplo, si es un sistema de biblioteca, puedes agregar nuevos libros, usuarios o préstamos.

2. **Leer registros (Read):**
   - Puedes ver los datos que ya están en las tablas. Por ejemplo, puedes listar todos los libros disponibles o ver qué libros ha prestado un usuario.

3. **Actualizar registros (Update):**
   - Si hay algún error o quieres cambiar algo, puedes modificar los datos existentes. Por ejemplo, cambiar el correo de un usuario o marcar un libro como devuelto.

4. **Eliminar registros (Delete):**
   - Si ya no necesitas un registro, puedes eliminarlo. Por ejemplo, borrar un usuario que ya no usa el sistema.

5. **Salir:**
   - Cuando termines, puedes salir del programa desde el menú.

---

### Tablas y sus funciones:

La base de datos tiene 3 tablas principales, y cada una tiene una función específica. Aquí te explico para qué sirve cada una:

1. **Tabla "Usuarios":**
   - Esta tabla guarda información sobre los usuarios del sistema.
   - Campos:
     - `id`: Un número único para cada usuario (es la clave primaria).
     - `nombre`: El nombre del usuario.
     - `email`: El correo electrónico del usuario.
     - `fecha_registro`: La fecha en que el usuario se registró en el sistema.
   - **Función:** Sirve para saber quiénes son los usuarios y cuándo se registraron.

2. **Tabla "Libros":**
   - Esta tabla guarda información sobre los libros que hay en la biblioteca.
   - Campos:
     - `id`: Un número único para cada libro (es la clave primaria).
     - `titulo`: El título del libro.
     - `autor`: El autor del libro.
     - `categoria`: La categoría del libro (por ejemplo, novela, ciencia ficción, etc.).
     - `disponible`: Indica si el libro está disponible para prestar (True) o no (False).
   - **Función:** Sirve para saber qué libros hay en la biblioteca y si están disponibles.

3. **Tabla "Préstamos":**
   - Esta tabla registra los préstamos de libros a los usuarios.
   - Campos:
     - `id`: Un número único para cada préstamo (es la clave primaria).
     - `usuario_id`: El ID del usuario que pidió prestado el libro (clave foránea que conecta con la tabla "Usuarios").
     - `libro_id`: El ID del libro que se prestó (clave foránea que conecta con la tabla "Libros").
     - `fecha_prestamo`: La fecha en que se prestó el libro.
     - `fecha_devolucion`: La fecha en que se devolvió el libro (si aún no se devuelve, este campo estará vacío).
   - **Función:** Sirve para saber qué libros ha prestado cada usuario y cuándo los devolvieron (o si aún no los han devuelto).

---

### Relaciones entre tablas:

- La tabla "Préstamos" está conectada con las tablas "Usuarios" y "Libros" a través de las claves foráneas `usuario_id` y `libro_id`. Esto nos permite saber:
  - Qué usuario pidió prestado un libro.
  - Qué libro se prestó.
  - Cuándo se prestó y cuándo se devolvió.
