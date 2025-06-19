def number_of_words(text):
    spliting_words = text.split()
    text_number_of_words = len(spliting_words)
    
    return text_number_of_words

def number_each_time_characters_appear(text):
    lowered_text = text.lower()
    characters_dict = {}
    
    for character in lowered_text:
        if character not in characters_dict:
            characters_dict[character] = 1
        else:
            characters_dict[character] += 1
        
    return characters_dict


def take_dict_of_charac_and_return_sorted_list_of_dict(dict):
    list_of_dictionaries = []
    
    for key, value in dict.items():
        if key.isalpha():
            new_dict = {f"char": key, "num": value}
            list_of_dictionaries.append(new_dict)
    
    list_of_dictionaries.sort(reverse=True, key=lambda item: item["num"])
    
    return list_of_dictionaries