import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';


const RnMNavBar = () => {
    return (
        <>
            <Navbar expand="lg" className="tw-bg-purple-300 border border-secondary rounded-bottom sticky-top">
                <Container className="d-flex align-items-start m-0">
                    <Navbar.Brand as={Link} to="/" className="bg-dark text-white p-2 rounded">
                        <img
                            src="/src/assets/rick-morty-11.png"
                            width="30"
                            height="30"
                            className="d-inline-block align-top"
                            alt="Rick and Morty Image"
                        />
                        <span className="p-2">Rick and Morty Explorer</span>
                    </Navbar.Brand>
                    <Nav.Item>
                        <Nav.Link as={Link} to="/about" title="About">
                            About
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link as={Link} to="/characters" title="Characters">
                            Characters
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link as={Link} to="/smurfs" title="Error Page">
                            Error Page Test
                        </Nav.Link>
                    </Nav.Item>
                </Container>
            </Navbar>
        </>
    );
}

export default RnMNavBar;