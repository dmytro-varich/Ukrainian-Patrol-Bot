def load_homographs_list(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read() 
    homographs_words = list(content.split(" "))
    return homographs_words


def append_words_to_file(words: list, file_path: str):
    with open(file_path, 'a+', encoding='utf-8') as file:
        words = words
        file.seek(0)
        global_words = [line.strip() for line in file]
        for word in words:
            if word not in global_words:
                file.write(' ' + word)


def remove_words_to_file(word_to_remove: str, file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    words = lines[0].strip().split()
    words = [word for word in words if word != word_to_remove]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(' ' + ' '.join(words))