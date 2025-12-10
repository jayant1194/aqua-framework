from .k8_base_client import K8BaseClient
from kubernetes import client,config
import yaml
from pathlib import Path
from kubernetes.stream import stream
import time


class ApiClient(K8BaseClient):
    def __init__(self,kubeconfig):
        super().__init__(kubeconfig)
        config.load_kube_config(config_file=kubeconfig)
        self.core=client.CoreV1Api()
        self.apps=client.AppsV1Api()



    def list(self,namespace,kind='pod'):
        if kind=='pod':

            pods=self.core.list_namespaced_pod(namespace)
            list_pod=[pod.metadata.name for pod in pods.items()]
            return list_pod
        raise NotImplementedError()
    def get_namespace(self):
        result=self.core.list_namespace()
        return [i.metadata.name for i in result.items()]


    def delete(self,namespace,name,kind="Pod"):

        if  kind=="Pod":
            self.core.delete_namespaced_pod(namespace,name)
        elif kind=="Deployment":
            self.apps.delete_namespaced_deployment(namespace,name)
        elif kind=="Service":
            self.core.delete_namespaced_service(namespace,name)
        elif kind=="Namespace":
            return self.core.delete_namespace(namepace)
        else:
            raise Exception(f"kind {kind} is not supported")
    def apply(self,namespace="default",yaml_path=None,manifest=None):


        kind=manifest["kind"]
        name=manifest['metadata']['name']
        namespace=manifest['metadata']['namespace']
        if kind=="Pod":
            return self.core.create_namespaced_pod(namespace,manifest)
        elif kind=="Deployment":
            return self.apps.create_namespaced_deployment(namespace,manifest)
        elif kind=="Service":
            self.core.create_namespaced_service(namespace,manifest)
        elif kind=="ConfigMap":
            return self.core.create_namespaced_config_map(namespace,manifest)
        elif kind=="Namespace":
            return self.core.create_namespace(manifest)
        else:
            raise Exception(f"some error is not supported")

    def exec_pod(self,pod_name,namespace,command,container):
        try:
            output=stream(func=self.core.connect_get_namespaced_pod_exec,namespace=namespace,name=pod_name,command=command,container=container,stderr=True,stdin=False,stdout=True,tty=False)
            return output
        except client.exceptions.ApiException as e:
            raise Exception(f" unable to exec into pod {pod_name} : {e}")




    def get_logs(self,pod_name,namespace):
        logs=self.core.read_namespaced_pod_log(namespace,pod_name)
        return logs


    def get(self,namespace,name,kind='Pod'):

        if kind=="Pod":
            return self.core.read_namespaced_pod(namespace,name)
        raise NotImplementedError()






















