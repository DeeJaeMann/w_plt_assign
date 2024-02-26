
const replaceImages = () => {
    // Get an array of the images from the document
    let images = document.body.getElementsByTagName('img')

    // Iterate through the images array
    for(let intI = images.length - 1; intI >= 0; intI--) {

        let thisImage = images[intI]
 
        // Check if this image has an alt
        if(thisImage.alt) {
            // Create a text node from the image alt attribute
            let thisAlt = document.createTextNode(thisImage.alt)
            // Replace the img tag with the text node
            thisImage.parentNode.replaceChild(thisAlt, thisImage)
        }
    }
   
}