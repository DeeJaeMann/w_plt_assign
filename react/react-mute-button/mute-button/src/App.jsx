import { useState } from 'react'
import imgOnBtn from './assets/icons/on.svg'
import imgOffBtn from './assets/icons/off.svg'
import './App.css'

function App() {

  // State for button (true = on)
  const [imgBtnState, setBtnState] = useState(true)
  
  // Toggles imgBtnState true/false
  const toggleBtn = () => setBtnState(!imgBtnState)

  // Selects which image to render for button
  const renderBtnDisplay = () => imgBtnState ? imgOnBtn : imgOffBtn; 

  return (
    <>
      <div id="mainContainer">
        <img className="imgBtn" src={renderBtnDisplay()} onClick={toggleBtn}></img>
      </div>

    </>
  )
}

export default App
