from typing import Any 
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
                self.storage.append((self.rank_counter, str(item)))
                self.rank_counter += 1
        else:
            raise ValueError(f"Invalid data: {data}")

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and not isinstance(data, bool):
            return True
        
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, str) and not isinstance(x, bool) for x in data)
        
        return False
    
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError(f"Invalid data: {data}")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self.storage.append((self.rank_counter, item))
            self.rank_counter += 1

class LogProcessor(DataProcessor):
    def _is_valid_log_dict(self, d: Any) -> bool:
        if not isinstance(d, dict) or not d:
            return False
        
        return all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())
    
    def validate(self, data: Any) -> bool:
        if self._is_valid_log_dict(data):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(self._is_valid_log_dict(x) for x in data)

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError(f"Invalid data: {data}")

        items = data if isinstance(data, list) else [data]

        for item in items:
            formatted_log = ": ".join(item.values())
            self.storage.append((self.rank_counter, formatted_log))
            self.rank_counter += 1

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # -------------------------------------------------------------
    # 1. Numeric Processor
    # -------------------------------------------------------------
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()

    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("\nTest invalid ingestion of string 'foo' without prior validation:")
    try:
        # mypy vai alertar aqui por passar str em um método que espera int/float.
        # Isso é PROPOSITAL conforme a especificação do exercício!
        num_proc.ingest("foo")  # type: ignore[arg-type]
    except ValueError as e:
        print(f"Got exception: Improper numeric data ({e})")

    print("\nProcessing data: [1, 2, 3, 4, 5]")
    num_proc.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    # -------------------------------------------------------------
    # 2. Text Processor
    # -------------------------------------------------------------
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()

    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    print("\nProcessing data: ['Hello', 'Nexus', 'World']")
    text_proc.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    # -------------------------------------------------------------
    # 3. Log Processor
    # -------------------------------------------------------------
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"\nProcessing data: {log_data}")
    log_proc.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")