from random import choice, randint

from faker import Faker

from lib.models import Carrera, Estudiante, Prueba


class GeneradorDatos:
    """Genera datos de ejemplo de carreras, estudiantes y pruebas.

    Esta clase inicializa colecciones con información realista usando Faker.

    Attributes:
        carreras (list[Carrera]): Catálogo base de carreras.
        estudiantes (list[Estudiante]): Conjunto de estudiantes generados.
        pruebas (list[Prueba]): Conjunto de pruebas generadas.
        calificaciones (list[Calificacion]): Lista de calificaciones generadas.
        _materias (list[str]): Lista de nombres de asignaturas disponibles.
        _fake (Faker): Generador de datos configurado para ``es_CL``.
    """

    def __init__(self, n_estudiantes=150, n_pruebas=30) -> None:
        """Inicializa el generador y crea datos de ejemplo.

        Args:
            n_estudiantes (int): Cantidad de estudiantes a generar.
            n_pruebas (int): Cantidad de pruebas a generar.

        Returns:
            None
        """
        self._fake = Faker("es_CL")

        # carreras
        self.carreras = [
            Carrera("ING001", "Ingeniería en Computación", "Ingeniería", 8),
            Carrera("ING002", "Ingeniería Química", "Ingeniería", 8),
            Carrera("SAL001", "Medicina", "Salud", 10),
            Carrera("HUM010", "Pedagogía en Historia", "Humanidades", 8),
            Carrera("ING007", "Arquitectura", "Ingeniería", 10),
        ]

        # materias
        self._materias = [
            "Matemáticas I",
            "Matemáticas II",
            "Física",
            "Base de Datos II",
            "Taller de comunicaciones",
            "Ingeniería y Sociedad",
            "Proyecto I",
            "Electivo II",
        ]

        self.estudiantes = []
        self.pruebas = []
        self.calificaciones = []

        self._genera_estudiantes(n_estudiantes)
        self._genera_pruebas(n_pruebas)

    def _genera_estudiantes(self, n_estudiantes: int) -> None:
        """Genera y agrega múltiples estudiantes de una sola vez.

        Args:
            n_estudiantes (int): Cantidad de estudiantes a generar (>= 0).

        Returns:
            None
        """
        for _ in range(n_estudiantes):
            self.estudiantes.append(
                Estudiante(
                    id=len(self.estudiantes) + 1,
                    nombre=self._fake.name(),
                    apellido=self._fake.last_name(),
                    email=self._fake.email(),
                    fecha_ingreso=self._fake.date_between("-3y", "-1y"),
                    fecha_nacimiento=self._fake.date_between("-25y", "-18y"),
                    semestre_actual=randint(1, 8),
                    carrera=choice(self.carreras),
                )
            )

    def _genera_pruebas(self, n_pruebas: int) -> None:
        """Genera y agrega múltiples pruebas de una sola vez.

        Args:
            n_pruebas (int): Cantidad de pruebas a generar (>= 0).

        Returns:
            None
        """
        for _ in range(n_pruebas):
            _id = len(self.pruebas) + 1
            self.pruebas.append(
                Prueba(
                    id=_id,
                    nombre=f"Prueba {_id}",
                    fecha=self._fake.date_between("-1y", "today"),
                    materia=choice(self._materias),
                    puntaje_maximo=randint(50, 100),
                    calificaciones=[],
                )
            )


def main():
    GeneradorDatos()


if __name__ == "__main__":
    main()
