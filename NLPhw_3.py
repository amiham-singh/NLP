
import nltk



## write your own grammars
grammar = nltk.CFG.fromstring("""

S 	-> NP VP
NP 	-> Prop | Det N | Det ADJ N
VP 	-> V PP NP | V NP | V VP | V Det ADV | V AP | Det V
AP 	-> ADV AP | ADJ VP
PP 	-> Det NP
ADV 	-> 'again' | 'necessarily' | 'not'
ADJ 	-> 'nice' | 'able'
Det 	-> 'to' | 'last' | 'a' | 'that'
N 	-> 'month' | 'day'
V 	-> 'went' | 'is' | 'can' | 'say' | 'fly' | 'are'
Prop 	-> 'Bob' | 'France' | 'Today' | 'You' | 'Birds'

  """)
 #%% 
rd_parser = nltk.RecursiveDescentParser(grammar)

senttext1 ="Today is a nice day"
senttext2 = "Bob went to France last month"
senttext3= "You can say that again"
senttext4 = "Birds are not necessarily able to fly"
senttext5 = "Bob is not able to say"
senttext6 = "You can fly to France Today"
senttext7 = "Bob went to France Today"
#%%

sentlist = senttext7.split()
trees = rd_parser.parse(sentlist)

treelist= list(trees)

for tree in treelist:
	print (tree)
#%%
senttext1 ="Today is a nice day"
senttext2 = "Bob went to France last month"
senttext3= "You can say that again"
senttext4 = "Birds are not necessarily able to fly"
senttext5 = "Bob is not able to say"
senttext6 = "You can fly to France Today"
senttext7 = "Bob went to France Today"

grammar = nltk.PCFG.fromstring("""
S 	-> NP VP [1.0]
NP 	-> Prop[0.4] | Det N[0.3] | Det ADJ N[0.3]
VP 	-> V PP NP [0.16] | V NP [0.20] | V VP [0.16] | V Det ADV [0.16] | V AP [0.16] | Det V [0.16]
AP 	-> ADV AP[0.5] | ADJ VP [0.5]
PP 	-> Det NP [1.0]
ADV -> 'again' [0.3] | 'necessarily' [0.3] | 'not' [0.4]
ADJ -> 'nice' [0.5] | 'able' [0.5]
Det -> 'to' [0.25] | 'last' [0.25] | 'a' [0.25] | 'that'[0.25]
N 	-> 'month' [0.5] | 'day' [0.5]
V 	-> 'went' [0.16] | 'is' [0.16] | 'can' [0.16] | 'say' [0.16] | 'fly' [0.20] | 'are' [0.16]
Prop -> 'Bob'[0.4] | 'France' [0.18] | 'Today' [0.18] | 'You' [0.15] | 'Birds' [0.09]
    """)
    
rd_parser = nltk.RecursiveDescentParser(grammar)