
const replaceImages = () => {
    let images = document.body.getElementsByTagName('img')

    for(let intI = images.length - 1; intI >= 0; intI--) {
        let thisImage = images[intI]
 

        if(thisImage.alt) {

            let thisAlt = document.createTextNode(thisImage.alt)
            thisImage.parentNode.replaceChild(thisAlt, thisImage)
        }
    }
   

}