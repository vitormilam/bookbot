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
            