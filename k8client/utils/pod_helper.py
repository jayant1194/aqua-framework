


def check_verify_pod(aqua_client,pod_name,namespace):
    list_pods=aqua_client.pods.list_pods(namspace=namespace)
    if pod_name in list_pods:
        return True
    else:
        return False