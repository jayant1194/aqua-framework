

def test_pod_lifecycle(aqua_client,namespace="jayanth"):
    pod_name="jayanth-test"
    aqua_client.pods.create_pod(pod_name=pod_name,namespace=namespace,image="nginx")

