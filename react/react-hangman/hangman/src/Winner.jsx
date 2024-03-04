import {useState, useEffect, useCallback} from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';



function Winner({puzzle, setPuzzle, setGuessedLetters, getRandomWord, lettersDisplay, setLettersDisplay, checkLetters}) {
    const [show, setShow] = useState(false);

    // console.log("Winner Component Called")

    //TODO: Why is this being called twice?
    const handleClose = () => {
        setShow(false);
        setPuzzle(getRandomWord)
        setGuessedLetters([])
        setLettersDisplay(checkLetters)
    }
    const handleShow = () => setShow(true);

    const checkWinner = useCallback(() => {
        const reWinPattern = new RegExp(`_`, 'g')
        console.log("checkWinner called")
        console.log(`Display ${lettersDisplay}`)

        if(!reWinPattern.test(lettersDisplay)) {
            handleShow();
            console.log("No underscore found!")
        } else {
            console.log("Found underscore!")
        }
    })

    useEffect (() => {
        checkWinner()
    }, [lettersDisplay, checkWinner]);

    return (
        <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>You Win!</Modal.Title>
            </Modal.Header>
            <Modal.Body>You Win!</Modal.Body>
            <Modal.Footer>
                <Button variant="primary" onClick={handleClose}>
                    Close
                </Button>
            </Modal.Footer>
        </Modal>
    )
}

export default Winner;