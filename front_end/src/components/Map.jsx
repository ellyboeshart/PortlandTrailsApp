import React from 'react'
import GoogleMapReact from 'google-map-react'
import { Icon } from '@iconify/react'

import './map.css'

const LocationPin = ({ text }) => (
  <div className="pin">
    <Icon icon="mdi-light:home" className="pin-icon" />
    <p className="pin-text">{text}</p>
  </div>
)

const Map = ({ location, zoomLevel }) => (
  <div className="map">
    <h2 className="map-h2">Welcome, PDX Hikers!</h2>

    <div className="google-map">
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'AIzaSyAYEecq-0vewqtZUphgIFOZb6LM0ddbIiw' }}
        defaultCenter={location}
        defaultZoom={zoomLevel}
      >
        <LocationPin
          lat={location.lat}
          lng={location.lng}
          text={location.address}
        />
      </GoogleMapReact>
    </div>
  </div>
)

export default Map