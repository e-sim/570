# Erica Sim
# Ling 570 Autumn 2017
# hw4

import sys

#making an FST (in Carmel format) for the lexicon
LEXICON = open(sys.argv[1], "r")
#LEXICON = open("lexicon_ex", "r")

# prints first line of output FST
print("q99")
st_counter = 0

for line in LEXICON:
    if line == "\n":
        continue

    word = line.split()[0]
    pos_tag = line.split()[1]

    for letter in word:
        if len(word) == 1:
            print('(q0 (q99 "' + letter + '" ' + pos_tag + '))')
           # print("(F (q0 *e*))")

        elif letter is word[0]:
            print('(q0 (q' + str(st_counter + 1) + ' "' + letter + '" *e*))')

        #last letter
        elif letter is word[len(word)-1]:
            print('(q' + str(st_counter) + ' (q99 "' + letter + '" ' + pos_tag + '))')

        else:
            print('(q' + str(st_counter) + ' (q' + str(st_counter + 1) + ' "' + letter + '" *e*))')

        st_counter += 1

print("(q99 (q0 *e*))")
