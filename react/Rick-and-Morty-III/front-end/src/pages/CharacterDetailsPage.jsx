import { useState } from 'react';
import { useLoaderData } from 'react-router-dom';
import RnMCard from '../components/RnMCard'
// import getThisCharacter from '../lib/getThisCharacter'

const CharacterDetailsPage = () => {
    const objCharacterData = useLoaderData();
    const [objThisCharacter, setThisCharacter] = useState(objCharacterData)


    return (
        <>
            <h2>Character Details</h2>

            {
            <RnMCard
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
        </>
    )
}

export default CharacterDetailsPage