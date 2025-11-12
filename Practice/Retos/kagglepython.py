import re 
def multi_word_search(doc_list, keywords):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville","casino"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
   
    words_dict = {}
    
    for key in keywords:
        lista = []
        for word in doc_list:
            new= []
            new.append(re.sub(r"[!?.',]","",word))
            for words in new:
                sen = words.split()
                for i in sen:
                    if i.lower() == key:
                        lista.append(doc_list.index(word))
                        break
                    

        words_dict[key]=lista 
    
    return words_dict

    

doc_list = ['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?', "He bought a casino. A casino! That's crazy."]
keywords = ["casino"]


print(multi_word_search(doc_list, keywords))

