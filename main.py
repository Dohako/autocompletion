n = int(input())
dictionary = {}
for i in range(n):
    word, count = input().split()
    first_letter = word[0]
    len_c = len(count)
    if len_c < 10:
        missing = 10 - len_c
        count = '0' * missing + count
    count_word = count + '_' + word
    # count = int(count)
    if first_letter in dictionary.keys():
        # dictionary[first_letter].append([count, word])
        # dictionary[first_letter].append([word,count])
        dictionary[first_letter].append(count_word)
        # dictionary[first_letter].sort()
    else:
        dictionary.update({first_letter: [count_word]})
for first_letter in dictionary.keys():
    dictionary[first_letter].sort(reverse=True)
print(dictionary)
m = int(input())
for i in range(m):
    word = input()
    first_letter = word[0]
    if first_letter in dictionary.keys():
        qty = len(dictionary[first_letter])
        # if qty > 10:
        #     qty = 10
        j = 0
        for i in range(qty):
            word_from_dict = dictionary[first_letter][qty - 1 - i]
            if word in word_from_dict:
                print(dictionary[first_letter][qty - 1 - i].split('_')[1])
                j += 1
            if j >= 10:
                break
