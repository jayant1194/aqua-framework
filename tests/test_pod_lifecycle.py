

def test_pod_lifecycle(aqua_client,namespace="jayanth"):
    pod_name="jayanth-test"
    output=aqua_client.pods.create_pod(name=pod_name,namespace=namespace,image="nginx")
    print(output)
    return output



