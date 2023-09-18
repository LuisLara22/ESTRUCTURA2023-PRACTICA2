import datetime

# Definición de las clases
class Persona:
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    def guardar(self, gestor):
        gestor.agregar_persona(self)

    def editar(self, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno, nueva_fecha_nacimiento):
        self.nombre = nuevo_nombre
        self.apellido_paterno = nuevo_apellido_paterno
        self.apellido_materno = nuevo_apellido_materno
        self.fecha_nacimiento = nueva_fecha_nacimiento

    def eliminar(self, gestor):
        gestor.eliminar_persona(self)

class Autor(Persona):
    def __init__(self, cod_autor, pais, editorial, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        super().__init__(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

    def __str__(self):
        return super().__str__() + f", Código de Autor: {self.cod_autor}, País: {self.pais}, Editorial: {self.editorial}"

    def guardar(self, gestor):
        gestor.agregar_autor(self)

    def editar(self, nuevo_pais, nueva_editorial):
        self.pais = nuevo_pais
        self.editorial = nueva_editorial

    def eliminar(self, gestor):
        gestor.eliminar_autor(self)

class Categoria:
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

    def guardar(self, gestor):
        gestor.agregar_categoria(self)

    def editar(self, nueva_categoria):
        self.categoria = nueva_categoria

    def eliminar(self, gestor):
        gestor.eliminar_categoria(self)

class Libro:
    def __init__(self, codigo_libro, titulo, tomo):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.tomo = tomo
        self.autores = []  # Lista de autores del libro
        self.categoria = None  # Categoría del libro

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def asignar_categoria(self, categoria):
        self.categoria = categoria

    def guardar(self, gestor):
        gestor.agregar_libro(self)

    def editar(self, nuevo_titulo, nuevo_tomo):
        self.titulo = nuevo_titulo
        self.tomo = nuevo_tomo

    def eliminar(self, gestor):
        gestor.eliminar_libro(self)

class GestorEntidades:
    def __init__(self):
        self.personas = []
        self.autores = []
        self.categorias = []
        self.libros = []

    # Métodos para agregar entidades
    def agregar_persona(self, persona):
        self.personas.append(persona)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Métodos para editar entidades
    def editar_persona(self, cod_persona, nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno, nueva_fecha_nacimiento):
        for persona in self.personas:
            if persona.cod_persona == cod_persona:
                persona.editar(nuevo_nombre, nuevo_apellido_paterno, nuevo_apellido_materno, nueva_fecha_nacimiento)
                print("Persona editada con éxito.")
                break
        else:
            print("Persona no encontrada.")

    def editar_autor(self, cod_autor, nuevo_pais, nueva_editorial):
        for autor in self.autores:
            if autor.cod_autor == cod_autor:
                autor.editar(nuevo_pais, nueva_editorial)
                print("Autor editado con éxito.")
                break
        else:
            print("Autor no encontrado.")

    def editar_categoria(self, cod_categoria, nueva_categoria):
        for categoria in self.categorias:
            if categoria.cod_categoria == cod_categoria:
                categoria.editar(nueva_categoria)
                print("Categoría editada con éxito.")
                break
        else:
            print("Categoría no encontrada.")

    def editar_libro(self, codigo_libro, nuevo_titulo, nuevo_tomo):
        for libro in self.libros:
            if libro.codigo_libro == codigo_libro:
                libro.editar(nuevo_titulo, nuevo_tomo)
                print("Libro editado con éxito.")
                break
        else:
            print("Libro no encontrado.")

    # Métodos para eliminar entidades
    def eliminar_persona(self, persona):
        self.personas.remove(persona)

    def eliminar_autor(self, autor):
        self.autores.remove(autor)

    def eliminar_categoria(self, categoria):
        self.categorias.remove(categoria)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    # Método para generar reporte
    def generar_reporte(self):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"reporte_{fecha_actual}.txt"
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Reporte de Libros\n")
            archivo.write("=========================================\n")
            for libro in self.libros:
                archivo.write(f"Código: {libro.codigo_libro}\n")
                archivo.write(f"Título: {libro.titulo}\n")
                archivo.write(f"Tomo: {libro.tomo}\n")
                archivo.write(f"Categoría: {libro.categoria.categoria if libro.categoria else 'No asignada'}\n")
                archivo.write("Autores:\n")
                for autor in libro.autores:
                    archivo.write(f"- {str(autor)}\n")
                archivo.write("=========================================\n")


# Funciones para mostrar menús
def menu_principal():
    print("Menú Principal")
    print("1. Gestionar Personas")
    print("2. Gestionar Autores")
    print("3. Gestionar Categorías")
    print("4. Gestionar Libros")
    print("5. Generar Reporte")
    print("0. Salir")

def menu_gestionar_personas():
    print("Menú Gestionar Personas")
    print("1. Agregar Persona")
    print("2. Listar Personas")
    print("0. Volver al Menú Principal")

def menu_gestionar_autores():
    print("Menú Gestionar Autores")
    print("1. Agregar Autor")
    print("2. Listar Autores")
    print("0. Volver al Menú Principal")

def menu_gestionar_categorias():
    print("Menú Gestionar Categorías")
    print("1. Agregar Categoría")
    print("2. Listar Categorías")
    print("0. Volver al Menú Principal")

def menu_gestionar_libros():
    print("Menú Gestionar Libros")
    print("1. Agregar Libro")
    print("2. Editar Libro")
    print("3. Eliminar Libro")
    print("0. Volver al Menú Principal")


# Creación del gestor de entidades
gestor = GestorEntidades()

while True:
    menu_principal()
    opcion_principal = input("Selecciona una opción: ")

    if opcion_principal == "1":
        while True:
            menu_gestionar_personas()
            opcion_gestionar_personas = input("Selecciona una opción: ")
            if opcion_gestionar_personas == "1":
                # Agregar Persona
                cod_persona = input("Ingrese el código de la persona: ")
                nombre = input("Ingrese el nombre: ")
                apellido_paterno = input("Ingrese el apellido paterno: ")
                apellido_materno = input("Ingrese el apellido materno: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
                persona = Persona(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                persona.guardar(gestor)
                print("Persona agregada con éxito.")
            elif opcion_gestionar_personas == "2":
                # Listar Personas
                for persona in gestor.personas:
                    print(f"Código: {persona.cod_persona}")
                    print(f"Nombre: {persona.nombre}")
                    print(f"Apellido Paterno: {persona.apellido_paterno}")
                    print(f"Apellido Materno: {persona.apellido_materno}")
                    print(f"Fecha de Nacimiento: {persona.fecha_nacimiento}")
                    print("-----------------------")
            elif opcion_gestionar_personas == "0":
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    elif opcion_principal == "2":
        while True:
            menu_gestionar_autores()
            opcion_gestionar_autores = input("Selecciona una opción: ")
            if opcion_gestionar_autores == "1":
                # Agregar Autor
                cod_autor = input("Ingrese el código del autor: ")
                nombre = input("Ingrese el nombre: ")
                apellido_paterno = input("Ingrese el apellido paterno: ")
                apellido_materno = input("Ingrese el apellido materno: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
                pais = input("Ingrese el país del autor: ")
                editorial = input("Ingrese la editorial: ")
                autor = Autor(cod_autor, pais, editorial, cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
                autor.guardar(gestor)
                print("Autor agregado con éxito.")
            elif opcion_gestionar_autores == "2":
                # Listar Autores
                for autor in gestor.autores:
                    print(f"Código de Autor: {autor.cod_autor}")
                    print(f"Nombre: {autor.nombre}")
                    print(f"Apellido Paterno: {autor.apellido_paterno}")
                    print(f"Apellido Materno: {autor.apellido_materno}")
                    print(f"Fecha de Nacimiento: {autor.fecha_nacimiento}")
                    print(f"País: {autor.pais}")
                    print(f"Editorial: {autor.editorial}")
                    print("-----------------------")
            elif opcion_gestionar_autores == "0":
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    elif opcion_principal == "3":
        while True:
            menu_gestionar_categorias()
            opcion_gestionar_categorias = input("Selecciona una opción: ")
            if opcion_gestionar_categorias == "1":
                # Agregar Categoría
                cod_categoria = input("Ingrese el código de la categoría: ")
                categoria = input("Ingrese el nombre de la categoría: ")
                nueva_categoria = Categoria(cod_categoria, categoria)
                nueva_categoria.guardar(gestor)
                print("Categoría agregada con éxito.")
            elif opcion_gestionar_categorias == "2":
                # Listar Categorías
                for categoria in gestor.categorias:
                    print(f"Código de Categoría: {categoria.cod_categoria}")
                    print(f"Nombre de Categoría: {categoria.categoria}")
                    print("-----------------------")
            elif opcion_gestionar_categorias == "0":
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    elif opcion_principal == "4":
        while True:
            menu_gestionar_libros()
            opcion_gestionar_libros = input("Selecciona una opción: ")
            if opcion_gestionar_libros == "1":
                # Agregar Libro
                codigo_libro = input("Ingrese el código del libro: ")
                titulo = input("Ingrese el título del libro: ")
                tomo = input("Ingrese el tomo del libro: ")
                nuevo_libro = Libro(codigo_libro, titulo, tomo)
                nuevo_libro.guardar(gestor)
                print("Libro agregado con éxito.")
            elif opcion_gestionar_libros == "2":
                # Editar Libro
                codigo_libro = input("Ingrese el código del libro que desea editar: ")
                nuevo_titulo = input("Ingrese el nuevo título del libro: ")
                nuevo_tomo = input("Ingrese el nuevo tomo del libro: ")
                gestor.editar_libro(codigo_libro, nuevo_titulo, nuevo_tomo)
            elif opcion_gestionar_libros == "3":
                # Eliminar Libro
                codigo_libro = input("Ingrese el código del libro que desea eliminar: ")
                for libro in gestor.libros:
                    if libro.codigo_libro == codigo_libro:
                        libro.eliminar(gestor)
                        print("Libro eliminado con éxito.")
                        break
                else:
                    print("Libro no encontrado.")
            elif opcion_gestionar_libros == "0":
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    elif opcion_principal == "5":
        # Generar Reporte
        gestor.generar_reporte()
        print("Reporte generado con éxito.")

    elif opcion_principal == "0":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida del menú principal.")


