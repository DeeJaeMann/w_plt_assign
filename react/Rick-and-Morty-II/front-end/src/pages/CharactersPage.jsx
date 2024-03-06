import { useState, useEffect } from 'react';
import axios from 'axios';

function CharactersPage() {
    /*
        Should render a BootStrap Card Component
            Display image and info for identified character
        Get all characters from Rick and Morty API
            https://rickandmortyapi.com/
     */
    // This is an array of character objects
    const [arrCharacterObj, setArrCharacterObj] = useState([]);

 
    useEffect(() => {
        const getCharacters = async () => {
            try {
                let intPageCount = 1;
                let boolNextPage = true;

                do {
                    // Request all character data from the API
                    const response = await axios.get(`https://rickandmortyapi.com/api/character/?page=${intPageCount}`);
                    // Check if there is a next page
                    response.data.info.next ? boolNextPage = true : boolNextPage = false

                    const arrTheseChars = response.data.results;
                    // console.log(arrTheseChars)

                    intPageCount++;
                    setArrCharacterObj(await [...arrCharacterObj, arrTheseChars])
                } while (boolNextPage);
                
                // console.log(response.data);
            } catch (error) {
                console.error(`An error occured: ${error}`);
            }
        };

        getCharacters();
        console.log(`After getCharacters() ${arrCharacterObj}`)
    }, []);



    return (
        <>
            <div className="container-fluid">
                <div className="text-center">
                    <h2>The Characters</h2>
                </div>
            </div>
        </>
    );
}

export default CharactersPage;