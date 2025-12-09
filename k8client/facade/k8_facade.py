
from k8client.resources.podclient import Podclient
class k8sfacade():

    def __init__(self,api_impl):
        self.api=api_impl
        self.pods=Podclient(self.api)
    def info(self):
        return {
            "client-type":self.api.__class__.__name__
        }
