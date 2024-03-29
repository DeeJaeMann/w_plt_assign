import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import NotFound from "./pages/NotFound";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import CharactersPage from "./pages/CharactersPage";
import getCharacters from "./lib/getCharacters";

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
            }
        ],
        errorElement: <NotFound />
    },
]);

export default router;