from django.shortcuts import render
import opencage.geocoder
import phonenumbers
from phonenumbers import geocoder,carrier
import folium
import opencage
from opencage.geocoder import OpenCageGeocode
Key = "10782f255d3a4697ab2d66aa16559575"




def Geolocation_Tracker(request):

    if request.method == 'POST':
        number = request.POST['number']
        check_number = phonenumbers.parse(number)
        location = geocoder.description_for_number(check_number,'en')
        service_provider = carrier.name_for_number(check_number,"en")

        position = OpenCageGeocode(Key)
        query = str(location)
        results = position.geocode(query)
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']


        map_location = folium.Map(location=[latitude,longitude],zoom_start=9)
        folium.Marker([latitude,longitude],popup=location).add_to(map_location)
        map_location.save('./templates/Geolocation_Tracker/mapLocation.html')

        return render(request,'Geolocation_Tracker/mapLocation.html')

    return render(request,'Geolocation_Tracker/Geolocation_Tracker.html')