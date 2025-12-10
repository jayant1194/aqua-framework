

class namespaceclient():
    def __init__(self,apiimpl):
        self.api=apiimpl
    def create_ns(self,name):
        body={
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": name}
        }
        return self.api.apply(manifest=body)
    def delete_ns(self,namespace):
        return self.api.delete(namepace=namespace)
    def get_ns(self):
        return self.api.get_namespace()


