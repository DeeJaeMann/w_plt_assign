import { Outlet } from "react-router-dom";
import RnMNavBar from "./components/RnMNavBar"
import './App.css';

function App() {

  return (
    <>
      <RnMNavBar />
      <Outlet />
    </>
  );
}

export default App
