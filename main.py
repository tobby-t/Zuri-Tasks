# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

while True:  
    def find_anagrams(string1, string2):
            # [assignment] Add your code here
        string1= input('Enter a word: ')
        string2= input('Enter another word: ')
        if len(string1)==len(string2):
            return sorted(string1.lower()) == sorted(string2.lower())
        else:
            return False
        
    print(find_anagrams("string1", "string2"))




