#!/usr/bin/env node

/**
 * 
 * @param {string} string1 Target string to check for a match
 * @param {string} string2 String used to check from
 * @returns Bool - True if a match is found, False if not
 */

function isCharacterMatch(string1, string2) {

    // Construct a RegEx with the characters from strCheck
    // Flagged as case insensitive
    let regexCheckPattern = new RegExp(`[${string2}]{${string2.length}}`,"i");

    //console.log(regexCheckPattern)

    return regexCheckPattern.test(string1)
}

function anagramsFor(word, listOfWords) {
    let arrResult = []

    for(let strThisWord of listOfWords) {
        if(isCharacterMatch(word, strThisWord)) {
            arrResult.push(strThisWord)
        }

    }

    return arrResult;
}

exports.isCharacterMatch = function(string1, string2) {
    isCharacterMatch(string1, string2)
};

exports.anagramsFor = function(word, listOfWords) {
    anagramsFor(word, listOfWords)
};

//module.exports = isCharacterMatch, anagramsFor;

let listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

//console.log(isCharacterMatch("CharM", "mARch"))
console.log(anagramsFor("threads", listOfWords))
console.log(anagramsFor("threads", listOfWords).length)
