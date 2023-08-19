""" Cleaning text steps 
1)create a text file and take text from it 
2)convert the letter into lowercase 
3)Remove punctuations like (,.!?) we are importing string and string.punctuation will 
give us all the punctuations so we can easily remove them
 """
import string
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob

text=open('read.text', encoding='utf-8').read()
lower_case=text.lower() 
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))

 # here translate is working as converting the whole text with out any punctuation
 #here str.maketrans is a function that takes 3 parameters and 1st parameter 
 # is here a list of characters that need to be replaced
 # list of characters with which characters need to be replace 
 # 3rd list of characters that need to be dleleted 

# here we are starting tokinization spiliting words into list

tokenized_words = cleaned_text.split()

# stop words are that words which have no meaning

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#Removing stop words from tokenized  words list 

final_words = []
# removing stop words from main list so that we get the final words and we can analyze
#  that what's the eemotion is in the text 

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#NLP EMOTION ALGORITM 
# 1)Check if the word in the final word list is also present in emotion.txt
#   --open emotion text file 
#   --loop through each line and clear it 
#   --extract the word and emotion using split 
# 2)if word is present ->Add the emotion to emotion_list 
# 3)Finally count each emotion in the emotion list  

emotion_list=[] 
with open('Emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion = clear_line.split(':') 
        if word in final_words:
            emotion_list.append(emotion)  
# print(emotion_list)            
w =Counter(emotion_list)
# print(w)
fig ,ax1 =plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.bar(w.keys(),w.values())
plt.savefig('graph.png')
plt.show()


print("Printing subjectivity and polarity of data")
blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity
if polarity > 0:
    sentiment = "positive"
elif polarity < 0:
    sentiment = "negative"
else:
    sentiment = "neutral"
    
print(f"Sentiment of data is : {sentiment}")
print(f"Polarity of data is : {polarity}")
print(f"Subjectivity of data is : {subjectivity}")









