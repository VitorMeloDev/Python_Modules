from typing import Any, Protocol 
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

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join([item for _, item in data]))

class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
            pairs = [f'"item_{rank}": "{text}"' for rank, text in data]
            print("JSON Output:")
            print("{" + ", ".join(pairs) + "}")

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            output_list: list[tuple[int, str]] = []
            
            for _ in range(nb):
                if not proc.storage:
                    break
                output_list.append(proc.output())
            
            if output_list:
                plugin.process_output(output_list)

if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()

    stream.print_processors_stats()
    print()

    print("Registering Processors")
    print()
    data_int = NumericProcessor()
    data_str = TextProcessor()
    data_log = LogProcessor()
    stream.register_processor(data_int)
    stream.register_processor(data_str)
    stream.register_processor(data_log)

    data_list = ["Hello world", [3.14, -1, 2.71],
                 [{"log_level": "WARNING", "log_message":
                  "Telnet access! Use ssh instead"},
                  {"log_level": "INFO", "log_message":
                   "User wil isconnected"}], 42,
                 ["Hi", "five"]]
    print("Send first batch of data on stream:", data_list)
    print()

    stream.process_stream(data_list)
    print()

    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()

    stream.print_processors_stats()
    print()

    data_list_2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                   [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                    {'log_level': 'NOTICE', 'log_message':
                    'Certificate expires in 10 days'}],
                   [32, 42, 64, 84, 128, 168], 'World hello']
    print("Send another batch of data:", data_list_2)
    print()

    stream.process_stream(data_list_2)
    print()

    stream.print_processors_stats()
    print()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()

    stream.print_processors_stats()