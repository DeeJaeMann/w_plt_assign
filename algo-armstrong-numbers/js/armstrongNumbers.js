#!/usr/bin/env node
// How can you make this more scalable and reusable later?

// Begin Helper Functions

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
 * This function calculates the total of each digit as an array calculated to the power
 * of the array length.
 * @param {array} arrNum Array of digits to calculate
 * @returns Calculated total of digits to the power of the length of the given array
 */
function calculateNumber(arrNum) {
    let intTotal = 0;
    let arrSubTotals = [];

    // Iterate through arrNum and calculate the digits to the power of the length of the array
    for(let intDigit of arrNum) {
        let intThisSubTotal = (intDigit ** arrNum.length);
        // Add them to the subtotal array 
        arrSubTotals.push(intThisSubTotal);
    }

    // Add all of the subtotals together
    for(let intDigit of arrSubTotals) {
        intTotal += intDigit;
    }

    return intTotal;

}

// Copied from armstrongNumbersSpec.js to use for internal testing
function createArrayOfNum(maxValue) {
    return [...Array(maxValue).keys()];
  }

// End Helper Functions

/**
 * This function accepts a range of numbers as an array and returns the Armstrong Numbers
 * found in that array
 * @param {array} arrInput Array of a range of numbers to search for Armstrong Numbers
 * @returns Array containing Armstrong Numbers found in the given range
 */
function findArmstrongNumbers(arrInput) {
    let arrResult = [];

    for(let intNumber of arrInput) {
        // Take each number from the array and turn it into a string
        // Iterate through the characters of the string to calculate
        // the number to determine if it is an Armstrong Number or not

        let intThisNum = intNumber;

        let arrThisNumDigits = splitDigits(intThisNum)

        let intThisTotal = calculateNumber(arrThisNumDigits)

        if(intThisTotal === intNumber) {
            arrResult.push(intNumber)
        }
    }

    return arrResult;

}

exports.findArmstrongNumbers = function() {
//exports.findArmstrongNumbers;
};

//module.exports = findArmstrongNumbers;

//console.log(findArmstrongNumbers(createArrayOfNum(99)))