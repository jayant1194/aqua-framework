
from k8client.resources.podclient import Podclient
from k8client.resources.namespace_client import namespaceclient
class k8sfacade():

    def __init__(self,api_impl):
        self.api=api_impl
        self.pods=Podclient(self.api)
        self.namespace=namespaceclient(self.api)
    def info(self):
        return {
            "client-type":self.api.__class__.__name__
        }
