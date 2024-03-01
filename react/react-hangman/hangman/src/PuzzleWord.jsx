import { useState } from 'react'


function PuzzleWord ({puzzle, lettersDisplay}) {

    // console.log(`PuzzleWord Comp: ${puzzle}`)

    return (
        <>
            <p>Answer: {puzzle}</p>
            <p>Output: {lettersDisplay}</p>

        </>
    )
}

export default PuzzleWord;