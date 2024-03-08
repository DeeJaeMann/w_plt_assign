import { useState } from 'react';
import { useLoaderData } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import RnMCard from '../components/RnMCard'
// import getThisCharacter from '../lib/getThisCharacter'

const CharacterDetailsPage = () => {
    const objCharacterData = useLoaderData();
    const [objThisCharacter, setThisCharacter] = useState(objCharacterData)


    return (
        <>
            <Container className="container-fluid">
                <Container className="text-center tw-bg-purple-600">
                    <h2 className="m-0 py-2 text-light">Character Details</h2>
                </Container>
                <Container fluid className="tw-bg-purple-600 p-2 rounded-bottom">
                    {<RnMCard
                        intID={objThisCharacter.id}
                        imgSrc={objThisCharacter.image}
                        strName={objThisCharacter.name}
                        strStatus={objThisCharacter.status}
                        strSpecies={objThisCharacter.species}
                        strType={objThisCharacter.type}
                        strGender={objThisCharacter.gender}
                        strOrigin={objThisCharacter.origin.name}
                        strLocation={objThisCharacter.location.name}
                    />}
                </Container>
            </Container>
        </>
    )
}

export default CharacterDetailsPage