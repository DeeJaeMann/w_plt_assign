#!/usr/bin/env node

/**
 * 
 * @param {number} num 
 * @returns 
 */

function toRomanLazy(num) {
  let strOutput = "";
  //let strLog = "";
  let objRomanNumeralToAribic = {
    'V' : 5,
  };
  let arrRomanNumeralPriorityOrder = ['M','D','C','L','X','V','I'];

  for(let strElement of arrRomanNumeralPriorityOrder) {
    let intDivisor = 0;
    let intTmpDivide = 0;

    // Assign the divisor based on our element
    switch (strElement) {
      case 'M' :
        intDivisor = 1000;
        break;
      case 'D' :
        intDivisor = 500;
        break;
      case 'C' :
        intDivisor = 100;
        break;
      case 'L' :
        intDivisor = 50;
        break;
      case 'X' :
        intDivisor = 10;
        break;
      case 'V' :
        intDivisor = 5;
        break;
      default :
        intDivisor = 1;
        break;
    }

    intTmpDivide = Math.floor(num / intDivisor)

    if(intTmpDivide > 0) {
      strOutput += `${strElement.repeat(intTmpDivide)}`;
      num = num - (intDivisor * intTmpDivide);
    }
    //strLog += `Letter ${strElement} Divisor ${intDivisor} Tmp ${intTmpDivide}\n`
  }

  //console.log(`*****\n${strLog}*****\n`);
  return strOutput;
}

function toRoman(num) {
  let strTemp = toRomanLazy(num);

  let strOutput = strTemp;

  let strLog = "";

  let arrRomanNumeralPriorityOrder = ['M','D','C','L','X','V','I'];

  for(let intIndex = 0; intIndex < arrRomanNumeralPriorityOrder.length + 1; intIndex++) {
    let regexPattern = new RegExp(arrRomanNumeralPriorityOrder[intIndex] + "{4}"); // /M/
    if(regexPattern.test(strOutput))  {
      strLog += `Element ${arrRomanNumeralPriorityOrder[intIndex]} Matched`;
      let regexBehindPattern = new RegExp(arrRomanNumeralPriorityOrder[intIndex - 1] + arrRomanNumeralPriorityOrder[intIndex] + "{4}");
      if(regexBehindPattern.test(strOutput)) {
        strLog += `LookBehind Matched ${arrRomanNumeralPriorityOrder[intIndex - 1]}`;
        strOutput = strOutput.replace(regexBehindPattern, arrRomanNumeralPriorityOrder[intIndex] + arrRomanNumeralPriorityOrder[intIndex - 2]);
      } else {
      strOutput = strOutput.replace(regexPattern, arrRomanNumeralPriorityOrder[intIndex] + arrRomanNumeralPriorityOrder[intIndex - 1]);
      }
    }

  }
  //console.log(strLog);

  return strOutput;
}

//console.log(toRomanLazy(944));
// console.log(toRoman(35));
// console.log(toRoman(11));
//console.log(toRoman(944));
// console.log(toRoman(400));
// console.log(toRoman(4));

module.exports = { toRoman, toRomanLazy };
