import subprocess
from k8_base_client import K8BaseClient
import time


class kubectlclient(K8BaseClient):
    def __init__(self,kubeconfig):
        super().__init__(kubeconfig)

    def _run(self, cmd):
        cmd=cmd.split()
        if self.kubeconfig:
            cmd.extend(["--kubeconfig",self.kubeconfig])
        result=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if result.returncode!=0:
            raise Exception(f"failed command....{result.stderr}")
        return result.stdout.strip()



    def get_pods(self,namespace):
        cmd=f"kubectl get pods -n {namespace} --no-headers"
        list_pods=[]
        pods_names=self._run(cmd).splitlines()
        for pod_name in pods_names:
            pod=pod_name.split()[0]
            list_pods.append(pod)
        return list_pods





    def get_namespace(self):
        cmd=f"kubectl get namespace --no-headers"
        result=self._run(cmd)
        return result



    def apply(self,yaml_path):
        cmd=f"kubectl apply -f {yaml_path}"
        result=self._run(cmd)
        return result

    def delete(self,yaml_path):
        cmd=f"kubectl delete -f {yaml_path}"
        result=self._run(cmd)
        return result

    def exec_pod(self,pod_name,namespace,command,container=None):
        if container:
            cmd=f"kubectl exec  {pod_name} -n {namespace} -c {container} -- {command}"
        else:
            cmd=f"kubectl exec -it {pod_name} -n {namespace}  -- {command}"
        result=self._run(cmd)
        return result




    def wait_pod_ready(self, pod_name,namespace,timeout=60):
        for i in range(timeout):
            cmd=f"kubectl get pods  {pod_name} -n {namespace} --no-headers "
            result=self._run(cmd).splitlines()



            listr = result.split()
            if listr[2] in ("Running","Succeeded","Completed"):
                return True

            time.sleep(1)
        raise Exception(f"pod {pod_name} is not ready in {timeout} seconds")

    def get_logs(self,pod_name,namespace):
        cmd=f"kubectl logs  {pod_name} -n {namespace}"
        result=self._run(cmd)
        return result

    def get(self,name,namespace,kind):
        cmd=f"kubectl get {kind} {name} -n {namespace} --no-headers"
        result=self._run(cmd)
        return result
    def describe_pod(self,pod_name,namespace):
        command=f"kubectl describe pod {pod_name} -n {namespace}"
        result=self._run(command)
        return result