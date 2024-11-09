def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    word_num = count_words(file_contents)
    char_num = sort_characters(count_characters(file_contents))
    print_report(path, word_num, char_num)


def count_words(string):
    return len(string.split())


def sort_dict(d):
    return d["count"]


def sort_characters(characters):
    list = []
    for c in characters:
        list.append({"char": c, "count": characters[c]})
    list.sort(reverse=True, key=sort_dict)

    return list


def count_characters(string):
    string = string.lower()
    characters = {}
    for i in string:
        if i < "a" or i > "z":
            continue
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters


def print_report(book_path, words, characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")
    for c in characters:
        print(c)
#        print(f"The '{c["char"]}' was found {c["count"]} times")
    print("--- End report ---")


main()
