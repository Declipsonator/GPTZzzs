# GPTZzzs
ChatGpt/Gpt3 detector bypasser. Works with all detectors including GptZero.

## Running
1. Install Python (This was tested on Python 3.1)
2. Replace the content inside of text.txt with your gpt generated text
3. Run `python main.py`
4. Input the percentage of words to change and run it\
<b>(The best percentage is between 20% and 30%)</b>
5. Select which collection of synonyms you want. Both work but FinNLP requires a higher percentage because it has less words.
5. You're Done! Check output.txt for the result.

It is recommended to go over the text and fix any weird bits once finished.

## Information
Currently GPTZzzs works by downloading a dictionary of synonyms and replacing a number of words with their counterparts. While this works most of the time, sometimes synonyms can be very odd and would require fixing by humans. This process however does a great job at getting past GPT detectors! This works with every detector tested from GPT Zero to the Grammarly Plagiarism Check.
<br/>
<br/>


<b>Before           |  After</b>
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/96392121/218274220-3a7741e2-3c9b-4139-b26b-3bd5135a503c.png" height="400" width="380" /> | <img src="https://user-images.githubusercontent.com/96392121/218274223-c1f4fe84-9a61-4348-9ec7-815d7526be25.png" height="400" width="380"/>

## TODO
- <del>Replace words with synonyms</del>
- Only use synonyms that are common words in english
- Remove/add unnecessary words
- Reorder sentences
- Switch out expressions
- Abbreviate/unabbreviate words/phrases

<a href="https://www.buymeacoffee.com/declipsonator" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" alt="Buy Me A Coffee" height="41" width="174"></a>

