import geocoder
from kivy.app import App
from kivy_garden.mapview import MapView,MapMarker

class MapViewApp(App):
    def build(self):

        g = geocoder.ip('me')
        lat, lon = g.latlng
        mapview = MapView(zoom=20, lat=lat, lon=lon)
        marker = MapMarker(lat=lat, lon=lon, source='image\icon\your_location@36.png')
        mapview.add_marker(marker)
        return mapview

MapViewApp().run()
