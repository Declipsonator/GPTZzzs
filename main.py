import os
import urllib.request
import json
import random

file_name = "synonyms.json"
url = "https://raw.githubusercontent.com/zaibacu/thesaurus/master/en_thesaurus.jsonl"


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
# Load synonym file or download it if it doesn't exist

if os.path.exists(file_name):
    with open(file_name, "r") as f:
        text = f;
        synonyms = json.load(text)
        print("\033[1;33;40mLoaded file from local folder")
else:
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')

        lines = text.split("\n")
        word_synonyms = [json.loads(line) for line in lines if line]
        print("Loaded file from remote URL")
        
        # Create word-synonyms dictionary
        
        synonyms = {entry['word']: entry['synonyms'] for entry in word_synonyms}

        # Save dictionary to file

        dict_file_name = "synonyms.json"
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

for i in range(len(words)):
    if i in chosen_indices:
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