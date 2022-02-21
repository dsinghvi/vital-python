import pytest
from vital import Client

@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_get_glucose(provider, test_client: Client, user_key: str, start_date: str, end_date: str):
    data = test_client.Vitals.glucose(user_key, start_date, end_date, provider)
    assert data is not None

@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_get_cholesterol(provider, test_client: Client, user_key: str, start_date: str, end_date: str):
    data = test_client.Vitals.cholesterol(user_key, start_date, end_date, provider)
    assert data is not None

@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_get_ige(provider, test_client: Client, user_key: str, start_date: str, end_date: str):
    data = test_client.Vitals.ige(user_key, start_date, end_date, provider)
    assert data is not None

@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_get_igg(provider, test_client: Client, user_key: str, start_date: str, end_date: str):
    data = test_client.Vitals.igg(user_key, start_date, end_date, provider)
    assert data is not None

@pytest.mark.parametrize("provider", ["oura", "fitbit", "strava", "garmin"])
def test_get_heartrate(provider, test_client: Client, user_key: str, start_date: str, end_date: str):
    data = test_client.Vitals.heartrate(user_key, start_date, end_date, provider)
    assert data is not None


def test_get_raw(
    test_client: Client, user_key: str
):
    data = test_client.Profile.get_raw(user_key)
    assert data is not None