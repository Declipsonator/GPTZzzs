import os
import urllib.request
import json
import random

file_name = "synonyms.json"
zaibacu_url = "https://raw.githubusercontent.com/zaibacu/thesaurus/master/en_thesaurus.jsonl"
finnlp_url = "https://raw.githubusercontent.com/FinNLP/synonyms/master/src.json"


print("""\033[1;31;40m
░██████╗░██████╗░████████╗███████╗███████╗███████╗░██████╗
██╔════╝░██╔══██╗╚══██╔══╝╚════██║╚════██║╚════██║██╔════╝
██║░░██╗░██████╔╝░░░██║░░░░░███╔═╝░░███╔═╝░░███╔═╝╚█████╗░
██║░░╚██╗██╔═══╝░░░░██║░░░██╔══╝░░██╔══╝░░██╔══╝░░░╚═══██╗
╚██████╔╝██║░░░░░░░░██║░░░███████╗███████╗███████╗██████╔╝
░╚═════╝░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚══════╝╚══════╝╚═════╝░
\033[0m""")


percentToChange = input("\033[1;32;40mPercentage of words to change: \033[0m")



try:
    percentToChange = float(percentToChange)
except:
    print("\033[0;31;40mNot valid number\033[0m")
    exit()

if percentToChange < 0 or percentToChange > 100:
    print("\033[0;31;40mNumber needs to be between 0 and 100\033[0m")
    exit()
    
    
collection = input("""
Synonym Collection to Use:

1. Zaibacu Thesaurus
2. FinNLP Synonyms

\033[1;32;40m
Choice: \033[0m""")

try:
    collection = int(collection)
except:
    print("\033[0;31;40mNot valid number\033[0m")
    exit()

if collection < 1 or collection > 2:
    print("\033[0;31;40mNumber needs to be between 1 and 2\033[0m")
    exit()    
    
    
    
ignore_quotes = input("""
\033[1;32;40mIgnore Quotations (y/N): \033[0m""")

if ignore_quotes.lower() == "y" or ignore_quotes.lower() == "yes":
    ignore_quotes = True
    
elif ignore_quotes.lower() == "n" or ignore_quotes.lower() == "yes":
    ignore_quotes = False
else:
    print("\033[0;31;40mInvalid answer, answer with y or n\033[0m")
    exit()


    

# Load synonym file or download it if it doesn't exist
print("")
if os.path.exists("{}{}".format(collection, file_name)):
    with open("{}{}".format(collection, file_name), "r") as f:
        text = f;
        synonyms = json.load(text)
        print("\033[1;33;40mLoaded file from local folder")
else:
    try:
        if collection == 1:
            response = urllib.request.urlopen(zaibacu_url)
            data = response.read()
            text = data.decode('utf-8')

            lines = text.split("\n")
            word_synonyms = [json.loads(line) for line in lines if line]
            print("Loaded file from remote URL")
            
            # Create word-synonyms dictionary
            
            synonyms = {entry['word']: entry['synonyms'] for entry in word_synonyms}

        elif collection == 2:
            response = urllib.request.urlopen(finnlp_url)
            data = response.read()
            text = data.decode('utf-8')

            synonyms = json.loads(text)
            print("Loaded file from remote URL")
            
            # Create word-synonyms dictionary
            
            for key, value in synonyms.items():
                synonyms[key] = []
                for k, v in value.items():
                    synonyms[key] += [word for word in v[1:]]
                if("v" in synonyms[key]):
                    synonyms[key].remove("v")
                if("s" in synonyms[key]):
                    synonyms[key].remove("s")
                if("r" in synonyms[key]):
                    synonyms[key].remove("r")
                if("a" in synonyms[key]):
                    synonyms[key].remove("a")
                if("n" in synonyms[key]):
                    synonyms[key].remove("n")
              
                
        
        
        # Save dictionary to file

        dict_file_name = "{}synonyms.json".format(collection)
        with open(dict_file_name, "w") as f:
            f.write(json.dumps(synonyms))
            print("Saved dictionary to local folder")
            
    except Exception as e:
        print("\033[0;31;40mFailed to load synonyms file\033[0m")
        print(e)
        exit()
        

# Load text file

text_file_name = "text.txt"
if os.path.exists(text_file_name):
    with open(text_file_name, "r") as f:
        text = f.read()
        print("Loaded text file from local folder\033[0m")
else:
    print("\033[0;31;40mText file not found.\033[0m")
    exit()



words = text.split(" ")

newWords = ""

num_words = int(len(words) * percentToChange / 100)
chosen_indices = random.sample(range(len(words)), num_words)

quotation_count = 0
for i in range(len(words)):
    if "\"" in words[i]:
        quotation_count += words[i].count("\"")
    
    if i in chosen_indices and (quotation_count % 2 == 0 or ignore_quotes):
        word = words[i]
        endswith = ""
        if word.endswith((".", ",", "!", "'", "?", ":", ";")):
            endswith = word[len(word) - 1]
            word = word[:-1]
        
        if len(word) > 3 and word in synonyms.keys() and len(synonyms[word]) != 0:
            word = random.choice(synonyms[word])
        
        newWords = "{}{}{}".format(newWords, word, endswith)
        if i != len(words) - 1:
            newWords = "{}{}".format(newWords, " ")
            
            
    else:
        newWords = "{}{}".format(newWords, words[i])
        if i != len(words) - 1:
            newWords = "{}{}".format(newWords, " ")
        


with open("output.txt", "w") as f:
    f.write(newWords)
    print("Saved Result")