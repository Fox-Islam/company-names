const names = document.getElementById('names').textContent.trim().split('\n');
const places = document.getElementById('places').textContent.trim().split('\n');
const verbs = document.getElementById('verbs').textContent.trim().split('\n');
const trades = document.getElementById('trades').textContent.trim().split('\n');
const nouns = document.getElementById('nouns').textContent.trim().split('\n');
const adjectives = document.getElementById('adjectives').textContent.trim().split('\n');

function pickCapitalizedFromList(list) {
    return capitalizeFirstLetter(pickFromList(list));
}

function pickCapitalizedPluralFromList(list) {
    const word = capitalizeFirstLetter(pickFromList(list));
    if (wordCanEasilyPlural(word)) {
        return word + 's';
    }
    return word;
}

function pickFromList(list) {
    const randomIndex = Math.floor(Math.random() * list.length);
    return list[randomIndex];
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function createListString(list) {
    const length = Math.ceil(Math.random() * 3);
    if (length === 1) {
        return pickCapitalizedPluralFromList(list);
    }
    let words = [];
    let remainingLength = length;
    while (remainingLength > 1) {
        words.push(pickCapitalizedPluralFromList(list));
        remainingLength -= 1;
    }
    return words.join(', ') + " and " + pickCapitalizedPluralFromList(list);
}

const companyNameTypes = [
    "verbify",
    "verbtsy",
    "nounster",
    "location objects",
    "person's objects",
    "location trades",
    "person and co trades",
    "compound nouns",
    "person's adjective nouns",
];

const associateTypes = [
    " and Co.",
    " and Family",
    " and Daughters",
    " and Sons",
    " and Friends",
];

function generateCompanyName() {
    const type = pickFromList(companyNameTypes);
    switch (type) {
        case "verbify":
            return pickCapitalizedFromList(
                getWordsWithoutVowelEndings(verbs)
            ) + 'ify';
        case "verbtsy":
            return pickCapitalizedFromList(
                getWordsWithoutTEndings(verbs)
            ) + 'sy';
        case "nounster":
            return pickCapitalizedFromList(
                getWordsWithoutSOrErEndings(nouns)
            ) + 'ster';
        case "location objects":
            return pickCapitalizedFromList(places) + " " + createListString(nouns);
        case "person's objects":
            return pickCapitalizedFromList(names) + "'s " + createListString(nouns);
        case "location trades":
            return pickCapitalizedFromList(places) + " " + pickCapitalizedPluralFromList(trades);
        case "person and co trades":
            return pickCapitalizedFromList(names) + pickFromList(associateTypes) + " " + pickCapitalizedPluralFromList(trades);
        case "compound nouns":
            return pickCapitalizedFromList(nouns) + pickCapitalizedFromList(nouns);
        case "person's adjective nouns":
            return pickCapitalizedFromList(names) + "'s " + pickCapitalizedFromList(adjectives) + " " + createListString(nouns);
        default:
            const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
            return letters.charAt(Math.floor(Math.random() * letters.length));
    }
}

function getWordsWithoutVowelEndings(words) {
    return words.filter((word) => {
        return !wordEndsWithVowel(word);
    });
}

function wordEndsWithVowel(word) {
    const vowels = "aeiouy";
    if (vowels.includes(word[word.length - 1])) {
        return true;
    }
    return false;
}

function wordCanEasilyPlural(word) {
    return !word.endsWith('s') && !word.endsWith('y');
}

function getWordsWithoutTEndings(words) {
    return words.filter((word) => {
        return !word.endsWith('t');
    });
}

function getWordsWithoutSOrErEndings(words) {
    return words.filter((word) => {
        return !word.endsWith('s') && !word.endsWith('er');
    });
}

function buttonClick() {
    const textDiv = document.getElementById('text');
    const input = document.getElementById('input');
    if (input.value) {
        let generated = 0;
        let companyNames = [];
        while (generated < parseInt(input.value)) {
            companyNames.push(generateCompanyName());
            generated += 1;
        }
        textDiv.innerText = companyNames.join('\n');
        return;
    }
    textDiv.innerText = generateCompanyName();
}
