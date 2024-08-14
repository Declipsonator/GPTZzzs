import random


def change_text(text, synonyms, adjectives, percent_synonyms=50, ignore_quotes=True, percent_adjectives=60):
    words = text.split(" ")

    newWords = ""

    num_words = int(len(words) * percent_synonyms / 100)
    chosen_indices = random.sample(range(len(words)), num_words)

    quotation_count = 0
    for i in range(len(words)):
        if "\"" in words[i]:
            quotation_count += words[i].count("\"")

        if i in chosen_indices and (quotation_count % 2 == 0 or not ignore_quotes):
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
                newWords = "{} ".format(newWords)

    words = newWords.split(" ")

    newWords = ""

    num_words = int(len(words) * percent_synonyms / 100)

    quotation_count = 0
    emphasis_words = ["very", "very", "very", "really", "really", "really", "extremely", "quite", "so", "too", "very",
                      "really"]
    dont_change = False
    for i in range(len(words)):
        if "\"" in words[i]:
            quotation_count += words[i].count("\"")

        if words[i] in emphasis_words and words[i + 1] and words[i + 1] in adjectives and (
                quotation_count % 2 == 0 or not ignore_quotes):
            if random.randint(0, 100) < percent_adjectives:
                dont_change = True
                continue

        if words[i] in adjectives and not dont_change and (quotation_count % 2 == 0 or not ignore_quotes):
            if random.randint(0, 100) < percent_adjectives:
                emp_word = random.choice(emphasis_words)
                newWords = "{}{} {}".format(newWords, emp_word, words[i])
                if i != len(words) - 1:
                    newWords = "{} ".format(newWords)
                continue

        dont_change = False
        newWords = "{}{}".format(newWords, words[i])
        if i != len(words) - 1:
            newWords = "{} ".format(newWords)
            
        return newWords