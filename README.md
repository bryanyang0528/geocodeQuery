#geocodeQuery
============

You can get the imformation of geocode easily using this module.

This module is a wrapper of `google geocode api`
(https://developers.google.com/maps/documentation/geocoding/#GeocodingRequests)

**Geocoding** is the process of converting addresses *(like "1600 Amphitheatre Parkway, Mountain View, CA")* into geographic coordinates *(like latitude 37.423021 and longitude -122.083739)*, which you can use to place markers or position the map.

##Object
geocodequery.**GeocodeQuery(*language*, *region*)**
 Only class for query geocode, have two parameters.
 
 `language`(defult = *None*)-The language in which to return results.See the list of 
 supported domain languages. Note that we often update supported languages so this
 list may not be exhaustive. If language is not supplied, the geocoder will attempt
 to use the native language of the domain from which the request is sent wherever possible.
 
 `region`(defult = *None*) - The region code, specified as a ccTLD ("top-level domain") 
 two-character value. This parameter will only influence, not fully restrict, results 
 from the geocoder.

##Functions

* **get_geocode**(*address*)

`address` - The street address that you want to geocode, in the format used by the national
postal service of the country concerned. Additional address elements such as business names
and unit, suite or floor numbers should be avoided. 

`return` - nothing

* **get_lat()**

`return` - return the geocoded latitude value

* **get_lng()**

`return` - return the geocoded longitude value

* **get_cuntry()** *（相當於縣市等級）*

`return` - return a second-order civil entity below the country level. 
Within the United States, these administrative levels are counties. 
Not all nations exhibit these administrative levels.

* **get_area()** *（相當於行政區等級）*

`return` - return a third-order civil entity below the country level. 
This type indicates a minor civil division. Not all nations exhibit these 
administrative levels.

##Usage Limits
Users of the free API:
* **2,500** requests per 24 hour period.
* 5 requests per second.

##Examples

```python
from geocodequery import GeocodeQuery
gq = GeocodeQuery("zh-tw", "tw")
addr = "台北市館前路一段一號"
gq.get_geocode(addr)
gq.get_lat()
```

## Reverse query
Now you can query address by passing lat and lng!
It's from [google API](https://developers.google.com/maps/documentation/geocoding/#ReverseGeocoding)

**but I only implement query country function lol**

##Example
```python
#in python
from geocodequery import GeocodeQueryReverse
gqr = GeocodeQueryReverse(40.714224,-73.961452)
gqr.get_country() #United States
```
```shell
#you can query country in the command line
# python geocodequery.py [reverse] [lat] [lng] [country]
$ python geocodequery.py reverse 30.060797 130.530725 country
Japan
```

