// console.log("HELLO PAPA PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM

let intAnswer = Math.floor(Math.random()*100)

// answerTag = document.getElementById("answer")
// answerTag.textContent = intAnswer

const createHistoryItem = (guess) => {
    let historyContainer = document.getElementById('historyContainer')
    let li = document.createElement('li')

    li.innerText = `${guess}`

    historyContainer.appendChild(li)
}

const submitGuess = (event) => {
    event.preventDefault();
    let frmData = new FormData(event.target)
    let objData = Object.fromEntries(frmData)

    resultTag = document.getElementById("result")
    myGuess = Number(objData['my_guess'])

    // resultTag.textContent = objData['my_guess']
    if(myGuess === intAnswer) {
        resultTag.textContent = "Correct!"
    } else if(myGuess > intAnswer) {
        resultTag.textContent = "High!"
    } else {
        resultTag.textContent = "Low!"
    }

    createHistoryItem(myGuess)
}
