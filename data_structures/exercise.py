from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}

for i in sentence:

    if i in char_frequency:
        char_frequency[i] += 1
    else:
        char_frequency[i] = 1
pprint(char_frequency, width=1)
# max = ["", 0]

# for key in char_frequency:

#     if char_frequency[key] > max[1]:
#         max[0] = key
#         max[1] = char_frequency[key]
# print(max[0])


char_frequency_sorted = sorted(char_frequency.items(), key= lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0][0])


