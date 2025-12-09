from abc import ABC, abstractmethod

class K8BaseClient(ABC):
    def __init__(self,kubeconfig):
        self.kubeconfig=kubeconfig


    @abstractmethod
    def get_logs(self,pod_name,namespace):
        pass

    @abstractmethod
    def get_namespace(self):
        pass

    @abstractmethod
    def apply(self,manifest,yaml_path):
        pass

    @abstractmethod
    def delete(self,yaml_path,manifest):
        pass

    @abstractmethod
    def get(self,name,namespace,kind):
        pass


