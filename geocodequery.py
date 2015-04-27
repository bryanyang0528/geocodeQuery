import sys
import urllib, urllib2
import json

class GeocodeQuery:
    def __init__(self, language=None, region=None):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?language={0}&region={1}&sensor=false'.format(language, region)
        self.jsonResponse = {}
            
    def get_geocode(self, addr):
    	addr = urllib.quote(addr)
        url = self.url + '&address={}'.format(addr)
        response = urllib2.urlopen(url)
        self.jsonResponse = json.loads(response.read())
        return self.jsonResponse
        
    def get_lat(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["geometry"]["location"]["lat"]

    def get_lng(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["geometry"]["location"]["lng"]
    
    def get_cuntry(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["address_components"][4]["long_name"]

    def get_area(self):
        if len(self.jsonResponse["results"]) is not 0:
            return self.jsonResponse["results"][0]["address_components"][3]["long_name"]

class GeocodeQueryReverse:
    def __init__(self, lat =None, lng = None, language='en'):
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&language={2}'.format(lat, lng, language)
        response = urllib2.urlopen(url)
        self.jsonResponse = json.loads(response.read())

    def get_country(self):
        if len(self.jsonResponse["results"]) is not 0:
            for item in self.jsonResponse["results"][0]["address_components"]:
                if item["types"][0] == "country":
                    return item["long_name"]

if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print 'usage: geocodeQuery.py [reverse] [lat] [lng] [country/addr]'
        sys.exit(1)

    if (sys.argv[1] == 'reverse' and sys.argv[4] == 'country'):
        gqr = GeocodeQueryReverse(sys.argv[2],sys.argv[3])
        print gqr.get_country()

