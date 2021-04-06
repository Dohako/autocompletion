n = int(input())
dictionary = {}
for i in range(n):
    word, count = input().split()
    first_letter = word[0]
    count = int(count)
    if first_letter in dictionary.keys():
        if count in dictionary[first_letter].keys():
            dictionary[first_letter][count].append(word)
        else:
            dictionary[first_letter].update({count: [word]})
        if count not in dictionary[first_letter]['all_counts']:
            dictionary[first_letter]['all_counts'].append(count)
    else:
        dictionary.update({first_letter: {count: [word], 'all_counts': [count]}})
for first_letter in dictionary.keys():
    for key in dictionary[first_letter].keys():
        if key == 'all_counts':
            dictionary[first_letter][key].sort(reverse=True)
        else:
            dictionary[first_letter][key].sort()
m = int(input())
last_printed = ''
j = 0
message = ''
all_printed = 0
for i in range(m):
    word = input()
    first_letter = word[0]
    if first_letter in dictionary.keys():
        # j = 0
        if i != 0 and i != m - 1 and all_printed != 0:
            message += 'N2'
            # message += '\n'
            # print()
        if i == m - 1:
            message += "N4"
            # message += '\n'
            # print()
        printed = False
        new_in_m = True
        for counts in dictionary[first_letter]['all_counts']:
            for word_from_dict in dictionary[first_letter][counts]:
                if word in word_from_dict:
                    if new_in_m and i != 0:
                        message += 'N6'
                        # print()
                        new_in_m = False
                    if printed is True:
                        # print()
                        message += 'N'
                        # message += '\n'
                        # last_printed = 'n'
                    # print(word_from_dict, end='')
                    message += word_from_dict
                    # last_printed = ''
                    printed = True
                    j += 1
                if j >= 10:
                    break
            # if j >= 10:
            #     break
    if j != 0 and i != m-1:
        # message += "N3"
        # message += '\n'
        # print()
        pass
    # if m == 1:
    #     message += 'N5'
        # print()
    all_printed = j
    j = 0
print(message, end='')