import MapSection from './components/Map';
import './App.css';

const location = {
  address: '1600 Amphitheatre Parkway, Mountain View, california.',
  lat: 37.42216,
  lng: -122.08427,
}; // our location object from earlier

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          PORTLAND TRAILS
        </p>
      </header>
      <body>
      <MapSection location={location} zoomLevel={17} />
      </body>
    </div>
  );
}

export default App;
