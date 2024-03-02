
function InputForm({newGuessInput, processNewGuessInput, validateNewGuess, count}) {

    return (
        <>
            <hr></hr>
            <form>
                <input type="text" onChange={processNewGuessInput} id="guessInput" size="1" maxLength="1" value={newGuessInput}></input>
                <button onClick={validateNewGuess}>Submit Guess</button>
                <p>Guesses: {count}</p>
                {/* <p>Guessed Letters: {guessedLetters}</p> */}
            </form>

        </>
    );
}

export default InputForm;