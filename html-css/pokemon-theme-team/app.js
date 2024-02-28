

function setImage(strId, strUrl) {
    // Sets the provided image tag to the provided url
    let thisImage = document.getElementById(strId)
    thisImage.src = strUrl
}

function setName(strId, strName) {
    // Sets the provided name tag to the provided name
    let thisName = document.getElementById(strId)
    thisName.innerText = strName
}

function setHeading(strType) {
    // Changes the page heading to the selected pokemon type

    // create a title from the provided type
    strTitle = `${strType.charAt(0).toUpperCase()}${strType.substring(1)}`

    let thisHeading = document.getElementById("teamHeading")
    thisHeading.innerText = `Pokemon Team: ${strTitle}`
}

function getRandomId(intIndex) {
    // Generates a random number from the index provided
    return Math.floor(Math.random() * intIndex)
}

const getPokemonImage = async (strUrl) => {
    // Requests the individual pokemon data from the api and returns the front_default sprite
    const pokemonResponse = await axios.get(strUrl)

    return pokemonResponse.data.sprites.front_default

}

const generateTeam = async (event) => {
    // Main logic executed when button is pressed
    // Requests a type from the pokemon api and gets 6 random pokemon from the type object

    try{
        // prevent default page reload upon submit
        event.preventDefault();

        // request all of the pokemon types
        const typeArrayResponse = await axios.get('https://pokeapi.co/api/v2/type')

        let thisTypeArray = typeArrayResponse.data.results

        // pick a random type from the length of the array
        thisTypeArray = thisTypeArray[getRandomId(thisTypeArray.length)]

        const thisTypeUrl = thisTypeArray.url
        const thisTypeName = thisTypeArray.name

        // Set the page H1 to the type name (formatted as a title)
        setHeading(thisTypeName)

        // request the type endpoint from the api
        const thisTypeSelectionResponse = await axios.get(thisTypeUrl)

        // This is the array of pokemon for the type we have selected
        let pokemonInType = thisTypeSelectionResponse.data.pokemon

        // Initialize our array to store our choosen pokemon objects
        // (array of objects)
        let arrPokemonSelected = []

        // We're looping to pick 6 random pokemon
        for(let intIndex = 0; intIndex < 6; intIndex++) {
            // select a random pokemon from the array
            let thisPokemon = pokemonInType[getRandomId(pokemonInType.length)]

            // Set our tag ids so we can iterate through the array to perform page modifications

            strName = "name"
            strImg = "img"

            switch (intIndex) {
                case 0 :
                    strName += "One"
                    strImg += "One"
                    break
                case 1 :
                    strName += "Two"
                    strImg += "Two"
                    break
                case 2 :
                    strName += "Three"
                    strImg += "Three"
                    break
                case 3 :
                    strName += "Four"
                    strImg += "Four"
                    break
                case 4 :
                    strName += "Five"
                    strImg += "Five"
                    break
                case 5 :
                    strName += "Six"
                    strImg += "Six"
                    break   
            }

            // Object for our selected pokemon
            let objPokemonSelected = {
                'name': thisPokemon.pokemon.name,
                'url': thisPokemon.pokemon.url,
                'name_tag': strName,
                'image_tag': strImg
            }
            // Use the url key to get the associated image
            objPokemonSelected.image = await getPokemonImage(objPokemonSelected.url)

            // add the completed object to our array
            arrPokemonSelected.push(objPokemonSelected)
        }

        // Iterate through each pokemon object in the array and make the changes to the page
        for(thisPoke of arrPokemonSelected) {
            // Sets the image from the dictionary and image_tag
            setImage(thisPoke.image_tag, thisPoke.image)
            // Sets the name from the dictionary and name_tag
            setName(thisPoke.name_tag, thisPoke.name)
        }

    }
    catch(error) {
        // pop-up an error to the browser
        alert(error);
    }
}