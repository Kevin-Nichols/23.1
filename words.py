def print_upper_words(words):
    '''This function filters a list of words to display only words that start with the letter e or upper case E and convert them all to uppercase.
            Example - print_upper_words(["Even", "Odd", "everyone", "Evan", "cake"])
                would print -
                EVEN
                EVERYONE
                EVAN
    '''

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())



def print_upper_words2(words, must_start_with):
    """This function filters a list of words to display only words starting with the given letters and converts them all to uppercase.
            Example - print_upper_wordss2(["Kevin", "Michelle", "Michael", "Samantha", "Chris"], must_start_with=["M", "K"])
                would print-
                KEVIN
                MICHELLE
                MICHAEL
    """

    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())