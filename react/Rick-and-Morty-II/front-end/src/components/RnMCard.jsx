import { CardText } from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import ListGroup from "react-bootstrap/ListGroup";

function RnMCard({ 
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

            <Card key={intID} className="flex-row m-2" >
                <Card.Img src={imgSrc} className="p-2"/>
                <Card.Body>
                    <Card.Title>{strName}</Card.Title>
                <CardText>
                <ListGroup className="list-group-flush">
                    <ListGroup.Item>Status: {strStatus}</ListGroup.Item>
                    <ListGroup.Item>Species: {strSpecies} {strType}</ListGroup.Item>
                    <ListGroup.Item>Gender: {strGender}</ListGroup.Item>
                    <ListGroup.Item>Origin: {strOrigin}</ListGroup.Item>
                    <ListGroup.Item>Location: {strLocation}</ListGroup.Item>
                </ListGroup>
                </CardText>
                </Card.Body>
            </Card>
    )
}

export default RnMCard;