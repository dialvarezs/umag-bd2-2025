from random import choice, randint

from faker import Faker

from .models import Carrera, Estudiante, Prueba


class GeneradorDatos:
    def __init__(self, n_estudiantes=150) -> None:
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

        # estudiantes
        self.estudiantes = []
        for _ in range(n_estudiantes):
            self._agrega_estudiante()

        # pruebas
        self.pruebas = []
        for _ in range(30):
            self._agrega_prueba()

    def _agrega_estudiante(self):
        self.estudiantes.append(
            Estudiante(
                id=len(self.estudiantes) + 1,
                nombre=self._fake.name(),
                apellido=self._fake.last_name(),
                email=self._fake.email(),
                fecha_ingreso=self._fake.date_between("-1y", "today"),
                fecha_nacimiento=self._fake.date_between("-25y", "-18y"),
                semestre_actual=randint(1, 8),
                carrera=choice(self.carreras),
            )
        )

    def _agrega_prueba(self):
        _id = len(self.pruebas) + 1
        self.pruebas.append(
            Prueba(
                id=_id,
                nombre=f"Prueba {_id}",
                fecha=self._fake.date_between("-1y", "today"),
                materia=choice(self._materias),
                puntaje_maximo=randint(50, 100),
                peso_porcentual=25,
                tipo="prueba",
                calificaciones=[],
            )
        )


def main():
    datos = GeneradorDatos()


if __name__ == "__main__":
    main()
