# 1.
def analizar_ventas(ventas_mensuales):
    """Analiza las ventas mensuales y determina el total por mes y el mejor mes.

    Args:
        ventas_mensuales: Diccionario con las ventas mensuales

    Returns:
        Resumen de ventas por mes y el mejor mes
    """
    total_mes = {mes: sum(ventas) for mes, ventas in ventas_mensuales.items()}
    mejor_mes = max(total_mes.items(), key=lambda x: x[1])

    return {"total_por_mes": total_mes, "mejor_mes": mejor_mes[0]}


# 2.
def crear_perfil(nombre, edad, altura, es_estudiante):
    """Crea un perfil de usuario.

    Args:
        nombre: el nombre del usuario
        edad: la edad del usuario
        altura: la altura del usuario
        es_estudiante: indica si el usuario es estudiante

    Returns:
        str: Resumen del perfil del usuario
    """
    return f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}, Estudiante: {es_estudiante}"


# 3.
def analizar_productos(productos):
    """Analiza una lista de productos y devuelve información sobre ellos.

    Args:
        productos: lista de diccionarios con información de productos

    Returns:
        dict: Resumen del análisis de productos
    """
    total_precio = sum(prod["precio"] for prod in productos)
    promedio_precio = total_precio / len(productos) if productos else 0
    producto_mas_caro = max(productos, key=lambda x: x["precio"], default={})

    return {"precio_promedio": promedio_precio, "producto_mas_caro": producto_mas_caro}


# 4.
def contar_hasta(limite, parar_en):
    """Imprime números del 1 hasta límite, pero se detiene si encuentra parar_en.

    Args:
        limite: el número límite hasta donde contar
        parar_en: el número donde detenerse si se encuentra

    Returns:
        None (solo imprime)
    """
    for i in range(1, limite + 1):
        if i == parar_en:
            print(f"Detenido en {parar_en}")
            break
        print(i)


# 5.
def calcular_total_compra(lista_compras):
    """Calcula el costo total de una lista de compras.

    Args:
        lista_compras: lista de diccionarios con productos

    Returns:
        float: el costo total de la compra
    """
    return sum(producto["precio"] for producto in lista_compras)


def agregar_producto(lista, nombre, precio):
    """Agrega un producto a la lista de compras.

    Args:
        lista: lista de productos
        nombre: nombre del producto
        precio: precio del producto

    Returns:
        None (modifica la lista directamente)
    """
    lista.append({"nombre": nombre, "precio": precio})


# 6.
def limpiar_nombres(nombres):
    """Limpia una lista de nombres y cuenta cuántos tienen más de una palabra.

    Args:
        nombres: lista de nombres

    Returns:
        dict: nombres limpios y conteo de nombres con múltiples palabras
    """
    nombres_limpios = []
    nombres_multiples = 0

    for nombre in nombres:
        nombre_limpio = nombre.strip().title()
        nombres_limpios.append(nombre_limpio)
        if len(nombre_limpio.split()) > 1:
            nombres_multiples += 1

    return {"nombres_limpios": nombres_limpios, "multiples_palabras": nombres_multiples}


# 7.
def crear_libro(titulo, autor, año, paginas):
    """Crea un diccionario con información de un libro.

    Args:
        titulo: título del libro
        autor: autor del libro
        año: año de publicación
        paginas: número de páginas

    Returns:
        dict: información del libro
    """
    return {"titulo": titulo, "autor": autor, "año": año, "paginas": paginas}


def mostrar_libro(libro):
    """Muestra la información de un libro de forma ordenada.

    Args:
        libro: diccionario con información del libro

    Returns:
        None (solo imprime)
    """
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Año: {libro['año']}")
    print(f"Páginas: {libro['paginas']}")


# 8.
def filtrar_numeros(lista_numeros):
    """Filtra números en pares, cuadrados de impares y divisibles por 3.

    Args:
        lista_numeros: lista de números del 1 al 20

    Returns:
        dict: diccionario con las tres listas filtradas
    """
    pares = [n for n in lista_numeros if n % 2 == 0]
    cuadrados_impares = [n**2 for n in lista_numeros if n % 2 != 0]
    divisibles_3 = [n for n in lista_numeros if n % 3 == 0]

    return {"pares": pares, "cuadrados_impares": cuadrados_impares, "divisibles_3": divisibles_3}


