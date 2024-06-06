def word_count(text):
    return len(text.split())

def character_count(text):
    result = {}
    for character in text.lower():
        if not character.isalpha():
            continue
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

def to_list(dict):
    result = []
    for character, count in dict.items():
        result.append({"character": character, "count": count})
    return result

def sort_on(dict):
    return dict['count']

def main():
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        words = word_count(book_content)
        chars = to_list(character_count(book_content))
        chars.sort(reverse=True, key=sort_on)
        print('--- Begin report of books/frankenstein.txt ---')
        print(f"{words} words found in the document")
        print()
        for item in chars:
            print(f"The '{item['character']}' character was found {item['count']} times")

main()