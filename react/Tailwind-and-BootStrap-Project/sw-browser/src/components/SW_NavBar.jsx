import { useState, useEffect, useCallback } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar'
import NavDropdown from 'react-bootstrap/NavDropdown'; 

function SW_NavBar ({vehicleData, maxVehicles, selectedVehicle, setSelectedVehicle}) {

    // const renderVehicle = (vehicle) => {
        // console.log(`renderVehicle ${vehicle.name}`)
        // return(`<NavDropdown.Item href=#home">${vehicle.name}</NavDropdown.Item>`)
    // }

    const updateSelectedVehicle = useCallback((objVehicle) => {
        // This updates the state of selectedVehcile
        // useCallback seemed to be the only thing that worked to send it back to the main app
        setSelectedVehicle(objVehicle)
        console.log(`upSelVic ${objVehicle}`)
    }, [setSelectedVehicle])

    const handleVehicleSelect = (eventKey) => {
        // This takes the selected eventKey from the dropdown menu, gets the matching object._id from
        // vehicleDatan and sends tha tobject to updateSelectedVehicle to update the state
        const selectedObject = vehicleData.filter((vehicle) => vehicle._id === eventKey );
        console.log(`handleVicSel: selectedObject is ${selectedObject}`)
        console.log(`eventKey is ${eventKey}`)
        // setSelectedVehicle(selectedObject)
        updateSelectedVehicle(selectedObject)

    }

    const updateDropdownDisplay = () => {
        // This renders the title of the Navbar depending on whether a vehicle has been selected or not
        // Currently does not update when selectedVehicle changes
        // NOTE: useCallback does not update the '# Vehicles' upon start properly
        // NOTE: This returns a value to update a Bootstrap Component, useEffect does not return to the component(?)
        return(selectedVehicle.name === undefined ? `${maxVehicles} Vehicles` : `Selected: ${selectedVehicle.name}`)
    };

    return (
        <>
            <Container style={{justifyContent:"center", alignContent:"center"}}>
                <Navbar sticky="top" expand="lg" className="bg-body-tertiary">
                    <Row>
                        
                        <Col xs="auto" style={{border: "2px solid black"}}>
                            <Navbar.Brand href="#">SW-Browser</Navbar.Brand>
                        </Col>
                        <Col xs="auto"></Col>
                        <Col xs="auto" style={{border: "2px solid black", justifyContent:"space-between"}}>

                                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                                <Navbar.Collapse id="basic-navbar-nav">
                                    <Nav className="me-auto" onSelect={handleVehicleSelect}>
                                    <Nav.Link href="#home">Home</Nav.Link>
                                    <Nav.Link href="https://starwars-databank.vercel.app/" target="_blank">Star Wars Databank</Nav.Link>
                                    <NavDropdown title={updateDropdownDisplay()} id="basic-nav-dropdown">
                                        {vehicleData.map((vehicle, i) => (
                                            <NavDropdown.Item key={i} eventKey={vehicle._id} aria-selected="false"  href={vehicle.image} target="_blank">{vehicle.name}</NavDropdown.Item>
                                        ))}
                                        {/* <NavDropdown.Item href="#home">Placeholder</NavDropdown.Item> */}
                                    </NavDropdown>
                                    </Nav>
                                </Navbar.Collapse>
                        </Col>
                        
                    </Row>
                </Navbar>
                <p>Testing Selected Vehicle: {selectedVehicle.name}</p>  
            </Container>    
        </>
    )
}

export default SW_NavBar;