from app.domain.usecases import CreateModule as CreateModuleContract
from app.domain.usecases import CreateModuleParams
from app.services.contracts import ModuleRepositoryContract, SaveModuleParams
from app.services.helpers.http import HttpResponse, HttpStatus


class CreateModule(CreateModuleContract):
    def __init__(
        self,
        module_repository: ModuleRepositoryContract
    ) -> None:
        self.module_repository = module_repository

    def execute(self, params: CreateModuleParams) -> HttpResponse:
        module_id = self.module_repository.create_module(
            SaveModuleParams(
                name=params.name,
                subject=params.subject,
                duration=params.duration
            )
        )

        return HttpStatus.created_201({
            'module': module_id
        })
