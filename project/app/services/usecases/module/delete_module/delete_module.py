from app.domain.usecases import DeleteModule as DeleteModuleContract
from app.domain.usecases import DeleteModuleParams
from app.services.contracts import ModuleRepositoryContract
from app.services.helpers.http import HttpResponse, HttpStatus


class DeleteModule(DeleteModuleContract):
    def __init__(
        self,
        module_repository: ModuleRepositoryContract
    ) -> None:
        self.module_repository = module_repository

    def execute(self, params: DeleteModuleParams) -> HttpResponse:
        print("DELETE MODULOOOOOOOOO")
        module = self.module_repository.get_module_by_id(params.id)
        if not module:
            return HttpStatus.not_found_404(
                f"Module [{params.id}] does not exist"
            )

        self.module_repository.delete_module_by_id(
            id=module.id
        )

        return HttpStatus.no_content_204()
