import blankImg from './assets/blank.png'
import axios from 'axios'
import './App.css'

function App() {

  const setImage = (strId, strUrl) => {
    // Sets the provided image tag to the provided url
    const thisImage = document.getElementById(strId);
    thisImage.src = strUrl;
  }

  const setName = (strId, strName) => {
    // Sets the provided name tag to the provided name
    const thisName = document.getElementById(strId);
    thisName.innerText = strName;
  }

  const setHeading = (strType) => {
    // Changes the page heading to the selected pokemon type

    // Create a title from the provided type
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

      let typeArrayResponse = await axios.get('https://pokeapi.co/api/v2/type');

      let thisTypeArray = typeArrayResponse.data.results;

      let pokemonInType = 0;

      do {
        let randomTypeNum = getRandomId(thisTypeArray.length);

        // This is odd behavior, why is this happening?
        if (isNaN(randomTypeNum)) { continue; }

        console.log(`Type Random num ${randomTypeNum}`)
        thisTypeArray = thisTypeArray[randomTypeNum];

        console.log(`Type Array ${thisTypeArray}`)

        let thisTypeUrl = ""

        if(thisTypeArray.url) {
          thisTypeUrl = thisTypeArray.url;
        } else {
          continue;
        }

        let thisTypeSelectionResponse = await axios.get(thisTypeUrl);

      // verify that there are pokemon in the type

        pokemonInType = thisTypeSelectionResponse.data.pokemon;
      } while (pokemonInType < 1 && !isNaN(pokemonInType));


      let thisTypeName = thisTypeArray.name;
      if(pokemonInType.length === 0) {
        console.log(`No pokemon in type ${thisTypeName}`)
      }

      let arrPokemonSelected = [];

      for(let intIndex = 0; intIndex < 6; intIndex++) {
        const thisRandNum = getRandomId(pokemonInType.length);
        console.log(`Type: ${thisTypeName} Random Num: ${thisRandNum} Length: ${pokemonInType.length}`)
        const thisPokemon = pokemonInType[thisRandNum];

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

        let objPokemonSelected = {
          'name': thisPokemon.pokemon.name,
          'url': thisPokemon.pokemon.url,
          'name_tag': strName,
          'image_tag': strImg
        };

        objPokemonSelected.image = await getPokemonImage(objPokemonSelected.url);



        arrPokemonSelected.push(objPokemonSelected);
      }

      setHeading(thisTypeName);
      for(let thisPoke of arrPokemonSelected) {
        console.log(`Loop ${thisPoke} img ${thisPoke.image} in ${thisPoke.image_tag} PokeUrl ${thisPoke.url}`)
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
