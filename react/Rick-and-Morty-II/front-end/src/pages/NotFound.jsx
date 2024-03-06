import RnMNavBar from "../components/RnMNavBar";


function NotFound() {
    return (
        <>
            <RnMNavBar />
            <div className="container-fluid">
                <div className="text-center">
                    <h2 className="bg-warning text-dark">These are not the droids you are looking for!</h2>
                    <p>This page does not exist.</p>
                </div>
            </div>
        </>
    );
}

export default NotFound;