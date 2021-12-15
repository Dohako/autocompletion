n = int(input())
dictionary = {}
for i in range(n):
    word, count = input().split()
    first_letter = word[0]
    # len_c = len(count)
    # if len_c < 10:
    #     missing = 10 - len_c
    #     count = '0' * missing + count
    # count_word = count + '_' + word
    count = int(count)
    if first_letter in dictionary.keys():
        # dictionary[first_letter].append([count, word])
        if count in dictionary[first_letter].keys():
            dictionary[first_letter][count].append(word)
            # dictionary[first_letter]['all_counts'].append(count)
        else:
            dictionary[first_letter].update({count: [word]})
        if count not in dictionary[first_letter]['all_counts']:
            dictionary[first_letter]['all_counts'].append(count)
        # if count in dictionary[first_letter]
        # dictionary[first_letter].append([word,count])
        # dictionary[first_letter].append(count_word)
        # dictionary[first_letter].sort()
    else:
        dictionary.update({first_letter: {count: [word], 'all_counts': [count]}})
        # dictionary.update({first_letter: [[count, [word]]]})
        # dictionary.update({first_letter: [count_word]})
for first_letter in dictionary.keys():
    for key in dictionary[first_letter].keys():
        if key == 'all_counts':
            dictionary[first_letter][key].sort(reverse=True)
        else:
            dictionary[first_letter][key].sort()
# print(dictionary)
# print(len(dictionary['k']))
m = int(input())
last_printed = ''
j = 0
message = ''
for i in range(m):
    word = input()
    first_letter = word[0]

    if i != 0 and last_printed != 'n':
        # print("<- first worked here", end='')
        # print()
        last_printed = 'n'



    # if i == m-1 and last_printed != 'n':
    #     print()
    #     last_printed = 'n'
    # if j != 0 and last_printed != 'n':
    #     print()
    #     last_printed = 'n'
    if first_letter in dictionary.keys():
        j = 0
        if i != 0 and i != m - 1:
            # message += 'N2'
            message += '\n'
        if i == m - 1:
            # message += "N4"
            message += '\n'
        printed = False
        for counts in dictionary[first_letter]['all_counts']:
            for word_from_dict in dictionary[first_letter][counts]:
                if word in word_from_dict:
                    if printed is True:
                        # print()
                        # message += 'N'
                        message += '\n'
                        last_printed = 'n'
                    # print(word_from_dict, end='')
                    message += word_from_dict
                    last_printed = ''
                    printed = True
                    j += 1
                    # if i != m - 1:
                    #     print()
                # print(word_from_dict)
                # j += 1
                if j >= 10:
                    break
            if j >= 10:
                # print()
                break
    if j != 0 and i != m-1:
        # message += "N3"
        message += '\n'
    # if len(message) > 1:
    #     if message[-1] != '\n':
    #         message += '\n'
    # else:
    #     message += '\n'
    if i != m - 1 and j != 0:
        # print("<- third worked here", end='')
        # print()
        pass

    if i != m - 1 and last_printed != 'n' and j != 0:
        # print(f"<- second worked here {i} and {m}", end='')
        # print()
        last_printed = 'n'
    j = 0
print(message, end='')