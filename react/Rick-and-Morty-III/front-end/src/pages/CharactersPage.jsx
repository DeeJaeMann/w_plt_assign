import { useState } from 'react';  // useEffect removed, using useLoaderData instead
import { useLoaderData, Link, useNavigate } from 'react-router-dom';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import RnMCard from '../components/RnMCard';
import Button from 'react-bootstrap/Button';
// import getCharacters from '../lib/getCharacters';  // Not needed here anymore, using useLoaderData instead of useEffect

const CharactersPage = () => {
    /*
        Should render a BootStrap Card Component
            Display image and info for identified character
        Get all characters from Rick and Morty API
            https://rickandmortyapi.com/
     */
    // This is an array of character objects
    const arrCharacterData = useLoaderData();
    const [arrCharacterObj, setArrCharacterObj] = useState(arrCharacterData);
    const navigate = useNavigate();

    // console.log(arrCharacterObj)
    // console.log(arrCharacterObj[0].name)

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

    const processButtonClick = (intID) => {
        navigate(`/character/${intID}`);
    }
 
    return (
        <>
            <Container className="container-fluid">
                <Container className="text-center tw-bg-purple-600">
                    <h2 className="m-0 text-light">The Characters</h2>
                </Container>
                <Container fluid className="">
                    <Row className="justify-content-between" xs={1} sm={1} md={1} lg={2}>
                    {arrCharacterObj.map((char, i) =>
                    <Container key={i} className="tw-bg-purple-600">
                    <RnMCard
                        intID={char.id}
                        imgSrc={char.image}
                        strName={char.name}
                        strStatus={char.status}
                        strSpecies={char.species}
                        strType={char.type}
                        strGender={char.gender}
                        strOrigin={char.origin.name}
                        strLocation={char.location.name}
                    / >
                    </Container>)}
                    </Row>
                </Container>
            </Container>
        </>
    );
}

export default CharactersPage;