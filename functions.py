FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """ Procitaj tekst fajl u vrati to-do listu. """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Upisi to-do listu u tekstualni fajl. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


