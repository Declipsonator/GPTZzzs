from setuptools import setup, find_packages
import urllib.request
import json
import os
import re

"""
    Note to self:
    python setup.py sdist bdist_wheel
    twine upload --repository pypi dist/*
"""


# URLs for downloading the data files
zaibacu_url = "https://raw.githubusercontent.com/zaibacu/thesaurus/master/en_thesaurus.jsonl"
finnlp_url = "https://raw.githubusercontent.com/FinNLP/synonyms/master/src.json"
adjective_url = "https://raw.githubusercontent.com/rgbkrk/adjectives/master/index.js"
common_words_url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"

# Data directory inside the package
data_dir = os.path.join(os.path.dirname(__file__), 'gptzzzs', 'data')

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

def download_zaibacu():
    response = urllib.request.urlopen(zaibacu_url)
    data = response.read().decode('utf-8')
    word_synonyms = [json.loads(line) for line in data.split("\n") if line]
    with open(os.path.join(data_dir, "zaibacu.json"), "w") as f:
        json.dump({entry['word']: entry['synonyms'] for entry in word_synonyms}, f)

def download_finnlp():
    response = urllib.request.urlopen(finnlp_url)
    synonyms = json.loads(response.read().decode('utf-8'))
    with open(os.path.join(data_dir, "finnlp-separate.json"), "w") as f:
        json.dump(synonyms, f)
    for key, value in synonyms.items():
        synonyms[key] = [word for k, v in value.items() for word in v[1:] if word not in {"v", "s", "r", "a", "n"}]
    with open(os.path.join(data_dir, "finnlp-together.json"), "w") as f:
        json.dump(synonyms, f)

def download_common_words():
    response = urllib.request.urlopen(common_words_url)
    common_words = response.read().decode('utf-8').split("\n")
    with open(os.path.join(data_dir, "common_words.json"), "w") as f:
        json.dump(common_words, f)

def download_adjectives():
    response = urllib.request.urlopen(adjective_url)
    lines = response.read().decode('utf-8').split("\n")
    adjectives = [re.search('\'(.*)\',', line).group(1) for line in lines[1:-2] if re.search('\'(.*)\',', line)]
    with open(os.path.join(data_dir, "adjectives.json"), "w") as f:
        json.dump(adjectives, f)

# Download data files
download_zaibacu()
download_finnlp()
download_common_words()
download_adjectives()

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Setup configuration
setup(
    name='gptzzzs',
    version='0.0.1',
    packages=find_packages(),
    author='Jackson Hickey',
    author_email='jackson@jacksonhickey.tech',
    description='Gptzzzs is a tool that attempts large language model detection evasion by changing grammar.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Declipsonator/GPTZzzs',
    classifiers=[
        'Programming Language :: Python :: 3.1',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.1',
    include_package_data=True,
    package_data={'gptzzzs': ['data/*.json']},
)
