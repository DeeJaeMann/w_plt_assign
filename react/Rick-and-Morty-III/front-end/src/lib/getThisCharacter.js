#!/usr/bin/env node
import axios from 'axios'

const APIURL = "https://rickandmortyapi.com/api/character/"

const getThisCharacter = async (intID) => {
    try {
        const response = await axios.get(`${APIURL}${intID}`);

        const objThisChar = await response.data;

        return objThisChar;

    } catch(error) {
        console.error(`getThisCharacter Error: ${error}`);
    }
}

// getThisCharacter(2).then(res => {
//     console.log(res)
// }).catch(error => {
//     console.error(error)
// })

export default getThisCharacter;