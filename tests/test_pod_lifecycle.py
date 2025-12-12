from k8client.utils.pod_helper import check_verify_pod

def test_pod_lifecycle(aqua_client,namespace="jayanth"):
    pod_name="jayanth-test"
    output=aqua_client.pods.create_pod(name=pod_name,namespace=namespace,image="nginx")
    print("type of output.....",type(output))
    print("output..............",output)
    aqua_client.pods.wait_pod_ready(pod_name,namespace)
    #verify pod running
    #exec into pod and
    command=["curl", "-vso", "/dev/null", "http://localhost:80"]
    result=aqua_client.pods.exec_pod(pod_name=pod_name,namespace=namespace,command=command)
    assert "200 OK" in result
    output=aqua_client.pods.get_logs(pod_name,namespace)
    print(output)
    #delete pod
    aqua_client.pods.delete_pod(pod_name,namespace)
    #verify pod dleted
    check_pod=check_verify_pod(aqua_client,pod_name,namespace)
    assert check_pod,f"pod not deleted ${pod_name}"


    #






