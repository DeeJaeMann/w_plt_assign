import RnMNavBar from "../components/RnMNavBar";


const NotFound = () => {
    return (
        <>
            <RnMNavBar />
            <div className="container-fluid">
                <div className="text-center">
                    <h2 className="bg-warning text-danger rounded-bottom p-2">These are not the droids you are looking for!</h2>
                    <p className="text-alert">This page does not exist.</p>
                    <p>TODO: Style this page</p>
                </div>
            </div>
        </>
    );
}

export default NotFound;