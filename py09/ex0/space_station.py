from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def desplay_valid_station(station: SpaceStation):
    print("Space Station Data Validation")
    print("=" * 40)
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(
        "Status"
        f" {'Operational' if station.is_operational else 'Not Operational'}"
    )
    print()


def main():
    try:
        valid_station = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            notes='Station is operating normally'
        )
        desplay_valid_station(valid_station)
    except ValidationError as error:
        print("Unexpected validation error")
        print(error)

    print("=" * 40)
    try:
        invalid_station = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            notes='Station is operating normally'
        )
        print(invalid_station)
    except ValidationError as error:
        print("Expected validation error")
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
