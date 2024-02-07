import interactor

class ShowTaskRegistryCommand():
    def __init__(self, registry_presenter):
        self.__registry_presenter = registry_presenter

    def execute(self):
        self.__registry_presenter.out(interactor.task_registry)
