from app.domain.usecases import GetModule as GetModuleContract
from app.domain.usecases import GetModuleParams
from app.services.contracts import ModuleRepositoryContract
from app.services.helpers.http import HttpResponse, HttpStatus


class GetModule(GetModuleContract):
    def __init__(
        self,
        module_repository: ModuleRepositoryContract
    ) -> None:
        self.module_repository = module_repository

    def execute(self, params: GetModuleParams) -> HttpResponse:
        module = self.module_repository.get_module_by_id(params.id)
        if not module:
            return HttpStatus.not_found_404(
                f"Module [{params.id}] does not exist"
            )

        return HttpStatus.ok_200({
            'module': module
        })
