
import nltk
import re
from nltk import FreqDist
from nltk.corpus import PlaintextCorpusReader

 
mycorpus=	PlaintextCorpusReader('.','.*\.txt')
text = mycorpus.raw("tweetfile.txt")
mentions = nltk.regexp_tokenize(text,r'@\w+\b' )
len(set(mentions))

links = nltk.regexp_tokenize(text,r'(?:http|https):\/\/\w+\.\w+\/[\w.,@?^=%&:\/~+#-]*(?=\s)\b' )
len(links)

mentionsFreq = FreqDist(mentions)
top = mentionsFreq.most_common(10)


tweets = text.split("\r\n")

listOtweets = []

for i in tweets:
    if "@Inkululeko1" in i:
        listOtweets.append(i)
        
#QUESTION 2
        
        
import csv

f = [] 
with open('heemaTweets.csv', encoding='utf8') as csvfile:  
     reader = csv.DictReader(csvfile)  
     for row in reader:        
         f.append(row['text'])

tweetfile = open('amiham_tweet.txt', 'w')
for item in f:  
    tweetfile.write("%s\n" % item)  
    


file = open ('amiham_tweet.txt')

x = file.read()
y = file.readlines()

file.seek(0)
tweetlist = []
for line in file: 
    tweetlist.append(line.strip())

hashtagA = []
pattern = re.compile("(#\w+)")
for tweet in tweetlist:
    for word in tweet.split():
        if (pattern.match(word)):
            hashtagA.append(word)
hashtagA

trial = ' '.join(c for c in hashtagA if pattern.match(c))
hashtags = nltk.regexp_tokenize(trial,r"#\w+[^: .’',?;]" )

tagFreq = FreqDist(hashtags)
topTag = tagFreq.most_common(10)
 

fileW = open("hashtags.txt","w")
fileW.write("The hashtags Mahima uses:\n")
for tag in set(hashtags):
    fileW.write(tag)
    fileW.write("\n")

fileW.close()
#%%

import csv

f = [] 
with open('heemaTweets.csv', encoding='utf8') as csvfile:  
     reader = csv.DictReader(csvfile)  
     for row in reader:        
         f.append(row['text'])

tweetfile = open('amiham_tweet.txt', 'w')
for item in f:  
    tweetfile.write("%s\n" % item)  
    


file = open ('amiham_tweet.txt')

x = file.read()
y = file.readlines()

file.seek(0)
tweetlist = []
for line in file: 
    tweetlist.append(line.strip())

hashtagA = []
pattern = re.compile("(#\w+)")
for tweet in tweetlist:
    for word in tweet.split():
        if (pattern.match(word)):
            hashtagA.append(word)
hashtagA

trial = ' '.join(c for c in hashtagA if pattern.match(c))
hashtags = nltk.regexp_tokenize(trial,r"#\w+[^:.’',?;]" )

tagFreq = FreqDist(hashtags)
topTag = tagFreq.most_common(10)
 

fileW = open("hashtags.txt","w")
fileW.write("The uniquew hashtags Mahima uses:\n")
for tag in set(hashtags):
    fileW.write(tag)
    fileW.write("\n")

fileW.close()































   
#%%
file = open ('amiham_tweet.txt')

x = file.read()
y = file.readlines()
file.seek(0)
tweetlist = []
for line in file: 
    tweetlist.append(line.strip())



#%%
hashtag = []
pattern = re.compile("(#\w+[:.’',?;])")
for tweet in tweetlist:
    for word in tweet.split():
        if (pattern.match(word)):
            hashtag.append(word)
hashtag

trial = ' '.join(c for c in hashtag if pattern.match(c))           
          
#Couldnt do it in python. Did it in Regexr.com   
twiter = "#sublimetext #regex #NICAR17 #NICAR17 #NHdata #WomensMarch #Syracuse #ElectionNight #ramnathgoenka #debatenight #debatenight #ModiInUK #DCW #AskChetan #StStephens #FTII #Bollywood #SalmanVerdict #KisaanRally #LandBill #Rahul #FreedomOfExpression #NetNeutrality #NLalert #RahulGandhi #NLWatch #NLwatch #NLwatch #NLwatch #NLwatch #Reporters #NLWatch #Reporters #NLWatch #NLWatch #Reporters #NetNeutrality #66A #JeSuisNDTVGirl #JeSuisNDTVGirl #NDTVGirlAsks #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #JK #NLprimetime #NLprimetime #WhoKnew #censorship #NLprimetime #Futurama #ShameTheCop #NLprimetime #NLprimetime #Futurama #NLprimetime #NLprimetime #NLprimetime #NLprimetime #yoNidhiIsSoModest #NLprimetime #Goswami #NLprimetime #BJP #NLprimetime #NLprimetime #IndexDrawTheLine #Rip #DEC16 #IndexDrawtheLine #FCC #netneutrality #Reliance #HinduMahasabha- #hindumahasabha #ValentinesDay #hindumahasabha #ValentinesDay #NLprimetime #twitter #NLprimetime #NLprimetime #ManishSasodia #NLprimetime #NLprimetime #NLprimetime #NLprimetime. #NLprimetime #SureshbhaiPatel #NLprimetime #FreeAjStaff #NLprimetime #Ukraine&amp;Russia #NLprimetime #JonStewart's #FreeAJS #DelhiElectionResults #AAPs #NLHafta #Delhielections #swissleaks #AIBroast #TaylorSwift #NLprimetime #Futurama #NLpoll #RaifBadawi #NLprimetime #NLprimetime #NLprimetime #NLpoll #BJP #KiranBedi #IndexDrawtheLine #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #BJP #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #NLprimetime #newslaundry #Rupee #Dollar #NetNeutrality #newslaundry #MangaHangover #NLprimetime #MLAAbuseTape #NLprimetime #NLprimetime #BJP #Podcast #NLpodcast #NLprimetime #NewsX #GandhiKiller #NLprimetime #NLprimetime #SaifBrawlTapes #NLprimetime #Assange's #Azerbaijan #humanrights #delhiqueerpride #PrideKyun #StarWarsEpisodeVII #NLprimetime #NLprimetime #IPLCleanBowled #NLprimetime #NLprimetime #NLprimetime #Jurassicpark #KitKat #immerse #Zee #TOI #Censorship #Scotland #kashmiri #indeyref #ScotlandDecides #NLBlogs #newslaundry #newslaundry #newslaundry #NLBlogs #urgent #newslaundry #Clothesline #newslaundry #newslaundry #newslaundry #NLBlogs #urgent #newslaundry #newslaundry #newslaundry #newslaundry #newslaundry #Clothesline #newslaundry #KashmirFloods #Clothesline #tbt #newslaundry #newslaundry #podcast #Clothesline #newslaundry #KashmirFloods #newslaundry #podcast #newslaundry #newslaundry #Clothesline #newslaundry #newslaundry #KashmirFloods #Clothesline #newslaundry #newslaundry #podcast #Clothesline #IndiaTV #PIB #Jaitleys"
hashtag = []
hashtag = twiter.split()
tagFreq = FreqDist(hashtag)
topTag = tagFreq.most_common(10)