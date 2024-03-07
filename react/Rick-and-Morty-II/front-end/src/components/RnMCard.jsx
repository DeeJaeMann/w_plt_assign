import { CardText } from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import ListGroup from "react-bootstrap/ListGroup";

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

            <Card className="flex-row" style={{ width: "18rem"}}>
                <Card.Img src={imgSrc} key={key}/>
                <Card.Body>
                    <Card.Title>{strName}</Card.Title>
                </Card.Body>
                <CardText>
                <ListGroup className="list-group-flush">
                    <ListGroup.Item>Status: {strStatus}</ListGroup.Item>
                    <ListGroup.Item>Species: {strSpecies} {strType}</ListGroup.Item>
                    <ListGroup.Item>Gender: {strGender}</ListGroup.Item>
                    <ListGroup.Item>Origin: {strOrigin}</ListGroup.Item>
                    <ListGroup.Item>Location: {strLocation}</ListGroup.Item>
                </ListGroup>
                </CardText>

            </Card>

    )
}

export default RnMCard;