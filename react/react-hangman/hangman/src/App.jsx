import { useState, useEffect, useCallback } from 'react';
import PuzzleWord from './PuzzleWord.jsx';
import InputForm from './InputForm.jsx';
import MissedGuesses from './MissedGuesses.jsx';
import wordsData from './data/words.json';
import './App.css';

function App() {
  const [guessedLetters, setGuessedLetters] = useState([]);
  const [newGuessInput, setNewGuessInput] = useState("");
  const [count, setCount] = useState(0);


  // Generates a random word from the length of wordsData to set as the answer
  let getRandomWord = () => wordsData[Math.floor(Math.random() * wordsData.length)];

  const checkLetters = useCallback(() => {
    // Build a reverse pattern from the guessed letters
    // console.log(`Guessed Letters: ${guessedLetters}`)
    const reNotGuessedLetters = new RegExp(`[^${guessedLetters.join("")}]`, "g");

    // replace every letter that does not match the pattern with an underscore
    let newString = puzzle.replace(reNotGuessedLetters, '_');
    // Use look-arounds to insert spaces between each word character
    newString = newString.replace(/(?<=\w)(?=\w)/g, " ");

    // alert(newString)
    console.log(`Check Letters: ${newString}`)
    return(newString);

  })

  const [puzzle, setPuzzle] = useState(getRandomWord);
  // This could be moved into PuzzleWord
  const [lettersDisplay, setLettersDisplay] = useState(checkLetters)

  // This wasn't working correctly when in InputForm
  const processNewGuessInput = (event) => setNewGuessInput(event.target.value);

  const validateNewGuess = (event) => {
    // Checks if the input is valid: 
    // - is it a letter?
    // - is it a new guess?
    event.preventDefault();

    // RegEx pattern to test for letters
    const reLetters = /[a-z]/i;

    // Test if our input is a letter
    if(reLetters.test(newGuessInput)) {
        // Build a RegEx pattern to test if this letter has been guessed before
        const reGuessedLetters = new RegExp(`[${guessedLetters.join("")}]`);

        // Test our previous guesses vs our new input
        if(reGuessedLetters.test(newGuessInput)) {
            // Already guessed this letter
            alert("This letter has already been guessed!")
            // Reset input
            setNewGuessInput("");
        } else {
            // Add this guess to guessed letters
            // console.log(`Adding Letter ${newGuessInput}`)
            setCount((count) => count + 1)
            setGuessedLetters([...guessedLetters, newGuessInput.toLowerCase()].sort());
            // console.log(`Guessed Letters are: ${guessedLetters}`)
            // Reset input
            setNewGuessInput("")
            // checkLetters();
            // setLettersDisplay(checkLetters)
        }
    } else {
        // Something other than a letter was entered
        alert("Please only input letters!")
        // Reset input
        setNewGuessInput("")
    }

  } // End validateNewGuess

  useEffect(() => {
    setLettersDisplay(checkLetters)
  }, [guessedLetters, checkLetters]);

  // Output word to console for debugging
  console.log(puzzle)


  // Add component to display incorrect guesses
  return (
    <>
      <div className="mainContainer">
        <h1 className="headingText">Hangman</h1>
        <div className="puzzleContainer">
          <PuzzleWord 
          puzzle={puzzle}
          lettersDisplay={lettersDisplay}
          />
        </div>
        <div className="inputContainer">
          <InputForm 
          guessedLetters={guessedLetters}
          validateNewGuess={validateNewGuess}
          newGuessInput={newGuessInput}
          processNewGuessInput={processNewGuessInput}
          count={count}
          />
        </div>
        <div className="missedContainer">
          <MissedGuesses
          puzzle={puzzle}
          guessedLetters={guessedLetters}
          />
        </div>
      </div>
    </>
  )
}

export default App
