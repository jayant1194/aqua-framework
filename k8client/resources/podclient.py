import time

class Podclient():
    def __init__(self,api_imp):
        self.api=api_imp
    def create_pod(self,name,namespace,image):
        pod_body = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": name, "namespace": namespace},
            "spec": {"containers": [{"name": name, "image": image}]}
        }
        return self.api.apply(manifest=pod_body)
    def list_pods(self,namespace,kind='pod'):
        return self.api.list(namespace=namespace,kind=kind)
    def wait_pod_ready(self,pod_name,namespace,timeout=60):

        for i in range(timeout):
            result=self.api.get(name=pod_name,namespace=namespace)
            if result.status.phase=='Running':
                return result
            time.sleep(1)
        raise Exception(f"pod is not running state {pod_name}")

    def exec_pod(self,pod_name,namespace,command,container):

        return self.api.exec_pod(name=pod_name,namespace=namespace,command=command,container=container)
    def delete_pod(self,pod_name,name):
        return self.api.delete(pod_name=pod_name,name=name)

