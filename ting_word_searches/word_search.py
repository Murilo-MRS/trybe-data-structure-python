def exists_word(word, instance):
    word_occurence_count_list = []

    for index in range(len(instance)):
        file_info = instance.search(index)

        lines_location_list = []

        for i, line_content in enumerate(file_info["linhas_do_arquivo"]):
            if word.lower() in line_content.lower():
                lines_location_list.append(dict(linha=i + 1))

        if len(lines_location_list) > 0:
            word_occurence_count_list.append(
                dict(
                    palavra=word,
                    arquivo=file_info["nome_do_arquivo"],
                    ocorrencias=lines_location_list,
                )
            )

    return word_occurence_count_list


def search_by_word(word, instance):
    word_occurence_count_list = []

    for index in range(len(instance)):
        file_info = instance.search(index)

        lines_location_list = []

        for i, line_content in enumerate(file_info["linhas_do_arquivo"]):
            if word.lower() in line_content.lower():
                lines_location_list.append(
                    dict(linha=i + 1, conteudo=line_content)
                )

        if len(lines_location_list) > 0:
            word_occurence_count_list.append(
                dict(
                    palavra=word,
                    arquivo=file_info["nome_do_arquivo"],
                    ocorrencias=lines_location_list,
                )
            )

    return word_occurence_count_list
