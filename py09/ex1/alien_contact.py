from typing import Self
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def Contact(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('contact_id must start with "AC"')
        elif (
            self.contact_type == ContactType.PHYSICAL
            and self.is_verified is False
        ):
            raise ValueError("physical contact reports must be verified")
        elif (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesse")
        elif self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                'strong signals (> 7.0) must include a received message')

        return self


def info_alien(station: AlienContact):
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {station.contact_id}")
    print(f"Type: {station.contact_type.value}")
    print(f"Location: {station.location}")
    print(f"Signal: {station.signal_strength}/10")
    print(f"Duration: {station.duration_minutes} minutes")
    print(f"Witnesses: {station.witness_count}")
    print(f"Message: '{station.message_received}'")


def display_validation_error(error: ValidationError):
    print(error.errors()[0]["ctx"]["error"])


def main():
    try:
        info = AlienContact(
            contact_id='AC_2024_001',
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type='radio',
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        info_alien(info)
    except ValidationError as error:
        print("Unexpected validation error")
        print(error)
    print("======================================")
    try:
        invalid_info = AlienContact(
            contact_id='AC_2024_001',
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type='telepathic',
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print(invalid_info)
    except ValidationError as error:
        print("Expected validation error:")
        display_validation_error(error)


if __name__ == "__main__":
    main()
