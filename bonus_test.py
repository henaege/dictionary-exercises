from collections import defaultdict

list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beetles",9]
# conversion = ['one', 'two', 'three', 'four', 'five', 'six']

def list_to_dict(list):
    final_dictionary = {}
    for i in list1:
        if i is True:
            print 'Hello'
        if list1.count(i) == 1:
            final_dictionary.setdefault('one', [])
            if final_dictionary['one'].count(i) == 0:
                final_dictionary['one'].append(i)
        elif list1.count(i) == 2:
            final_dictionary.setdefault('two', [])
            if final_dictionary['two'].count(i) == 0:
                final_dictionary['two'].append(i)
        elif list1.count(i) == 3:
            final_dictionary.setdefault('three', [])
            if final_dictionary['three'].count(i) == 0:
                final_dictionary['three'].append(i)
        elif list1.count(i) == 4:
            final_dictionary.setdefault('four', [])
            if final_dictionary['four'].count(i) == 0:
                final_dictionary['four'].append(i)
        elif list1.count(i) == 5:
            final_dictionary.setdefault('five', [])
            if final_dictionary['five'].count(i) == 0:
                final_dictionary['five'].append(i)
        elif list1.count(i) == 6:
            final_dictionary.setdefault('six', [])
            if final_dictionary['six'].count(i) == 0:
                final_dictionary['six'].append(i)

    return final_dictionary




print(list_to_dict(list1))