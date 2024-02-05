#!/usr/bin/env node
// How can you make this more scalable and reusable later?


/**
 * This function splits the digits of a number into an array.
 * @param {number} intNum Number to be split
 * @returns Array of digits from intNum
 */
function splitDigits(intNum) {

    let arrResult = [];

    // Iterate through the number (as a string) and match each digit (globally)
    for(let strDigit of `${intNum}`.matchAll(/\d/g)) {
        arrResult.push(strDigit[0])
    }
    return arrResult;
}


/**
 * This function accepts a range of numbers as an array and returns the Armstrong Numbers
 * found in that array
 * @param {array} arrInput Array of a range of numbers to search for Armstrong Numbers
 * @returns Array containing Armstrong Numbers found in the given range
 */
function findArmstrongNumbers(arrInput) {
    let arrResult = [];

    for(let intIndex in arrInput) {
        // Take each number from the array and turn it into a string
        // Iterate through the characters of the string to calculate
        // the number to determine if it is an Armstrong Number or not

        let intThisNum = arrInput[intIndex];

        let arrThisNumDigits = splitDigits(intThisNum)

        console.log(arrThisNumDigits)
    }



    return arrResult;

}

exports.findArmstrongNumbers = function() {

};

console.log(findArmstrongNumbers([546, 25, 3]));