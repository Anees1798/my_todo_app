def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_l:
        todos_l = file_l.readlines()
        return todos_l


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
