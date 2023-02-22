var zaibacuThesaurus;
var finnplSynonyms;
var adjectives;

async function updateText() {
    let percentToChangeSyn = document.getElementById("input-syn-percent").value;
    let percentToChangeAdj = document.getElementById("input-adj-percent").value;
    let inputText = document.getElementById("input-text").value;
    let inputCollection = document.getElementById("input-collection").value;
    let ignoreQuotes = document.getElementById("input-ignore-quotes").checked;
    let words = inputText.split(" ");

    let newWords = "";
    let num_words = Math.floor(words.length * percentToChangeSyn / 100);
    let chosen_indices = getRandomSampleFromRange(0, words.length, num_words)

    if(inputCollection == "1" && zaibacuThesaurus == null) {
        await fetch("https://raw.githubusercontent.com/zaibacu/thesaurus/master/en_thesaurus.jsonl")
            .then(response => response.text())
            .then(data => {
                let lines = data.split("\n");
                let word_synonyms = []
                for(var line in lines) {
                    if(lines[line]) {
                        word_synonyms.push(JSON.parse(lines[line]));
                    }
                }
                let synonyms = {};
                word_synonyms.forEach(entry => {
                    synonyms[entry.word] = entry.synonyms;
                });
                zaibacuThesaurus = synonyms;

            })
            .catch(error => console.error(error));
        console.log("Fetched synonyms")
    } else if(inputCollection == "2" && finnplSynonyms == null) {
        await fetch("https://raw.githubusercontent.com/FinNLP/synonyms/master/src.json")
            .then(response => response.text())
            .then(data => {
                let synonyms = JSON.parse(data);

                for (const [key, value] of Object.entries(synonyms)) {
                    synonyms[key] = [];
                    for (const [k, v] of Object.entries(value)) {
                        synonyms[key] = synonyms[key].concat(v.slice(1));
                    }
                    if (synonyms[key].includes("v")) {
                        synonyms[key].splice(synonyms[key].indexOf("v"), 1);
                    }
                    if (synonyms[key].includes("s")) {
                        synonyms[key].splice(synonyms[key].indexOf("s"), 1);
                    }
                    if (synonyms[key].includes("r")) {
                        synonyms[key].splice(synonyms[key].indexOf("r"), 1);
                    }
                    if (synonyms[key].includes("a")) {
                        synonyms[key].splice(synonyms[key].indexOf("a"), 1);
                    }
                    if (synonyms[key].includes("n")) {
                        synonyms[key].splice(synonyms[key].indexOf("n"), 1);
                    }
                }

                finnplSynonyms = synonyms;

            })
            .catch(error => console.error(error));
        console.log("Fetched synonyms")
    }

    if(adjectives == null) {
        await fetch("https://raw.githubusercontent.com/rgbkrk/adjectives/master/index.js")
            .then(response => response.text())
            .then(data => {
                let lines = data.split("\n")
                let adjs = [];

                for(let i = 1; i < lines.length - 2; i++) {
                    var adjective = lines[i].substring(
                        lines[i].indexOf("'") + 1,
                        lines[i].lastIndexOf("',"));
                    adjs.push(adjective);
                }


                adjectives = adjs;

            })
            .catch(error => console.error(error));
        console.log("fetched adjectives")
    }

    console.log(chosen_indices)

    let synonymss = null;
    if(inputCollection == "1") synonymss = zaibacuThesaurus;
    else if(inputCollection == "2") synonymss = finnplSynonyms;

    let quoteCount = 0;
    for (let i = 0; i < words.length; i++) {
        if(words[i].indexOf("\"") != -1) quoteCount += (words[i].match(/"/g) || []).length;

        if (chosen_indices.includes(i) && (quoteCount % 2 == 0 || !ignoreQuotes)) {
            let word = words[i];
            let endswith = "";
            if (word.endsWith(".") || word.endsWith(",") || word.endsWith("!") || word.endsWith("'") || word.endsWith("?") || word.endsWith(":") || word.endsWith(";")) {
                endswith = word[word.length - 1];
                word = word.substr(0, word.length - 1);
            }

            if (word.length > 3 && synonymss[word] && synonymss[word].length != 0) {
                word = synonymss[word][Math.floor(Math.random() * synonymss[word].length)];
            }

            newWords += word + endswith + " ";
        } else {
            newWords += words[i];
            if(i !== words.length - 1) {
                newWords += " ";
            }
        }
    }
    console.log(newWords)

    words = newWords.split(" ");
    newWords = ""

    quoteCount = 0;
    let emphasisWords = ["very", "very", "very", "really", "really", "really", "extremely", "quite", "so", "too", "very", "really"]
    let dontChange = false;
    for (let i = 0; i < words.length; i++) {
        if (words[i].includes('"')) {
            quoteCount += words[i].split('"').length - 1;
        }

        if (emphasisWords.includes(words[i]) && adjectives.includes(words[i + 1]) && (quoteCount % 2 === 0 || !ignoreQuotes) && Math.floor(Math.random() * 100) < percentToChangeAdj) {
            dontChange = true;
            continue;
        }

        if (adjectives.includes(words[i]) && !dontChange && (quoteCount % 2 === 0 || !ignoreQuotes) && Math.floor(Math.random() * 100) < percentToChangeAdj) {
            const emp_word = emphasisWords[Math.floor(Math.random() * emphasisWords.length)];
            newWords += `${emp_word} ${words[i]}${i !== words.length - 1 ? ' ' : ''}`;
            continue;
        }

        dontChange = false;
        newWords += `${words[i]}${i !== words.length - 1 ? ' ' : ''}`;
    }

    document.getElementById("output-text").textContent = newWords;

    console.log(newWords)
}


function getRandomElements(array, numElements) {
    let randomElements = [];
    for (let i = 0; i < numElements; i++) {
        let randomIndex = Math.floor(Math.random() * array.length);
        randomElements.push(array[randomIndex]);
        array.splice(randomIndex, 1);
    }
    return randomElements;
}


function getRandomSampleFromRange(start, end, numElements) {
    let range = Array.from({length: end - start + 1}, (_, i) => start + i);
    return getRandomElements(range, numElements);
}




async function copyContent() {
    let text = document.getElementById('output-text').textContent;
    if (!navigator.clipboard) {
        alert("Copy functionality not supported");
    }
    try {
        await navigator.clipboard.writeText(text);
    } catch (err) {
        console.error("ERROR", err);
    }
}


