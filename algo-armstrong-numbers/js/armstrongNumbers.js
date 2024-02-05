#!/usr/bin/env node
// How can you make this more scalable and reusable later?

function findArmstrongNumbers(intNum) {

    if(intNum >= 0 && intNum <= 999) {


        return intNum;
    }

    return "Invalid Number: Must be between 0 and 999";
}

exports.findArmstrongNumbers = function() {

};

console.log(findArmstrongNumbers(5));