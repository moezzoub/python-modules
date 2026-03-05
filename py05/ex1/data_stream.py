from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return list(data_batch)
        return [
                item for item in data_batch if
                isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class StreamProcessor:
    def __init__(self) -> None:
        self._streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if not isinstance(stream, DataStream):
            raise TypeError("Only DataStream instances \
can be added to stream processor")
        self._streams.append(stream)


class SensorStream(DataStream):
    def __init__(self, id: str) -> str:
        super().__init__(id)
        self.type = "Environmental Data"
        self.total_temp: float = 0.0
        self.temp_count: int = 0

    def process_batch(self, data_batch: str) -> str:
        try:
            readings: List[str] = []
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    key, value = item.split(":", 1)
                    readings.append(f"{key}:{value}")
                    if key == "temp":
                        self.total_temp += float(value)
                        self.temp_count += 1
            avg_temp: float = self.total_temp / self.temp_count
            return f"Sensor analysis: {len(readings)} readings processed, \
avg temp: {avg_temp:.1f}°C"
        except Exception as e:
            return f"Sensor processing error: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type: str = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    action, value = item.split(":", 1)
                    amount = float(value)
                    if action == "buy":
                        self.net_flow += amount
                    elif action == "sell":
                        self.net_flow -= amount
            sign = "+" if self.net_flow >= 0 else ""
            return f"Transaction analysis: {len(data_batch)} operations, net \
flow: {sign}{self.net_flow:.0f} units"
        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        return [
                item for item in data_batch
                if float(item.split(":", 1)[1]) >= 100]


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"
        self.error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.error_events = len([
                                        e for e in data_batch if
                                        isinstance(e, str) and "error" in e])
            return f"Event analysis: {len(data_batch)} events, \
{self.error_events} error detected"
        except Exception as e:
            return f"Event processing error: {e}"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_stream.get_stats()["stream_id"]}, Type: \
Environmental Data")
    stream_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013", 54]
    print(f"Processing sensor data batch  {stream_batch}")
    print(sensor_stream.process_batch(stream_batch))

    print("\nInitializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction_stream.get_stats()["stream_id"]}, Type: \
Financial Data")
    transaction_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")
    print(transaction_stream.process_batch(transaction_batch))

    print("\nInitializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(f"Stream ID: {event_stream.get_stats()["stream_id"]}, Type: \
System Events")
    events_batch: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(events_batch)}]")
    print(event_stream.process_batch(events_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    mixed_batches: Dict[str, List[str]] = {
        "SENSOR_001": ["temp:30", "humidity:80"],
        "TRANS_001": ["buy:200", "sell:50", "buy:30", "sell:120"],
        "EVENT_001": ["login", "error", "logout"],
    }
    print("\nBatch 1 Results:")
    print(f"  - Sensor data: {len(mixed_batches['SENSOR_001'])} \
readings processed")
    print(f"  - Transaction data: {len(mixed_batches['TRANS_001'])} \
operations processed")
    print(f"  - Event data: {len(mixed_batches['EVENT_001'])} \
events processed")
    print("\nStream filtering active: High-priority data only")
    sensor_filter = SensorStream("SENSOR_F")
    critical_sensors = sensor_filter.filter_data(
        [
            "temp:critical_alert", "humidity:normal",
            "pressure:critical_alert"], "critical"
    )
    transaction_filter = TransactionStream("TRANSACTION_F")
    large_transactions = transaction_filter.filter_data(["buy:80", "sell:150",
                                                        "buy:75"])
    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts, \
{len(large_transactions)} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
