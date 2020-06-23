# Python lab 6 Assignment Submission
# Sunny Kriplani
# 119220438

import nltk
import string


# This function takes a book name and find the raw text to analyze all textual
# data in form of counts
def analyze(book_name):
    # Finding raw data of book and calculating respective data
    text = nltk.corpus.gutenberg.raw(book_name)
    words = nltk.corpus.gutenberg.words(book_name)
    sentences = (nltk.corpus.gutenberg.sents(book_name))
    ps = nltk.stem.PorterStemmer()
    print("Analysis of " + book_name)
    print("# chars = ", str(len(text)))
    print("# words = ", str(len(words)))
    print("# sentences ", str(len(sentences)))
    ln_word = max(words, key=len)
    print("Longest word = '" + ln_word + "'")
    long = max(sentences, key=len)
    long_len = len(long)
    print("Longest sentence = '", end='')
    print(long[0] + " " + long[1] + " " + long[2] + ". . . " +
          long[long_len-2] + " " + long[long_len-1] +
          "' (" + str(long_len) + " words)")
    stem_lst = {}
    strn = ""
    no_pun = ""
    not_essen = string.punctuation + "0123456789"
    words = list(set(words))        # To make distinct words
    vocab = []
    # vocabulry calculation using by removing punctuations and tokenizing
    for word in words:
        words_new = nltk.tokenize.word_tokenize(word)
        for w in words_new:
            strn += " " + ps.stem(w)
    for char in strn:
        if char not in not_essen:
            no_pun += char
    temp_lst = no_pun.split()
    for x in temp_lst:
        if x not in vocab:
            vocab.append(x)
    print("Vocab size = " + str(len(vocab)))
    # stem calculation based on the stem API
    for w in words:
        lst = []
        stem = ps.stem(w)
        if stem in stem_lst:
            lst = stem_lst[stem]
            lst.append(w)
            stem_lst[stem] = lst
        else:
            lst.append(w)
            stem_lst[stem] = lst
    ln_stem = max(stem_lst, key=lambda k: len(stem_lst[k]))
    print("Largest stem family '" + ln_stem + "':")
    print(stem_lst[ln_stem])
