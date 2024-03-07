import Card from 'react-bootstrap/Card';

function RnMCard({key, 
    intID,
    imgSrc, 
    strName,
    strStatus,
    strSpecies,
    strType,
    strGender,
    strOrigin,
    strLocation 
    }) {
    return(

            <Card className="flex-row">
                <Card.Img src={imgSrc} key={key}/>
                <Card.Body>
                    <Card.Title>{strName}</Card.Title>
                    <Card.Text>
                        ID: {intID}<br />
                        Status: {strStatus}<br />
                        Species: {strSpecies} {strType}<br />
                        Gender: {strGender}<br />
                        Origin: {strOrigin}<br />
                        Location: {strLocation}
                    </Card.Text>
                </Card.Body>
            </Card>

    )
}

export default RnMCard;