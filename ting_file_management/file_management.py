import sys


def txt_importer(path_file):
    if not path_file[-4:] == ".txt":
        error_msg = "Formato inválido"
        sys.stderr.write(error_msg)
        return None

    try:
        with open(path_file, "r") as file:
            news_imported_list = file.read().split("\n")

            return news_imported_list

    except FileNotFoundError:
        error_msg = f"Arquivo {path_file} não encontrado\n"
        sys.stderr.write(error_msg)
