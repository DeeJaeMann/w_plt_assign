import { useState, useEffect } from 'react';
import { useLoaderData } from 'react-router-dom';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import RnMCard from '../components/RnMCard';
import getCharacters from '../lib/getCharacters';

function CharactersPage() {
    /*
        Should render a BootStrap Card Component
            Display image and info for identified character
        Get all characters from Rick and Morty API
            https://rickandmortyapi.com/
     */
    // This is an array of character objects
    const data = useLoaderData();
    const [arrCharacterObj, setArrCharacterObj] = useState(data);

    console.log(arrCharacterObj)
    console.log(arrCharacterObj[0].name)
    // console.log("Loader Data", data)
    // setArrCharacterObj(data)

    // Call the API to populate arrCharacterObj
    // This works now
    // useEffect(() => {
    //     // setArrCharacterObj(getCharacters());
    //     getCharacters().then(res =>{
    //         setArrCharacterObj(res)
    //     }).catch(error => {
    //         console.error(error)
    //     })
    // }, []);

 
    return (
        <>
            <Container className="container-fluid">
                <Container className="text-center">
                    <h2>The Characters</h2>
                </Container>
                <Container fluid>
                    <Row className="justify-content-center">
                        <p>List</p>
                        <ul>
                            {/* {renderLine()} */}
                            {arrCharacterObj.map((char, i) => <li key={i}>Name:{char.name}</li>)}
                            <li>testing</li>
                            {/* <li>{arrCharacterObj[1].name}</li> */}
                            {/* Length: {arrCharacterObj.length} */}
                        </ul>
                        {/* <p>Bottom of list Length {arrCharacterObj.length}</p> */}
                    {/* {arrCharacterObj.map((char, i) => {
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
                    / > }) } */}
                    </Row>
                </Container>
            </Container>
        </>
    );
}

export default CharactersPage;