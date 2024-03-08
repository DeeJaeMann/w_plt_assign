import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import NotFound from "./pages/NotFound";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import CharactersPage from "./pages/CharactersPage";
import CharacterDetailsPage from "./pages/CharacterDetailsPage";
import getCharacters from "./lib/getCharacters";
import getThisCharacter from "./lib/getThisCharacter";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: "about/",
                element: <AboutPage />,
            },
            {
                path: "characters/",
                element: <CharactersPage />,
                loader: getCharacters, // loader: fetchCharacter(id)
            },
            {
                path: "character/:id",
                element: <CharacterDetailsPage/>,
                loader: ({ params }) => getThisCharacter(params.id)
            }
        ],
        errorElement: <NotFound />
    },
]);

export default router;