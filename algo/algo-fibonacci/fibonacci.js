#!/usr/bin/env node
function fibonacci(num) {

  // Validate num is a number
  regexPattern = /^\d+$/;
  
  if(regexPattern.test(num)) {
    // num is numeric
    if(num > 2) {
    // F(n) = F(n-1) + F(n-2)
    // let intNumOne = 1;
    // let intNumTwo = 1;
    // let intThisNum = 3;

    // while(intThisNum < num) {
    //   intNumOne = intNumTwo;
    //   intNumTwo = int;
    //   intThisNum++;
    // }


    // return intNumOne + intNumTwo;
    let arrFib = [0, 1, 1, 2];
    
    // We're already setup for F(3) so we'll only process from 4
    for(let intIndex = 4; intIndex <= num; intIndex++) {
      let intFirstNum = arrFib[arrFib.length-1];
      let intSecondNum = arrFib[arrFib.length-2];

      arrFib.push((intFirstNum + intSecondNum));
    }

    return arrFib[arrFib.length-1];
  }
  else if (num < 2) {
    // 
    return num;
  } else {
    return 1;
  }

  } else {
    // num is not numeric
    return "Argument must be numeric!";
  }
}

// // console.log(fibonacci("apple"));
// // console.log(fibonacci(10));
// console.log("0:" + fibonacci(0));
// console.log("1:" + fibonacci(1));
// console.log("2:" + fibonacci(2));
// console.log("3:" + fibonacci(3));
// console.log("4:" + fibonacci(4));
// console.log("5:" + fibonacci(5));
// console.log("6:" + fibonacci(6));
// console.log("7:" + fibonacci(7));
// console.log("8:" + fibonacci(8));
// console.log("9:" + fibonacci(9));

module.exports = fibonacci;
