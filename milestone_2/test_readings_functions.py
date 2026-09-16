from functools import reduce

import pytest

from milestone_1.main import filter_by_meter, filter_by_meter_improved, total_energy, peak_energy_reading

"""
Example for raising exceptions

def exception_func():
    raise SystemExit(1)
def test_runner():
    with pytest.raises(SystemExit):
        exception_func()
"""

readings = [
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 10.0,
    },
    {
        "meter_id": "building-b",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 7.0,
    },
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:30:00Z",
        "energy_kwh": 8.0,
    },
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:15:00Z",
        "energy_kwh": 12.0,
    },
]

# Introduce unaccounted for scenario
fragmented_readings = [
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 10.0,
    },
    {
        "timestamp": "2026-09-06T14:00:00Z",
    },
]

single_reading = [
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 10.0,
    },
]

# filter_by_meter tests
def test_filter_with_multiple_readings():
    result = filter_by_meter('building-a', readings)
    target = [
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 10.0,
    },
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:30:00Z",
        "energy_kwh": 8.0,
    },
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:15:00Z",
        "energy_kwh": 12.0,
    },
]
    assert result == target

def test_filter_with_empty_readings():
    result = filter_by_meter('building-a', [])
    target = []
    assert result == target

def test_filter_with_fragmented_readings_error():
    # Cause a bug with current implementation in milestone_1 since it assumes objects have all 3 key-value pairs
    with pytest.raises(KeyError):
        filter_by_meter('building-a', fragmented_readings)

def test_filter_with_fragmented_readings():
    # Fixed version. See comment on ideal validation of data
    result = filter_by_meter_improved('building-a', fragmented_readings)
    target = [{
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 10.0,
    }]
    assert result == target

# total_energy tests
def test_total_energy_with_multiple_readings():
    result = total_energy(readings)
    # Which is better for tests?
    # total = reduce(lambda x,y: x + y, (reading['energy_kwh'] for reading in readings))
    total = 37
    assert result == total

def test_total_energy_with_emtpy_readings():
    result = total_energy([])
    assert result == 0

def test_total_energy_with_single_reading():
    result = total_energy(single_reading)
    target = single_reading[-1]['energy_kwh']
    assert result == target

# peak_energy_reading tests
def test_peak_energy_with_multiple_readings():
    result = peak_energy_reading(readings)
    target = 12.0
    assert result == target

def test_peak_energy_with_empty_readings():
    result = peak_energy_reading([])
    assert result is None

def test_peak_energy_with_single_reading():
    # technically no need for this test
    test_total_energy_with_single_reading()