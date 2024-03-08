const AboutPage = () => {
    /*
        Should render general 'about me' info from the show
        Use API to render info (what info can you get from the API?)
     */

    return (
        <>
            <div className="container-fluid">
                <div className="text-center">
                    <h2>About the Show</h2>
                    <p><a href="https://www.adultswim.com/videos/rick-and-morty" target="_blank">Rick and Morty</a> is a television show for <a href="https://www.adultswim.com/" target="_blank">Adult Swim</a> created by Justin Roiland and Dan Harmon.</p>
                    <p>TODO:  Get more info from <a href="https://rickandmortyapi.com/" target="_blank">API</a></p>
                    <p>TODO: Style this page</p>
                </div>
            </div>
        </>
    );
}

export default AboutPage;