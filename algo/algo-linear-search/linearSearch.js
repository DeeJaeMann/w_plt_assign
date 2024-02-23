#!/usr/bin/env node

/**
 * Performs a sequential search of a given array provided with a searh criteria
 * @param {any} searchTerm Criteria to search for
 * @param {array} arr Array to search
 * @returns Index of element in array where criteria found, undefined if not found
 */
function linearSearch(searchTerm, arr) {
  // Iterate through the array and compare if this index matches our search criteria
  for (let intIndex = 0; intIndex < arr.length + 1; intIndex++) {
    if (arr[intIndex] === searchTerm) {
      return intIndex;
    }
  }
  return undefined;
}

/**
 * Performs a sequential search of a given array and returns all of the indexes found
 * @param {any} searchTerm Criteria to search for
 * @param {*} arr Array to search
 * @returns Array of indexes where criteria was found or empty array if not found
 */
function globalLinearSearch(searchTerm, arr) {
  let arrResult = [];

  // Iterate through the array and compare if this index matches our criteria
  for (let intIndex = 0; intIndex < arr.length; intIndex++) {
    if (arr[intIndex] === searchTerm) {
      arrResult.push(intIndex);
    }
  }
  // Return array of indexes found
  return arrResult;
}

//console.log(globalLinearSearch('a', 'bannanas'.split('')));

module.exports = { linearSearch, globalLinearSearch };
