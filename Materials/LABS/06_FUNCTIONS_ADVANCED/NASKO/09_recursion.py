def palindrome(word,index):
    if index == len(word)// 2:
        #base fo the function  we will stop when we reach the middle index of the word
       return f'{word} is a palindrome'
    
    if word[index] != word[-1  -index]:
        return f'{word} is not a palindrome'

    return  palindrome(word,index + 1)   #each time we call the function the index will increase 

print(palindrome('abcba',0))
print(palindrome('peter',0))