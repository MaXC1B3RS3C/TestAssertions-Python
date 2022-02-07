from datetime import datetime


students = [
    {"alumne": "Pepe Botella", "data_naiximent": "10-02-2005"},
    {"alumne": "Rafa Nadal", "data_naiximent": "09-02-2005"},
    {"alumne": "Pedro Pasqua", "data_naiximent": "10-02-2003"},
    {"alumne": "Manolo Mata", "data_naiximent": "09-02-2008"},
    {"alumne": "Juan Gris", "data_naiximent": "10-02-2000"},
    {"alumne": "Maria Debe", "data_naiximent": "10-02-1998"},
]


def ordenar_per_nom_antic():
    def nom(element):
        return element["alumne"]
    students.sort(key=nom)
    return students


# ordenar per nom
def ordenar_per_nom(students):
    # Declare funcio per a retornar dades ordenades basades amb data_naiximent
    return sorted(students, key=lambda element: element['alumne'])


# ordenar per data de naiximent descendent
def ordenar_per_naiximent_antic(students):
    # Declare funcio per a retornar dades ordenades basades amb data_naiximent
    def data_naiximent(element):
        return datetime.strptime(element['data_naiximent'], '%d-%m-%Y')
    students.sort(key=data_naiximent)
    return students


# ordenar per data de naiximent descendent eixemple antic
def ordenar_per_naiximent_vell(students):
    # Declare funcio per a retornar dades ordenades basades amb data_naiximent
    def data_naiximent(element):
        return datetime.strptime(element['data_naiximent'], '%d-%m-%Y')
    students.sort(key=data_naiximent)
    return students


# ordenar per data de naiximent descendent eixemple del profesor
def ordenar_per_naiximent(students):
    # Declare funcio per a retornar dades ordenades basades amb data_naiximent
    students.sort(key=lambda element: element['data_naiximent'])
    return students
