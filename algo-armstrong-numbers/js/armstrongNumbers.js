#!/usr/bin/env node
// How can you make this more scalable and reusable later?

function findArmstrongNumbers(arrInput) {
    let arrResult = [];

    for(let intIndex in arrInput) {
        // Take each number from the array and turn it into a string
        // Iterate through the characters of the string to calculate
        // the number to determine if it is an Armstrong Number or not

        let intMyNum = arrInput[intIndex];
        let arrDigits = [];
        for(let strDigit of `${intMyNum}`.matchAll(/\d/g)) {
            arrDigits.push(strDigit)
        }


        console.log(`Line: ${arrDigits} myNum ${intMyNum}`);
    }



    return arrResult;

}

exports.findArmstrongNumbers = function() {

};

console.log(findArmstrongNumbers([546, 25, 3]));