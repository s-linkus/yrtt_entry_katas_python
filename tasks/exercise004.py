# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.

import re
import string


def pig_it(text):
    words_list = text.split()
    pig_it_list = []
    pig_it_text = ("")
    for word in words_list:
        if re.match(r"[\w]+[!]", word) is None:
            pig_it_word = word[1:] + word[0] + "ay"
            pig_it_list.append(pig_it_word)
            pig_it_text = " ".join(pig_it_list)
        else:                                                      #not happy about this, but it does the job        
            word1 = word[:-2]                                       
            pig_it_word = word1[1:] + word1[0] + "ay" + word[-2:]
            pig_it_list.append(pig_it_word)
            pig_it_text = " ".join(pig_it_list)

    return (pig_it_text)
