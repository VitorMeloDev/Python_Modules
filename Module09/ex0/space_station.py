from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Pydantic model representing a cosmic space station."""
    
    station_id: str = Field(..., min_length=3, max_length=10, description="Unique station identifier")
    name: str = Field(..., min_length=1, max_length=50, description="Full name of the station")
    crew_size: int = Field(..., ge=1, le=20, description="Number of personnel on board")
    power_level: float = Field(..., ge=0.0, le=100.0, description="Power capacity percentage")
    oxygen_level: float = Field(..., ge=0.0, le=100.0, description="Oxygen capacity percentage")
    last_maintenance: datetime = Field(..., description="Timestamp of last maintenance check")
    is_operational: bool = Field(default=True, description="Current operational status")
    notes: Optional[str] = Field(default=None, max_length=200, description="Additional logs or notes")


def main() -> None:
    print("Space Station Data Validation\n")

    # 1. Create a valid space station
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-10-27T08:00:00Z",  # Pydantic parses strings to datetime
            is_operational=True
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {'Operational' if valid_station.is_operational else 'Offline'}\n")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    # 2. Attempt to create an invalid station (crew > 20)
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Overcrowded Station",
            crew_size=25, # Invalid: must be <= 20
            power_level=90.0,
            oxygen_level=80.0,
            last_maintenance="2024-10-27T08:00:00Z"
        )
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(f"- {err['msg']} (Field: {err['loc'][0]})")


if __name__ == "__main__":
    main()