import nltk
from nltk.util import ngrams
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import Counter, defaultdict

# Irvin Barham A20421723

# Downloading corpus WEBTEXT is my choice

nltk.download('brown')
nltk.download('reuters')
nltk.download('webtext')

#corpus = nltk.corpus.brown
#corpus = nltk.corpus.reuters
corpus = nltk.corpus.webtext

# Gathering stop words to remove them from corpus's
nltk.download('stopwords')
stopWordsCorpus = nltk.corpus.stopwords.words('english')
words = corpus.words()
words = [w for w in words if w.lower() not in stopWordsCorpus]
frequencyDistribution = nltk.FreqDist(word.lower() for word in words)
frequenciesAndWords = dict()

for word in words:
    frequenciesAndWords[word] = frequencyDistribution[word]
frequenciesAndWords = list(frequenciesAndWords.items())
frequenciesAndWords.sort(key=lambda a: a[1])
frequenciesAndWords.reverse()
labels, frequencies = map(list, zip(*frequenciesAndWords))

# Displays first 30 words with their corresponding frequencies:
for index in range(30):
    print(labels[index], ' ', frequencies[index])

# Plotting top ten words in corpus
numberOfWords = 10
yPos = range(len(labels))
plt.figure(figsize=(20, 20))
plt.bar(yPos[:numberOfWords], frequencies[:numberOfWords], align='center', alpha=0.5)
plt.xticks(yPos[:numberOfWords], labels[:numberOfWords])
plt.title('Token frequency counts in corpus [first 10 tokens]')
plt.xlabel('Word')
plt.ylabel('Frequency count')
plt.xticks(rotation=90)
plt.show()

# Plotting log plot for first 1000 words
labels2 = labels[:1000]
frequencies2 = frequencies[:1000]
fig, ax = plt.subplots()
xs = range(len(labels))
labels2 = range(len(labels))


def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels2[int(tick_val)]
    else:
        return ''


ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(xs, frequencies)
ax.set_title('Token frequency counts in corpus ranked')
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency count)')
plt.show()

# Calculating Unigram probability finding frequency of word then dividing by total words in corups
test = "judical"

total = 0
count = defaultdict(lambda: 0)
for word in corpus.words():
    total += 1
    count[word] += 1

# Determining Frequency by dividing by total words in Corpus
for word, ct in count.items():
    if word == test:
     print('Frequency of %s: %f%%' % (word, 100.0 * float(ct) / float(total)))