# 9.
def comparar_temperaturas(temperaturas):
    """Compara temperaturas entre ciudades y analiza promedios y variación.

    Args:
        temperaturas: diccionario con temperaturas por ciudad

    Returns:
        dict: ciudad con mayor promedio y mayor variación
    """
    import statistics

    promedios = {}
    variaciones = {}

    for ciudad, temps in temperaturas.items():
        promedios[ciudad] = sum(temps) / len(temps)
        variaciones[ciudad] = statistics.stdev(temps)

    ciudad_mayor_promedio = max(promedios.items(), key=lambda x: x[1])[0]
    ciudad_mayor_variacion = max(variaciones.items(), key=lambda x: x[1])[0]

    return {"mayor_promedio": ciudad_mayor_promedio, "mayor_variacion": ciudad_mayor_variacion}


# 10.
def evaluar_nota(nota):
    """Evalúa una nota y determina si está aprobado, reprobado o con distinción.

    Args:
        nota: nota entre 1.0 y 7.0

    Returns:
        str: resultado de la evaluación
    """
    if nota >= 6.0:
        return "Aprobado con distinción"
    elif nota >= 4.0:
        return "Aprobado"
    else:
        return "Reprobado"


# 11.
def calcular_gasto_promedio(gastos):
    """Calcula el promedio de una lista de gastos.

    Args:
        gastos: lista de gastos diarios

    Returns:
        float: promedio de los gastos
    """
    return sum(gastos) / len(gastos) if gastos else 0


def analizar_gastos_semanales(semanas):
    """Analiza gastos de múltiples semanas usando la función de promedio.

    Args:
        semanas: diccionario con gastos por semana

    Returns:
        dict: promedios por semana
    """
    return {semana: calcular_gasto_promedio(gastos) for semana, gastos in semanas.items()}


# 12.
def obtener_primera_y_ultima(frutas):
    """Obtiene la primera y última fruta de una lista.

    Args:
        frutas: lista de frutas

    Returns:
        tuple: primera y última fruta
    """
    if not frutas:
        return None, None
    return frutas[0], frutas[-1]


def agregar_fruta(frutas, nueva_fruta):
    """Agrega una fruta a la lista.

    Args:
        frutas: lista de frutas
        nueva_fruta: fruta a agregar

    Returns:
        None (modifica la lista directamente)
    """
    frutas.append(nueva_fruta)


def mostrar_frutas(frutas):
    """Muestra todas las frutas de la lista.

    Args:
        frutas: lista de frutas

    Returns:
        None (solo imprime)
    """
    for i, fruta in enumerate(frutas, 1):
        print(f"{i}. {fruta}")


# 13.
def calcular_puntos(partidos):
    """Calcula puntos totales basado en resultados de partidos.

    Args:
        partidos: lista de diccionarios con información de partidos

    Returns:
        int: puntos totales
    """
    puntos = 0
    for partido in partidos:
        goles_favor = partido["goles_favor"]
        goles_contra = partido["goles_contra"]

        if goles_favor > goles_contra:
            puntos += 3  # Victoria
        elif goles_favor == goles_contra:
            puntos += 1  # Empate
        # Derrota = 0 puntos

    return puntos


def goles_totales(partidos):
    """Calcula goles totales a favor y en contra.

    Args:
        partidos: lista de diccionarios con información de partidos

    Returns:
        dict: goles a favor y en contra
    """
    goles_favor = sum(partido["goles_favor"] for partido in partidos)
    goles_contra = sum(partido["goles_contra"] for partido in partidos)

    return {"goles_favor": goles_favor, "goles_contra": goles_contra}


def mejor_resultado(partidos):
    """Encuentra el mejor resultado (mayor diferencia de goles).

    Args:
        partidos: lista de diccionarios con información de partidos

    Returns:
        dict: partido con mejor resultado
    """
    mejor_partido = max(partidos, key=lambda x: x["goles_favor"] - x["goles_contra"])
    return mejor_partido


# 14.
def procesar_mensajes(mensajes):
    """Procesa mensajes de log y cuenta errores.

    Args:
        mensajes: lista de strings con mensajes de log

    Returns:
        dict: mensajes procesados y conteo de errores
    """
    mensajes_procesados = []
    errores = 0

    for mensaje in mensajes:
        partes = mensaje.split(" ", 2)
        fecha = partes[0]
        hora = partes[1]
        descripcion = partes[2]

        mensajes_procesados.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})

        if "Error" in descripcion or "error" in descripcion:
            errores += 1

    return {"mensajes": mensajes_procesados, "errores": errores}


# 15.
def analizar_texto(texto):
    """Analiza un texto y retorna estadísticas de palabras.

    Args:
        texto: string de texto a analizar

    Returns:
        dict: estadísticas del texto
    """
    palabras = texto.replace(".", "").replace(",", "").split()
    palabras_unicas = set(palabras)
    palabra_mas_larga = max(palabras, key=len) if palabras else ""

    return {
        "total_palabras": len(palabras),
        "palabras_unicas": len(palabras_unicas),
        "palabra_mas_larga": palabra_mas_larga,
    }
