import { useState, useEffect } from 'react';
import axios from 'axios';
import RnMCard from '../components/RnMCard';

function CharactersPage() {
    /*
        Should render a BootStrap Card Component
            Display image and info for identified character
        Get all characters from Rick and Morty API
            https://rickandmortyapi.com/
     */
    // This is an array of character objects
    const [arrCharacterObj, setArrCharacterObj] = useState([]);

    // Call the API to populate arrCharacterObj
    useEffect(() => {
        const getCharacters = async () => {
            try {
                // Initialize variables for the do-while loop
                let intPageCount = 1;
                // For safety, assume we have no more pages.  The loop will correct this
                let boolNextPage = false;

                // Use a do-while loop to iterate through the API pages to populate the characters into an array of objects
                // I am using a do-while because this loop is designed to run at least once through an unknown amount of pages
                // This is designed to continue to work if the amount of pages changes in the future
                do {
                    // Request all character data from the API
                    const response = await axios.get(`https://rickandmortyapi.com/api/character/?page=${intPageCount}`);

                    const arrTheseChars = await response.data.results;
                    // Map each array element into an object
                    arrTheseChars.map((char) => {
                        const objThisChar = {
                            'id': char.id,
                            'name': char.name,
                            'status': char.status,
                            'type': char.type,
                            'gender': char.gender,
                            'origin': char.origin,
                            'location': char.location,
                            'image': char.image,
                            'url': char.url

                        }
                        // Add the object to the arrCharacterObj array
                        setArrCharacterObj([...arrCharacterObj, objThisChar])
                    })

                    // Check if there is a next page, this is our loop condition
                    await response.data.info.next ? boolNextPage = true : boolNextPage = false

                    console.log(`Page: ${intPageCount}`)
                    // Incriment page count
                    intPageCount++;
                
                // Continue the loop until we have no next page
                } while (boolNextPage);
                
                // console.log(response.data);
            } catch (error) {
                console.error(`An error occured: ${error}`);
            }
        };

        getCharacters();
    }, []);


    return (
        <>
            <div className="container-fluid">
                <div className="text-center">
                    <h2>The Characters</h2>
                </div>
                <div>
                    {arrCharacterObj.map((char, i) =>
                    <div key={i}>
                    <RnMCard 
                        key={i}
                        intID={char.id}
                        imgSrc={char.image}
                        strName={char.name}
                        strStatus={char.status}
                        strSpecies={char.species}
                        strType={char.type}
                        strGender={char.gender}
                        strOrigin={char.origin.name}
                        strLocation={char.location.name}
                    / > </div>)}
                </div>
            </div>
        </>
    );
}

export default CharactersPage;