def sort_on(dict):
    return dict["number"]

def open_and_read(file):
    f = open("books/frankenstein.txt", "r")

    contents = f.read().lower()

    return contents

def getLenWords(contents):
    words = contents.split()

    return len(words)

def createDictionary(contents):
    dictionary = {}
    for char in contents:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    return dictionary

def char_dic_to_sort_list(dict):
    list = []

    for dic in dict:
        if dic.isalpha():
            list.append({"char": dic, "number": dict[dic]})

    list.sort(reverse=True, key=sort_on)
    return list

def printReport(len, list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len} words found in the document")

    for char in list:
        print(f"The '{char['char']}' character was found {char['number']} times")

    print("--- End report ---")

def main():
    contents = open_and_read("books/frankenstein.txt")

    len = getLenWords(contents)

    dictionary = createDictionary(contents)

    list = char_dic_to_sort_list(dictionary)

    printReport(len, list)

main()

