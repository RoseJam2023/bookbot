def main():
    try:
        with open("books/frankenstein.txt", encoding="utf-8") as f:
            print("File opened successfully")
            file_contents = f.read()
            print(file_contents)
        count = word_count(file_contents)
        characters = character_count(file_contents)
        sorted_dictionary = sort_dictionary(characters)
        
        create_report(count, sorted_dictionary)
    except FileNotFoundError:
        print("File not found. Please check the path.")

def word_count(file_contents):
    word_count = 0
    
    for word in file_contents.split():
        word_count += 1
    
    return word_count

def character_count(file_contents):

    character_count = {
        "a": 0,"b": 0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,
        "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,
    }
    for char in file_contents:
        lowered_char = char.lower()
        if lowered_char not in character_count and lowered_char.isalpha() == True:
            character_count[lowered_char] = 1

        if lowered_char in character_count:
            character_count[lowered_char] += 1

    return character_count

def sort_on(unsorted_list):
    return unsorted_list['Value']

def sort_dictionary(unsorted_dictionary):
    dictionary_list = []

    for character in unsorted_dictionary:
        value = unsorted_dictionary[character]
        temp_dict = dict([('Character', character), ('Value', value)])
        dictionary_list.append(temp_dict)

    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
    


def create_report(word_count, dictionary_list):
    print("--- Begining document report ---")
    print(f"There are {word_count} words found in the document\n")

    for i in range(0, len(dictionary_list)):
        dictionary_char = dictionary_list[i]['Character']
        dictionary_value = dictionary_list[i]['Value']

        print(f"The '{dictionary_char}' character was found {dictionary_value} times")

    print("--- End of Report ---")


main()
