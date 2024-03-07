#!/usr/bin/env node
import axios from 'axios';

const APIURL = "https://rickandmortyapi.com/api/character/?page=";

const getCharacters = async () => {
    try {
        // Initialize variables for the do-while loop
        let intPageCount = 1;
        // For safety, assume we have no more pages.  The loop will correct this
        let boolNextPage = false;

        let arrTotalChars = [];

        // Use a do-while loop to iterate through the API pages to populate the characters into an array of objects
        // I am using a do-while because this loop is designed to run at least once through an unknown amount of pages
        // This is designed to continue to work if the amount of pages changes in the future
        do {
            // Request all character data from the API
            const response = await axios.get(`${APIURL}${intPageCount}`);

            const arrTheseChars = await response.data.results;
        
            arrTotalChars.push(...arrTheseChars)
            
            // Check if there is a next page, this is our loop condition
            await response.data.info.next ? boolNextPage = true : boolNextPage = false

            // Incriment page count
            intPageCount++;
        
        // Continue the loop until we have no next page
        } while (boolNextPage);

        return arrTotalChars;
        
    } catch (error) {
        console.error(`getCharacters Error: ${error}`);
    }
};

// console.log(getCharacters());

export default getCharacters