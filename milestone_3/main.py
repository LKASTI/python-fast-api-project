from datetime import datetime, timezone
from pydantic import ValidationError
from energy_reading import EnergyReadingDataclass, EnergyReadingDataclassWithValidation
from milestone_3.energy_reading import EnergyReadingPydantic


def print_energy_reading_dataclass():
    try:
        # Missing args creates a TypeError
        r1 = EnergyReadingDataclass()
    except TypeError as e:
        print(e)

    # energy_kwh initialized with str doesn't create error or raise an exception (dataclass does not validate types)
    r1 = EnergyReadingDataclass(
        energy_kwh='',
        meter_id='',
        timestamp=datetime.now()
    )
    print(r1)

    print('\n')

    r2 = EnergyReadingDataclass(
        energy_kwh=20.1,
        meter_id='building-a',
        timestamp=datetime.now()
    )
    print(r2)

def print_energy_reading_dataclass_with_validation():
    try:
        # energy_kwh is initialized with '' which raises a ValueError from our post init validation
        # timestamp is initialized without a UTC timezone -> ValueError
        r1 = EnergyReadingDataclassWithValidation(
            energy_kwh='',
            meter_id='',
            timestamp=datetime.now()
        )
    except ValueError as e:
        print(e)

    r2 = EnergyReadingDataclassWithValidation(
        energy_kwh=20.1,
        meter_id='building-a',
        timestamp=datetime.now(timezone.utc)
    )
    print(r2)

def print_energy_reading_pydantic():
    try:
        # Pydantic will attempt to convert the str into a number -> raises ValidationError since empty str cannot be converted
        r1 = EnergyReadingPydantic(
            energy_kwh='',
            meter_id='building-a',
            timestamp=datetime.now(timezone.utc)
        )
    except ValidationError as e:
        print(e)

    # Converts str to datetime
    r2 = EnergyReadingPydantic(
        energy_kwh=20.1,
        meter_id='building-a',
        timestamp='2026-09-17T14:00:00Z'
    )
    print(r2)

    try:
        # Validation on energy_kwh forces >= 0 -> raise ValidationError
        r3 = EnergyReadingPydantic(
            energy_kwh=-6.0,
            meter_id='building-a',
            timestamp='2026-09-17T14:00:00Z'
        )
    except ValidationError as e:
        print(e)

    r4 = EnergyReadingPydantic()
    print(r4)

def main():
    print_energy_reading_pydantic()


if __name__ == "__main__":
    main()