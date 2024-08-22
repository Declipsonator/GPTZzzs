import os

import gptzzzs


print("""\033[1;31;40m
░██████╗░██████╗░████████╗███████╗███████╗███████╗░██████╗
██╔════╝░██╔══██╗╚══██╔══╝╚════██║╚════██║╚════██║██╔════╝
██║░░██╗░██████╔╝░░░██║░░░░░███╔═╝░░███╔═╝░░███╔═╝╚█████╗░
██║░░╚██╗██╔═══╝░░░░██║░░░██╔══╝░░██╔══╝░░██╔══╝░░░╚═══██╗
╚██████╔╝██║░░░░░░░░██║░░░███████╗███████╗███████╗██████╔╝
░╚═════╝░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚══════╝╚══════╝╚═════╝░
\033[0m""")



percentToChangeSyn = input("\033[1;32;40mPercentage of words to replace with synonyms (Recommended: 20-30 for Zaibacu, 70-90 for FinNLP):\033[0m")

try:
    percentToChangeSyn = float(percentToChangeSyn)
except:
    print("\033[0;31;40mNot valid number\033[0m")
    exit()

if percentToChangeSyn < 0 or percentToChangeSyn > 100:
    print("\033[0;31;40mNumber needs to be between 0 and 100\033[0m")
    exit()


collection = input("""
Synonym Collection to Use:

1. Zaibacu Thesaurus
2. FinNLP Synonyms (Recommended)

\033[1;32;40mChoice: \033[0m""")

try:
    collection = int(collection)
except:
    print("\033[0;31;40mNot valid number\033[0m")
    exit()

if collection < 1 or collection > 2:
    print("\033[0;31;40mNumber needs to be between 1 and 2\033[0m")
    exit()



percentToChangeAdj = input("\n\033[1;32;40mPercentage of adjectives to change emphasis on (Recommended: 50-80): \033[0m")

try:
    percentToChangeAdj = float(percentToChangeAdj)
except:
    print("\033[0;31;40mNot valid number\033[0m")
    exit()

if percentToChangeAdj < 0 or percentToChangeAdj > 100:
    print("\033[0;31;40mNumber needs to be between 0 and 100\033[0m")
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


use_common_words = input("""
\033[1;32;40mOnly Use Common Words (y/N) (Not Recommended): \033[0m""")

if use_common_words.lower() == "y" or use_common_words.lower() == "yes":
    ignore_quotes = True

elif use_common_words.lower() == "n" or use_common_words.lower() == "yes":
    use_common_words = False
else:
    print("\033[0;31;40mInvalid answer, answer with y or n\033[0m")
    exit()


text_file_name = "text.txt"
if os.path.exists(text_file_name):
    with open(text_file_name, "r") as f:
        text = f.read()
        print("Loaded text file from local folder\033[0m")
else:
    print("\033[0;31;40mText file not found.\033[0m")
    exit()

editor = gptzzzs.Gptzzzs()

synonym_list = "zaibacu" if collection == 1 else "finnlp"
response = editor.change_text(text, synonym_list=synonym_list, percent_synonyms=percentToChangeSyn, ignore_quotes=ignore_quotes, percent_adjectives=percentToChangeAdj, common_words=use_common_words, adjective_list="normal")

with open("output.txt", "w") as f:
    f.write(response)
    print("Saved Result")