function MissedGuesses ({puzzle, guessedLetters}) {

    // Pattern to match all of the letters in the answer
    const rePuzzle = new RegExp(`[${puzzle}]`, "g")
    // convert guessedLetters into a string
    let missedGuesses = guessedLetters.join("")
    // replace all letters found in the answer with a blank space
    missedGuesses = missedGuesses.replace(rePuzzle, "")
    missedGuesses = missedGuesses.replace(/(?<=\w)(?=\w)/g, " ");

    return (
        <>
            <p>Incorrect Guesses: {missedGuesses}</p>
        </>
    );

}

export default MissedGuesses;