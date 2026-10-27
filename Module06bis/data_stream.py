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

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    processed = True
                    break

            if not processed:
                print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {proc.rank_counter} items processed, "
                f"remaining {len(proc.storage)} on processor"
            )

if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()

    stream.print_processors_stats()
    print()

    print("Registering Numeric Processor")
    print()
    data_int = NumericProcessor()
    stream.register_processor(data_int)

    data_list = ["Hello world", [3.14, -1, 2.71],
                 [{"log_level": "WARNING", "log_message":
                  "Telnet access! Use ssh instead"},
                  {"log_level": "INFO", "log_message":
                   "User wil isconnected"}], 42,
                 ["Hi", "five"]]
    print("Send first batch of data on stream:", data_list)
    stream.process_stream(data_list)
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    data_str = TextProcessor()
    data_log = LogProcessor()
    stream.register_processor(data_str)
    stream.register_processor(data_log)
    print("Send the same batch again")
    stream.process_stream(data_list)
    stream.print_processors_stats()
    print()

    print("Consume some elements from the data"
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        rank, value = data_int.output()
    for _ in range(2):
        rank, value = data_str.output()
    for _ in range(1):
        rank, value = data_log.output()
    stream.print_processors_stats()
