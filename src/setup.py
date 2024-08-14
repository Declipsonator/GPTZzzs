from setuptools import setup, find_packages
from importlib import resources
import urllib.request
import json
import os

zaibacu_url = "https://raw.githubusercontent.com/zaibacu/thesaurus/master/en_thesaurus.jsonl"
finnlp_url = "https://raw.githubusercontent.com/FinNLP/synonyms/master/src.json"
adjective_url = "https://raw.githubusercontent.com/rgbkrk/adjectives/master/index.js"
common_words_url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"

def prepare():
    # Create data directory if it doesn't exist
    path = resources.files("gptzzzs").joinpath('data')
    if not os.path.exists(str(path)):
        os.makedirs(str(path))


def download_zaibacu():
    print("Downloading Zaibacu thesaurus from {}...".format(zaibacu_url))
    response = urllib.request.urlopen(zaibacu_url)
    data = response.read()
    text = data.decode('utf-8')

    lines = text.split("\n")
    word_synonyms = [json.loads(line) for line in lines if line]
    print("Loaded Zaibacu thesaurus from remote URL")

    # Create word-synonyms dictionary
    path = str(resources.files("gptzzzs").joinpath('data').joinpath("zaibacu.json"))
    with open(str(path), "w+") as f:
     f.write(json.dumps({entry['word']: entry['synonyms'] for entry in word_synonyms}))

    print("Wrote Zaibacu thesaurus to file")

def download_finnlp():
    response = urllib.request.urlopen(finnlp_url)
    data = response.read()
    text = data.decode('utf-8')

    synonyms = json.loads(text)
    print("Loaded synonym file from remote URL")

    path = str(resources.files("gptzzzs").joinpath('data').joinpath("finnlp-separate.json"))
    with open(str(path), "w+") as f:
        f.write(json.dumps(synonyms))

    # Create word-synonyms dictionary
    for key, value in synonyms.items():
        synonyms[key] = []
        for k, v in value.items():
            synonyms[key] += [word for word in v[1:]]
        if "v" in synonyms[key]:
            synonyms[key].remove("v")
        if "s" in synonyms[key]:
            synonyms[key].remove("s")
        if "r" in synonyms[key]:
            synonyms[key].remove("r")
        if "a" in synonyms[key]:
            synonyms[key].remove("a")
        if "n" in synonyms[key]:
            synonyms[key].remove("n")

    path = str(resources.files("gptzzzs").joinpath('data').joinpath("finnlp-together.json"))
    with open(str(path), "w+") as f:
        f.write(json.dumps(synonyms))







setup(
    name='gptzzzs',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # List any dependencies here
    author='Jackson Hickey',
    author_email='jackson@jacksonhickey.tech',
    description='Gptzzzs is a tool that attempts large language model detection evasion by changing grammar.',
    url='https://github.com/Declipsonator/GPTZzzs',
    classifiers=[
        'Programming Language :: Python :: 3.1',
        'License :: GNU General Public License v3.0',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.1',
    include_package_data=True,
    package_data={'': ['data/*.json']}
)

prepare()
download_zaibacu()
download_finnlp()



