frankenstein_text = "/home/sge-l7/PythonProjects/bookbot/books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as f:
        book_content = f.read()
    return book_content

def count_words(book_content):
    split_book = book_content.split()
    count_words = 0
    for i in split_book:
        count_words += 1
    return count_words

dictionary = {}

def count_each_character(book_content):
    book_into_char = list(book_content)
    for i in book_into_char:
        p = i.lower()
        if p in dictionary:
            dictionary[p] += 1
        else:
            dictionary[p] = 1
    return dictionary

def sort(dictionary):
    list_dic = list(dictionary.items())
    list_dic.sort(reverse=True, key=lambda item: item[1])
    return list_dic

