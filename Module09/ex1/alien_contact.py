from enum import Enum

from pydantic import AliasChoices, BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enumeration of supported alien contact methods."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model representing an incoming signal from an alien civilization."""

    contact_id: str = Field(..., min_length=3, max_length=15, description="Unique identifier for the contact")
    source_planet: str = Field(
        ...,
        min_length=2,
        max_length=40,
        validation_alias=AliasChoices("source_planet", "planet"),
        description="Planet or origin system",
    )
    contact_type: ContactType = Field(
        ...,
        validation_alias=AliasChoices("contact_type", "signal_type", "method"),
        description="Communication method used in the transmission",
    )
    signal_strength: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        validation_alias=AliasChoices("signal_strength", "strength"),
        description="Strength of the signal from 0 to 10",
    )
    message_received: str = Field(
        default="",
        max_length=500,
        validation_alias=AliasChoices("message_received", "message"),
        description="Decoded alien message",
    )
    is_response_expected: bool = Field(default=False, description="Whether a response from Earth is expected")

    @model_validator(mode="after")
    def validate_message_for_high_signal(self) -> "AlienContact":
        """Guard against empty transmissions when the signal is too strong."""

        if self.signal_strength > 7.0 and not self.message_received.strip():
            raise ValueError("Message cannot be empty when signal strength exceeds 7.0")

        return self


def main() -> None:
    print("Alien Contact Validation\n")

    try:
        valid_contact = AlienContact(
            contact_id="A-104",
            source_planet="Kepler-442b",
            contact_type=ContactType.RADIO,
            signal_strength=8.7,
            message_received="We observe your planet. Please respond.",
            is_response_expected=True,
        )
        print("Valid contact created:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Origin: {valid_contact.source_planet}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Signal strength: {valid_contact.signal_strength}")
        print(f"Message: {valid_contact.message_received}")
        print(f"Response expected: {'Yes' if valid_contact.is_response_expected else 'No'}\n")
    except ValidationError as exc:
        print(f"Unexpected error: {exc}")

    try:
        AlienContact(
            contact_id="A-105",
            source_planet="Tau Ceti",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=9.2,
            message_received="",
            is_response_expected=True,
        )
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            field_name = error['loc'][0] if error['loc'] else 'model'
            print(f"- {error['msg'].replace('Value error, ', '')} (Field: {field_name})")


if __name__ == "__main__":
    main()
