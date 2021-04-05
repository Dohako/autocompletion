n = int(input())
dictionary = {}
for i in range(n):
    word, count = input().split()
    first_letter = word[0]
    count = int(count)
    if first_letter in dictionary.keys():
        dictionary[first_letter].append([count, word])
        dictionary[first_letter].sort()
    else:
        dictionary.update({first_letter:[[count,word]]})
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
            word_from_dict = dictionary[first_letter][qty-1-i][1]
            if word in word_from_dict:
                print(dictionary[first_letter][qty-1-i][1])
                j += 1
            if j >= 10:
                break