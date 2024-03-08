import { CardText } from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import ListGroup from "react-bootstrap/ListGroup";
import Col from 'react-bootstrap/Col';

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

        <Col className="tw-bg-purple-600">
                <Card key={intID} className="flex-row m-2 tw-bg-purple-400 border-info">
                    <Card.Img src={imgSrc} className="p-2 m-0 tw-bg-purple-400 rounded-end-0" style={{width: "18rem", height: "20 rem"}}/>
                    <Card.Body className="tw-bg-blue-300 rounded-end">
                        <Card.Title className="text-center">{strName}</Card.Title>
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
            </Col>
    )
}

export default RnMCard;