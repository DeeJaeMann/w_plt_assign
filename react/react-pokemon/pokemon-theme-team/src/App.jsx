import blankImg from './assets/blank.png'
import axios from 'axios'
import './App.css'

function App() {

  // State?
  const setImage = (strId, strUrl) => {
    // Sets the provided image tag to the provided url
    const thisImage = document.getElementById(strId);
    thisImage.src = strUrl;
  }

  // State?
  const setName = (strId, strName) => {
    // Sets the provided name tag to the provided name
    const thisName = document.getElementById(strId);
    thisName.innerText = strName;
  }

  // State?
  const setHeading = (strType) => {
    // Changes the page heading to the selected pokemon type

    // Create a title from the provided type
    //TODO: Move this to a helper function that can 
    const strTitle = `${strType.charAt(0).toUpperCase()}${strType.substring(1)}`
    const thisHeading = document.getElementById("teamHeading")
    thisHeading.innerText = `Pokemon Team: ${strTitle}`
  }

  const getPokemonImage = async (strUrl) => {
    // Requests the individual pokemon data from the apio and returns the front_default sprite
    const pokemonResponse = await axios.get(strUrl);

    let pokeImg = pokemonResponse.data.sprites.front_default;

    if(pokeImg === null) {
      pokeImg = blankImg;
    }

    return pokeImg;
  }

  const getRandomId = (intIndex) => { return Math.floor(Math.random() * intIndex) }

  const generateTeam = async (event) => {
    // Main logic executed when button is pressed
    // Requests a type from the pokemon api and gets 6 random pokemon from the type object
    try {
      event.preventDefault();

      // This should move to an effect
      // TODO: Move to effect - Get pokeTypes
      let typeArrayResponse = await axios.get('https://pokeapi.co/api/v2/type');

      // State?
      let thisTypeArray = typeArrayResponse.data.results;

      // State?
      let pokemonInType = 0;

      // The reason I used a 'do - while' is to verify that there are elements in the 
      // returned array.  Some pokemon types don't have any 'members' but the types
      // are still returned.  You don't run into the blank array until you query
      // the selected type.
      // The loop uses whether pokemonInType has elements or not
      do {
        let randomTypeNum = getRandomId(thisTypeArray.length);

        // Most likely the NaN is coming from unexpected results from the API
        // It is an intermittent issue, however if we run into it we will restart
        // the loop and get a new random number
        // This is a patch to prevent the app from breaking
        if (isNaN(randomTypeNum)) { continue; }

        // Maybe this should be renamed?  Or rename the previous state of the array
        thisTypeArray = thisTypeArray[randomTypeNum];

        // State?
        let thisTypeUrl = ""

        // Verify if there is a url and assign it if there is
        if(thisTypeArray.url) {
          thisTypeUrl = thisTypeArray.url;
        } else {
          continue;
        }

        // Move to an effect
        //TODO: Determine which effect this goes to
        let thisTypeSelectionResponse = await axios.get(thisTypeUrl);


        pokemonInType = thisTypeSelectionResponse.data.pokemon;

        // verify that there are pokemon in the type, if there are non or the type
        // is not a number, iterate through the loop to get different data
        // the !isNan() part may not be needed anymore due to the validation
        // above
      } while (pokemonInType < 1 && !isNaN(pokemonInType));


      let thisTypeName = thisTypeArray.name;

      let arrPokemonSelected = [];

      for(let intIndex = 0; intIndex < 6; intIndex++) {
        const thisRandNum = getRandomId(pokemonInType.length);
        const thisPokemon = pokemonInType[thisRandNum];

// This can be a helper function
//TODO: Move select/case to helper function that returns array with 2 elements
        let strName = "name";
        let strImg = "img";

        switch(intIndex) {
          case 0 :
            strName += "One";
            strImg += "One";
            break;
          case 1 :
            strName += "Two";
            strImg += "Two";
            break;
          case 2 :
            strName += "Three";
            strImg += "Three";
            break;
          case 3 :
            strName += "Four";
            strImg += "Four";
            break;
          case 4 :
            strName += "Five";
            strImg += "Five";
            break;
          default :
            strName += "Six";
            strImg += "Six";
        }

// end of id helper function

// State variable?
        let objPokemonSelected = {
          'name': thisPokemon.pokemon.name,
          'url': thisPokemon.pokemon.url,
          'name_tag': strName,
          'image_tag': strImg
        };

// This should be the result of an effect
        objPokemonSelected.image = await getPokemonImage(objPokemonSelected.url);


// This should be in state?
        arrPokemonSelected.push(objPokemonSelected);
      }

      setHeading(thisTypeName);
      for(let thisPoke of arrPokemonSelected) {
        setImage(thisPoke.image_tag, thisPoke.image);
        setName(thisPoke.name_tag, thisPoke.name);
      }
    }
    catch(error) {
      console.log(error)
      alert("Something unexpected happened!  Please try again.");
    }
  }

  return (
    <>
        <header>
          <div className="headerContainer">
            <h1 id="teamHeading">Pokemon Team</h1>
          </div>
        </header>
        <main>
          <div className="mainContainer">
            <div id="outerFormContainer"></div>
            <div id="formContainer">
              <form onSubmit={(event) => generateTeam(event)}>
                <button id="btnSubmit">Generate My Team!</button>
              </form>
            </div>
            <div id="outerDisplayContainer">
              <div id="displayContainer">
                <div className="pokeContainer">
                  <p id="nameOne" className="pokeName">Empty</p>
                  <img src={blankImg} id="imgOne" className="pokeImg"></img>
                </div>
                <div className="pokeContainer">
                  <p id="nameTwo" className="pokeName">Empty</p>
                  <img src={blankImg} id="imgTwo" className="pokeImg"></img>
                </div>
                <div className="pokeContainer">
                  <p id="nameThree" className="pokeName">Empty</p>
                  <img src={blankImg} id="imgThree" className="pokeImg"></img>
                </div>
                <div className="pokeContainer">
                  <p id="nameFour" className="pokeName">Empty</p>
                  <img src={blankImg} id="imgFour" className="pokeImg"></img>
                </div>
                <div className="pokeContainer">
                  <p id="nameFive" className="pokeName">Empty</p>
                  <img src={blankImg} id="imgFive" className="pokeImg"></img>
                </div>
                <div className="pokeContainer">
                  <p id="nameSix" className="pokeName">Empty</p>
                  <img src={blankImg} id="imgSix" className="pokeImg"></img>
                </div>
              </div>
            </div>
          </div>
        </main>
    </>
  )
}

export default App
