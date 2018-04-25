# Store the file path associated with the file (note the backslash may be OS specific) 
file = 'raw_data/paragraph_1.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # print(text)

    # Store all of the text inside a variable called "lines"
   
    text_string = text.read()
    sentences = text_string.split('.')
    sentences_count = len(sentences)
    words_whole = text_string.split(' ')
    words_count = len(words_whole)
    avg_sentence_len = words_count / sentences_count
    letter_count = 0

    for word in words_whole:
        letter_count = letter_count + len(word)
    
    avg_letter_count = letter_count / words_count
    # format(avg_letter_count, '.2f')
    # round(avg_letter_count, 2)
    
    print(type(sentences_count))
    print(type(words_count))

    print("Paragraph Analysis")
    print("-----------------------")
    print("Approximate Word Count: ", words_count)
    print("Approximate Sentence Count: ", sentences_count)
    print("Average Letter Count: ", round(avg_letter_count, 2))
    print("Average Sentence Length: ", round(avg_sentence_len, 2))








    # Print the contents of the text file
   #  print(lines)
    # print(type(lines))
    