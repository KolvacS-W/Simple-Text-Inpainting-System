# Writing to a file
wordfile = open('change_words.txt', 'r')
wordlist = wordfile.read().split('\n')
wordfile.close()

finalfile = open('useless.txt', 'w')
changefile = open('changed_words_final.txt', 'w')
originfile = open('origin_sentence_withcomma.txt', 'w')

print(wordlist)
 
# Using readline()
file1 = open('original_sentence.txt', 'r')
sentenlist = file1.read().split('\n')
 
for i in range(0, len(sentenlist)):
    line = sentenlist[i]
    changewd = wordlist[i].split(',')[0]
    newwd = wordlist[i].split(',')[1]
    # print(changewd)
    # print(newwd)
    if ',' in line:
        originfile.write(line)
        originfile.write('\n')
    
        linelist = line.split(',')

        for semiline in linelist:

            if changewd in semiline:
                newsemiline = semiline.replace(changewd, newwd)
                print(newsemiline)
                finalfile.writelines([newsemiline])
                changefile.write(changewd+' -> '+newwd)
                changefile.write('\n')

            else:
                finalfile.write('____')
            
            if linelist[0] == semiline:
                finalfile.write(', ')
            else:
                finalfile.write('.')
        finalfile.write('\n')    

file1.close()
finalfile.close()
originfile.close()
# file1 = open('myfile.txt', 'w')
# file1.writelines((L))
# file1.close()

