import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';


const RnMNavBar = () => {
    return (
        <>
            <Navbar expand="lg" className="tw-bg-purple-300 border border-info rounded-bottom sticky-top">
                <Container className="d-flex align-items-start m-0">
                    <Navbar.Brand as={Link} to="/" className="bg-dark text-white p-2 rounded">
                        <img
                            src="/src/assets/rick-morty-11.png"
                            width="30"
                            height="30"
                            className="d-inline-block pb-2"
                            alt="Rick and Morty Image"
                        />
                        <span className="p-2 fs-3">Rick and Morty Explorer</span>
                    </Navbar.Brand>
                    <Nav.Item>
                        <Nav.Link as={Link} to="/about" title="About" className="fs-5 badge bg-secondary">
                            About
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link as={Link} to="/characters" title="Characters" className="fs-5 badge bg-secondary">
                            Characters
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link as={Link} to="/smurfs" title="Error Page" className="fs-5 badge bg-danger">
                            Error Page Test
                        </Nav.Link>
                    </Nav.Item>
                </Container>
            </Navbar>
        </>
    );
}

export default RnMNavBar;