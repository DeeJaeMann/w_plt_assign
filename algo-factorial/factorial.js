#!/usr/bin/env node
  /**
   * Calculates the factorial notation of a given number
   * @param {number} 
   * @returns Number
   */
function factorial(num) {
  // Verify number is a digit
  let regexPattern = /^\d+$/;

  if(regexPattern.test(num)) {
    // Input is a digit

    let intResult = 1;
    
    for(let intIndex = 1; intIndex < num + 1; intIndex++){
      intResult *= intIndex;
    }

    return intResult;

  } else {
    // Input is not a digit
    return "Entry must be a digit!";
  }
}


module.exports = factorial;
