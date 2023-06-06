import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_name_list = [file["nome_do_arquivo"] for file in instance._data]

    if path_file in file_name_list:
        return print(f"Arquivo {path_file} já foi processado.")

    news_imported_list = txt_importer(path_file)
    news_imported_dict = dict(
        nome_do_arquivo=path_file,
        qtd_linhas=len(news_imported_list),
        linhas_do_arquivo=news_imported_list,
    )
    instance.enqueue(news_imported_dict)

    sys.stdout.write(str(news_imported_dict))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    first_out = instance.dequeue()

    sys.stdout.write(
        f"Arquivo {first_out['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
