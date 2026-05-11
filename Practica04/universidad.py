from datetime import datetime

class Biblioteca():
    class Horario():
        def __init__(self, diasApertura, horaApertura ,horaCierre):
            self.diasApertura = diasApertura
            self.horaApertura = horaApertura
            self.horaCierre = horaCierre

        def mostrarHorario(self):
            print (f"Horario de apertura: {self.diasApertura} de {self.horaApertura} a {self.horaCierre}")
            
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaLibros = []
        self.listaAutores = []
        self.listaPrestamos = []
        self.horario = self.Horario("Lunes a Viernes", "9:00", "18:00")

    def agregarLibro(self, libro):
        self.listaLibros.append(libro)
        if libro.autor not in self.listaAutores:
            self.listaAutores.append(libro.autor)

    def agregarAutor(self, autor):
        self.listaAutores.append(autor)

    def prestarLibro(self ,estudiante , libro):
        nuevoPrest = Prestamo(estudiante ,libro)
        self.listaPrestamos.append(nuevoPrest)
        print(f"Libro '{libro.titulo}' prestado a {estudiante.nombre}.")

    def mostrarEstado(self):
        print(f"\n{'='*10} ESTADO: {self.nombre} {'='*10}")
        self.horario.mostrarHorario()
        print(f"Libros en catálogo: {len(self.listaLibros)}")
        print(f"Autores registrados: {len(self.listaAutores)}")
        print(f"Préstamos activos: {len(self.listaPrestamos)}")

    def cerrarBiblioteca(self):
        print(f"\nCerrando la {self.nombre}")
        self.listaPrestamos.clear()

class Libro():
    def __init__ (self ,titulo ,isbn , contenido, autor):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor 
        self.paginas = [Pagina(i + 1, cont) for i, cont in enumerate(contenido)]

    def leer(self):
        print(f"\nLeyendo Libro: {self.titulo}")
        self.autor.mostrarInfo()
        for p in self.paginas:
            p.mostrarHorario()

class Autor():
    def __init__(self, nombre, nacionalidad):
        self.nombre= nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} , Nacionalidad: {self.nacionalidad}")

class Estudiante():
    def __init__(self, codigoEstudiante, nombre):
        self.codigoEstudiante = codigoEstudiante
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} , Código: {self.codigoEstudiante}")

class Prestamo():
    def __init__(self, estudiante, libro):
        self.fechaPrestamo = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.fechaDevolucion = "Pendiente" 
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(f"Préstamo: {self.libro.titulo} a {self.estudiante.nombre} el {self.fechaPrestamo}")

class Pagina():
    def __init__(self ,numeroPagina ,contenidoPagina):
        self.numeroPagina = numeroPagina
        self.contenidoPagina = contenidoPagina

    def mostrarHorario(self):
        print(f"Página {self.numeroPagina}: {self.contenidoPagina}")

Autor1 = Autor("Franz Tamayo", "Boliviano")
Estu1 = Estudiante("Inf-111","maria de loa angeles")

contenidos = ["Educacion","pedagogia","filosofia"]
libro1 = Libro("Pedagogia", "1234567890", contenidos, Autor1)

miBibli = Biblioteca("Biblioteca Central")

miBibli.agregarLibro(libro1)
miBibli.mostrarEstado()
libro1.leer()
miBibli.cerrarBiblioteca()
miBibli.mostrarEstado()