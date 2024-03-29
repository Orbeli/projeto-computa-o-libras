from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.models import Module

@dataclass
class SaveModuleParams:
    name: str
    subject: str
    duration: str


class ModuleRepositoryContract(ABC):
    @abstractmethod
    def get_module_by_id(
        self,
        id: int
    ) -> Module:
        raise NotImplementedError()

    @abstractmethod
    def delete_module_by_id(
        self,
        id: int
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def create_module(
        self,
        params: SaveModuleParams
    ) -> str:
        raise NotImplementedError()
