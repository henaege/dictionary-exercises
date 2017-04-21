def word_histogram(paragraph):
    histo = {}
    for i in word:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
            
    print(histo)