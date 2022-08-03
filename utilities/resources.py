class APIResources:
    country = 'us/'
    zipcode = '90210'

    api_resources = {'endpoint_usa': 'us/90210','endpoint_can':'ca/a0a'}

    expected_response_old = {
        'endpoint_usa': {"post code": "90210", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA", "latitude": "34.0901"}]}}

    expected_response = {
        'endpoint_usa': {"post code": "90210", "country": "United States", "country abbreviation": "US", "places": [
            {"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA",
             "latitude": "34.0901"}]},
        'endpoint_can': {"post code": "A0A", "country": "Canada", "country abbreviation": "CA", "places": [
            {"place name": "Southeastern Avalon Peninsula (Ferryland)", "longitude": "-52.9589",
             "state": "Newfoundland and Labrador", "state abbreviation": "NL", "latitude": "47.0073"}]}
    }