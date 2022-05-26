# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(story):
    # [assignment] Add your code here
    with open('story.txt') as file:
        contents = file.read()
    
    return str(contents)
print(read_file_content('story'))


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict()
    small_text = text.lower()
    no_text = small_text.replace('?', '')
    same_text = no_text.replace('.', '')
    bare_text = same_text.replace(',', '') 
    each_word = bare_text.split()
    
    for word in each_word:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
   
    return count
print (count_words())
