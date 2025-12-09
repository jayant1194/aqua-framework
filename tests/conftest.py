import pytest
from resources.api_client import ApiClient
from facade.k8_facade import k8sfacade



@pytest.fixture(scope="session",target_name="aqua_client")
def k8_client():
    client=ApiClient("~/.kube/config")
    return k8sfacade(client)