# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    words = text.split()
    pig_it_list = []
    pig_it_text = ("")
    for l in words:
        pig_it_word = l[1:] + l[0] + "ay"
        pig_it_list.append(pig_it_word)
        pig_it_text = " ".join(pig_it_list)

    return (pig_it_text)

#is failing the test with punctuation marks
