import { useState, useEffect, useCallback } from 'react';
import axios from "axios";
import SW_NavBar from './components/SW_NavBar';
import './App.css'

function App() {
  const [maxVehicles, setMaxVehicles] = useState(0);
  const [vehicleData, setVehicleData] = useState([]);
  const [selectedVehicle, setSelectedVehicle] = useState({})

  const getMaxVehicles = async () => {
    try {
      const response = await axios.get("https://starwars-databank-server.vercel.app/api/v1/vehicles");
      // console.log(response.data.info.total);
      await setMaxVehicles(response.data.info.total)
      console.log(response.data.info.total)
      // return(response.data.info.total)

    } catch (error) {
      console.error(`Error: getMaxVehicles: ${error}`);
    }
  };

  const getVehicleData = useCallback( async () => {
    try {
      const response = await axios.get(`https://starwars-databank-server.vercel.app/api/v1/vehicles?page=1&limit=${maxVehicles}`);
      // console.log(`getVehicleData: ${response.data.data[1].name}`)
      // return(response.data.data)
      await setVehicleData(response.data.data)

    } catch (error) {
      console.error(`Error: getVehicleData: ${error}`)
    }
  }, []);


  useEffect(() => {
    getMaxVehicles();
    getVehicleData();
  }, [getVehicleData]);

  useEffect(() => {

  })
  // console.log(`last vic data: ${vehicleData}`);

  return (
    <>
      <div className="App">
        <SW_NavBar 
        vehicleData={vehicleData}
        maxVehicles={maxVehicles}
        selectedVehicle={selectedVehicle}
        setSelectedVehicle={setSelectedVehicle}
        />
        <img height="500vw" src={selectedVehicle.image} />
      </div>
    </>
  )
}

export default App
