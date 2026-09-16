import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self.storage:
            return self.storage.pop(0)
        else:
            raise IndexError("List does not exist or is empty!")

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            items = data if isinstance(data, list) else [data]

            for item in items:
                self.storage.append(tuple[self.rank_counter], str(item))
                self.rank_counter += 1
        else:
            raise ValueError(f"Invalid data: {data}")