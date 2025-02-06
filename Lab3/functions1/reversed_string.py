def reverse_words(sentence):
    rsentence = " ".join(sentence.split()[::-1])
    print(rsentence)
sentence = str(input("Enter a sentence: "))
reverse_words(sentence)