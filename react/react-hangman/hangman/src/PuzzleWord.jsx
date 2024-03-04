import { useState } from 'react'


function PuzzleWord ({puzzle, lettersDisplay}) {

    // console.log(`PuzzleWord Comp: ${puzzle}`)

    return (
        <>
            {/* <p>Answer: {puzzle}</p> */}
            <h2 className="puzzleText">Puzzle: {lettersDisplay}</h2>

        </>
    )
}

export default PuzzleWord;