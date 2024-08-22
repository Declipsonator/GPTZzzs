# Quick Warning
Hey, don't cheat in school (or anything for that matter), I made this project for fun because I find ai interesting. Is it even that good? No. Words are replaced with words that don't work in context or with ancient words that don't make sense. But is it fun to play around with? Yes. So enjoy.


# GPTZzzs
ChatGpt/Gpt3 detector bypasser. This program takes a text file and replaces a percentage of the words with synonyms. This is a simple way to bypass GPT detectors and make your text look more original. This is a fun project and should not be used for cheating or any other malicious purposes.

## Getting Started
1. Download the package with `pip install gptzzzs`
2. Run the program with the following:
```python
import gptzzzs

thing = gptzzzs.Gptzzzs()

text = "" # Put your text here

response = thing.basic_change_text()(text)
```

It is recommended to go over the text and fix any weird bits once finished.

## Information
Currently, GPTZzzs works by downloading a dictionary of synonyms and replacing a number of words with their counterparts. While this works most of the time, sometimes synonyms can be very odd and would require fixing by humans.
<br/>
<br/>


|                                                                  <b>Before                                                                   |                                                                  After</b>                                                                  |
|:--------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| <img src="https://user-images.githubusercontent.com/96392121/218274220-3a7741e2-3c9b-4139-b26b-3bd5135a503c.png" height="400" width="380" /> | <img src="https://user-images.githubusercontent.com/96392121/218274223-c1f4fe84-9a61-4348-9ec7-815d7526be25.png" height="400" width="380"/> |


## TODO
- <del>Replace words with synonyms</del>
- <del>Only use synonyms that are common words in english<del>
- <del>Remove/add unnecessary words</del>
- Reorder sentences
- Switch out expressions
- Abbreviate/unabbreviate words/phrases
- AI? (Maybe)

## Appearances
- [Authorship Obfuscation in Multilingual Machine-Generated Text Detection](https://arxiv.org/abs/2401.07867)
- [Navigating the Shadows: Unveiling Effective Disturbances for Modern AI Content Detectors](https://arxiv.org/abs/2406.08922)
- [TAROT: Task-Oriented Authorship Obfuscation Using Policy Optimization Methods](https://arxiv.org/abs/2407.21630)

## Credits
Independently developed by [Jackson Hickey](https://github.com/declipsonator). Licensed under the GNU General Public License v3.0.
