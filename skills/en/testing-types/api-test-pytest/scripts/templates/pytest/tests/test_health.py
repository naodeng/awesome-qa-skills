def test_health_example(api_client):
    resp = api_client.request("get", "/health")
    assert resp.status_code in [200, 404]
