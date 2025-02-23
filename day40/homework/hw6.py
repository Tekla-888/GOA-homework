#Abbreviate a Two Word Name
def abbreviate_name(name):

  
    words = name.upper().split()

    if len(words) != 2:

        return "Invalid input. Please provide a two-word name."

    return words[0][0] + "." + words[1][0]

