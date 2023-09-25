list_of_stop_words = ['C']
string_to_process = ['Python', 'php', 'go', 'C']
split_str = string_to_process
filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))
print("строка без стоп слов: ", filtered_str)