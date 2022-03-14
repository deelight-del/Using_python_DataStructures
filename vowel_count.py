def vowel_count():
    
    '''Counts small letter vowels in 
    a word and returns the vowels'''
    
    word = input('Enter your word:')    #input the word
    count = 0     #Initiate the count of vowel as zero
    vowel_present = []    #empty list to append vowels found
    vowel = {'a', 'e', 'i', 'o', 'u'}    #set of vowels

    for string in word:
        if string in vowel:
            count= count+1
            vowel_present.append(string)    #Append vowel
    print(f'the number vowel present are: {count}')
    print(f'the unique vowel present are: {set(vowel_present)}')