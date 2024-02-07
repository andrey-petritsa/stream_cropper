import refactor.glb.global_service

class ServiceClient():
    def call_service(self):
        return refactor.glb.global_service.service.get_hello()