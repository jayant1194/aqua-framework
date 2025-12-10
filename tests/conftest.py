import pytest
from k8client.resources.api_client import ApiClient
from k8client.facade.k8_facade import k8sfacade




@pytest.fixture(scope="session",name="aqua_client")
def k8_client():
    client=ApiClient("~/.kube/config")
    return k8sfacade(client)


@pytest.fixture(scope="session")
def create_namespace(aqua_client):
     return aqua_client.namespace.create_ns(name="jayanth")


