
function InputForm({newGuessInput, processNewGuessInput, validateNewGuess, count}) {

    return (
        <>
            <form>
                <span>Please guess a letter: </span>
                <input type="text" onChange={processNewGuessInput} id="guessInput" size="1" maxLength="1" value={newGuessInput}></input>
                <button id="btnSubmit" onClick={validateNewGuess}>Submit Guess</button>
                {/* <p>Guesses: {count}</p> */}
                {/* <p>Guessed Letters: {guessedLetters}</p> */}
            </form>

        </>
    );
}

export default InputForm;