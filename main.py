# Importing 
from stats import *
import sys  


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    
    return file_content

        
def main():
    # Check if the user provided a file path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     

    book_path = sys.argv[1]   
    string_text = get_book_text(book_path)
    
    print("============ BOOKBOT ============")
    
    print("Analyzing book found")
    
    print("----------- Word Count ----------")  
    text_count = number_of_words(string_text)
    print(f"Found {text_count} total words")
    
    number_character = number_each_time_characters_appear(string_text)
    sorted_dict = take_dict_of_charac_and_return_sorted_list_of_dict(number_character)
    
    print("--------- Character Count -------")
    for i in sorted_dict:     
        print(f"{i['char']}: {i['num']}")



main()