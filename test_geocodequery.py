import unittest2


class TestGeocodeQuery(unittest2.TestCase):

	def _getTargetClass(self):
		from geocodequery import GeocodeQuery
		return GeocodeQuery

	def _makeOne(self, *args, **kw):
		return self._getTargetClass()(*args, **kw)

	def test_defualt_url(self):
		gq = self._makeOne()
		self.assertEqual(gq.url,
			'https://maps.googleapis.com/maps/api/geocode/json?language=None&region=None&sensor=false')

	def test_cus_url(self):
		gq = self._makeOne("zh-tw","tw")
		self.assertEqual(gq.url,
			'https://maps.googleapis.com/maps/api/geocode/json?language=zh-tw&region=tw&sensor=false')

	def test_defult_jsonResponse(self):
		gq = self._makeOne()
		self.assertEqual(gq.jsonResponse, {})

	def test_get_geocode_empty(self):
		gq = self._makeOne()
		gq.get_geocode("")
		self.assertEqual(gq.jsonResponse['results'], [])
