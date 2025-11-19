# Basic test using requests (run after starting the app)
import requests
def test_query():
    r = requests.post('http://localhost:5000/api/query', json={'text':'Hi there'})
    assert r.status_code == 200
    j = r.json()
    assert 'intent' in j
