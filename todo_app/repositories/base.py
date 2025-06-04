from typing import TypeVar, Generic, Dict, Optional, List
from uuid import UUID

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self):
        self.items: Dict[UUID, T] = {}

    def get_all(self) -> List[T]:
        return list(self.items.values())

    def get_by_id(self, id: UUID) -> Optional[T]:
        return self.items.get(id)

    def create(self, item: T) -> T:
        self.items[item.id] = item
        return item

    def update(self, id: UUID, item: T) -> Optional[T]:
        if id in self.items:
            self.items[id] = item
            return item
        return None

    def delete(self, id: UUID) -> bool:
        if id in self.items:
            del self.items[id]
            return True
        return False