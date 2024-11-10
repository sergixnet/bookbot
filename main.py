def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lower_text = text.lower()

    result = {}

    for i in range(len(lower_text)):
        character = lower_text[i]

        if not character.isalpha():
            continue

        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    
    return result

def sort_on(dict):
    return dict["num"]

def print_report(words, chars):
    char_list = []

    for key in chars.keys():
        element = { 'name': key, 'num': chars[key] }
        char_list.append(element)
    
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for element in char_list:
        print(f"The '{element['name']}' character was found {element['num']} times")
    
    print("--- End report ---")


def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        book_contents = f.read()
        words = count_words(book_contents)
        chars = count_chars(book_contents)
        print_report(words, chars)

main()