def word_histogram(paragraph):
    para_list = paragraph.split(" ")
    histo = {}
    for i in para_list:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
            
    return histo
    

# def sort_histogram(histogram):
#     print(max(histogram))

string_in = raw_input("Paragraph: ")
new_histo = word_histogram(string_in)
sorted_list = []

for key in new_histo:
    sorted_list.append([key, new_histo[key]])
sorted_list.sort(key = lambda x: x[1])

print'1: ' + sorted_list[-1][0] + '\n2: ' + sorted_list[-2][0] + '\n3: ' + sorted_list[-3][0]