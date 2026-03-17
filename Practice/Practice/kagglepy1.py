def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
   
  
    lista = []
    for word in doc_list:
        word1 = word.strip(".?")
        new= word1.split(',')
        for words in new:
            sen = words.split()
            for i in sen:
                i.lower()
                if i.lower() == keyword:
                    lista.append(doc_list.index(word))
                    break
      

    return lista