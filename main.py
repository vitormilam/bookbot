# Importing 
from stats import number_of_words, number_each_time_characters_appear


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    
    return file_content

        
def main():
    string_text = get_book_text("books/frankenstein.txt")
    
    text_count = number_of_words(string_text)
    print(f"{text_count} words found in the document")
    
    print(number_each_time_characters_appear(string_text))



main()