from sentence_transformers import SentenceTransformer, util

originfile = open('origin_sentence_withcomma.txt', 'r')
originlist = originfile.read().split('\n')
originfile.close()

blfile = open('T5predicted2.txt', 'r')
bllist = blfile.read().split('\n')
blfile.close()

scorefile = open('T5_similarity.txt', 'w')

sum = 0
max = 0
min = 1

for i in range(0, len(bllist)):
    print(i)
    sentencesanswer = [bllist[i], originlist[i]]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    #Compute embedding for both lists
    embedding_1= model.encode(sentencesanswer[0], convert_to_tensor=True)
    embedding_2 = model.encode(sentencesanswer[1], convert_to_tensor=True)


    if float(util.pytorch_cos_sim(embedding_1, embedding_2))>1:
        print(util.pytorch_cos_sim(embedding_1, embedding_2))
        print(sentencesanswer)
        print(embedding_1)
        print(embedding_2)

    # print(util.pytorch_cos_sim(embedding_1, embedding_2))
    scorefile.write(str(float(util.pytorch_cos_sim(embedding_1, embedding_2))))
    scorefile.write('\n')
    sum+= float(util.pytorch_cos_sim(embedding_1, embedding_2))
    if float(util.pytorch_cos_sim(embedding_1, embedding_2)) > max:
        max = float(util.pytorch_cos_sim(embedding_1, embedding_2))

    if float(util.pytorch_cos_sim(embedding_1, embedding_2)) < min:
        min = float(util.pytorch_cos_sim(embedding_1, embedding_2))


avg = sum/len(bllist)

print('avg:')
print(avg)

print('min:')
print(min)

print('max:')
print(max)

scorefile.close()

    # tensor([[0.7341]])
    # tensor([[0.4868]])
    #bl: avg:0.6188326041806828


#
# avg:
# avg:
# 0.839221195840254
# min:
# 0.5353361368179321
# max:
# 0.9897149801254272


#2



#3
# avg:
# 0.840426908760536
# min:
# 0.5353361368179321
# max:
# 0.9867590665817261