def word_histogram(paragraph):
    para_list = paragraph.split(" ")
    histo = {}
    for i in para_list:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
            
    print(histo)

string_in = raw_input("Paragraph: ")
word_histogram(string_in)