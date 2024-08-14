import importlib.resources as resources
import json
import os
import normal_change


class Gptzzzs:

    percent_synonyms = 50
    ignore_quotes = True
    percent_adjectives = 60
    synonym_list = "finnlp"
    custom_synonyms = None
    custom_adjectives = None


    def __init__(self):
        # Load synonym, adjective, and common word files
        with open(str(resources.files("gptzzzs").joinpath('data/finnlp-together.json')), "r") as f:
            self.finnlp_together = json.load(f)

        with open(str(resources.files("gptzzzs").joinpath('data/finnlp-separate.json')), "r") as f:
            self.finnlp_separate = json.load(f)

        with open(str(resources.files("gptzzzs").joinpath('data/common_words.json')), "r") as f:
            self.common_words = json.load(f)

        with open(str(resources.files("gptzzzs").joinpath('data/adjectives.json')), "r") as f:
            self.adjectives = json.load(f)

        with open(str(resources.files("gptzzzs").joinpath('data/zaibacu.json')), "r") as f:
            self.zaibacu = json.load(f)




    def change_text(self, text, synonym_list="finnlp", percent_synonyms=50, ignore_quotes=True, percent_adjectives=60, common_words=False, adjective_list="normal"):
        if synonym_list == "finnlp":
            synonyms = self.finnlp_together
        elif synonym_list == "zaibacu":
            synonyms = self.zaibacu
        elif synonym_list == "custom" and self.custom_synonyms is None:
            raise ValueError("Custom synonyms not set")
        elif synonym_list == "custom":
            synonyms = self.custom_synonyms
        else:
            raise ValueError("Invalid synonym list")

        if adjective_list == "normal":
            adjectives = self.adjectives
        elif adjective_list == "custom" and self.custom_adjectives is None:
            raise ValueError("Custom adjectives not set")
        elif adjective_list == "custom":
            adjectives = self.custom_adjectives
        else:
            raise ValueError("Invalid adjective list")

        if common_words:
            synonyms = {word: synonyms[word] for word in synonyms if word in self.common_words}

        return normal_change.change_text(text, synonyms, adjectives, percent_synonyms, ignore_quotes, percent_adjectives)


