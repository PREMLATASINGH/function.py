def count_word_frequency(text):
    word_count = {}
    words = text.split()
    
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count   
text = "Hello world! Hello everyone. Welcome to the world of programming."
frequency = count_word_frequency(text)
print(frequency)
print(count_word_frequency("This is a test. This test is only a test."))
print(count_word_frequency("Python is great. Python is easy to learn."))    
