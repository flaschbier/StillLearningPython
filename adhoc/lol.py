list_letters = ["A","B","C"]
list_numbers = [1]
list_of_lists = [[list_letters],[list_numbers]]

for letter in list_letters:
    value = "x"
    "Append x to the end of list_numbers that corresponds to letter in list_letters"


"""
First let's fix the obvious syntax errors like missing brackets, string quotes, misspelled variable names and the like:

    list_letters = ["A","B","C"]
    list_numbers = [1]
    list_of_lists = [[list_letters],[list_numbers]]

    for letter in list_letters:
        value = "x"
        "Append x to the end of list_numbers that corresponds to letter in list_letters"

For further questions you might like to consult [this here](http://stackoverflow.com/help/how-to-ask) to to make sure you are asking a well-formed question.

Now to your lists. While you are asking about lists of lists, you are forming lists of lists of lists. See in an interactive shell:

    >>> import lol
    >>> lol.list_of_lists
    [[['A', 'B', 'C']], [[1]]]

I would expect that you rather wanted to put the two lists in another list like so:

    list_of_lists = [list_letters, list_numbers]
"""
