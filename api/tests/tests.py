from django.test import TestCase, SimpleTestCase, TransactionTestCase
from api.models import preexisting_models
from rest_framework.test import APIClient, RequestsClient

# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class RootEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_response(self):
        response = self.client.get('/disaster-resilience/')
        assert response.status_code == 200

class APIRootEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/disaster-resilience/api')
        assert response.status_code == 200

class DocsEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_response(self):
        response = self.client.get('/disaster-resilience/docs')
        assert response.status_code == 200

class SandboxAPIEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.datasets = ['foundations/censusresponse','foundations/landslide/','foundations/liquefaction','foundations/shaking','slides/poi/']
    def test_list_responses(self):
        for endpoint in self.datasets:
            response = self.client.get('/disaster-resilience/sandbox/'+endpoint)
            assert response.status_code == 200
    def test_detail_responses(self):
        for endpoint in self.datasets:
            response = self.client.get('/disaster-resilience/sandbox/'+endpoint+"/1")
            assert response.status_code == 200

class APIEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.datasets = ['NeighborhoodUnits', 'BuildingFootprints', 'ElectricalTransmissionStructures', 'Jurisdictions', 'QuakeLossView', 'PhfM6P8BedrockGroundmotion', 'PopulationAndBuildingDensity', 'CensusBgAoi', 'CommunityCenters', 'Hospital', 'OregonLiquefactionSusceptibility', 'OregonNehrpSiteClass', 'OregonVsMeasurementIntervals', 'OregonVsMeasurementSites', 'UnreinforcedMasonryBuildings', 'Address', 'FireSta', 'Schools', 'NeighborhoodsRegions', 'MajorRiverBridges', 'BasicEarthquakeEmergencyCommunicationNodeBeecnLocations', 'RlisSt180520', 'POI', 'DisasterNeighborhoods', 'DisasterNeighborhoodView', 'DisasterNeighborhoodGrid']
    def test_list_responses(self):
        for endpoint in self.datasets:
            response = self.client.get('/disaster-resilience/api/'+endpoint)
            assert response.status_code == 200
    def test_detail_responses(self):
        for endpoint in self.datasets:
            response = self.client.get('/disaster-resilience/api/'+endpoint+"/1")
            assert response.status_code == 200
        
