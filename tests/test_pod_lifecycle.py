

def test_pod_lifecycle(aqua_client,namespace="jayanth"):
    pod_name="jayanth-test"
    output=aqua_client.pods.create_pod(name=pod_name,namespace=namespace,image="nginx")
    print("type of output.....",type(output))
    print("output..............",output)
    aqua_client.pods.wait_pod_ready(pod_name,namespace)
    #verify pod running
    #exec into pod and
    command=["curl", "-vso", "/dev/null", "http://localhost:80"]
    result=aqua_client.pods.exec_pod(pod_nanme=pod_name,namespace=namespace,command=command)
    print(result)





