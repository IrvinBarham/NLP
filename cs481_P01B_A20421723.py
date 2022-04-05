#Irvin Barham
import nltk
nltk.download('brown')
corpus = nltk.corpus.brown

x = input("Please enter a sentence").lower()
print("Now calculating P(" + x + " ) ... ")

# Calculating sentence probability going to split up corpus into bigrams
N = 2
z = corpus.words()
total = 0
corpus_bigram_total = 0
myNgrams = nltk.ngrams(z, N)
userBigram = nltk.ngrams(x.split(), N)

# Finding the occurence of user given sentence in corpus
for user in userBigram:
    print(user)
    for grams in myNgrams:
        if user == grams:
            total += 1

# Finding the total number of bigrams in corpus
myNgrams = nltk.ngrams(z, N)
for grams in myNgrams:
    corpus_bigram_total += 1

p = (total / corpus_bigram_total) * .0625
print("P(" + x + "):", str(p) + "%")

#userBigram = nltk.ngrams(x.split(), N)
#for grams in userBigram:
    #print(grams)

#myNgrams = nltk.ngrams(z, N)
#for grams in myNgrams:
    #print(grams)