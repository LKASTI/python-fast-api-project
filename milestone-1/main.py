"""
milestone-1: write basic functions that operate on a list of objects

filter_by_meter(): filters the data by meter
total_energy(): gets the total energy of all rows
peak_energy_reading(): gets the object with the highest energy reading
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

single_reading = [
    {
        "meter_id": "building-a",
        "timestamp": "2026-09-06T14:00:00Z",
        "energy_kwh": 10.0,
    },
]

empty_readings = []

def filter_by_meter(target_meter_id: str, readings_list: list[dict]) -> list[dict]:
    filtered_readings = []
    if not target_meter_id: return filtered_readings

    for reading in readings_list:
        meter_id = reading['meter_id']
        if meter_id and meter_id == target_meter_id: filtered_readings.append(reading)
    return filtered_readings

def total_energy(readings_list: list[dict]) -> float:
    total = 0.0
    for reading in readings_list:
        val = reading['energy_kwh']
        if val and isinstance(val, (float, int)):
            total += val
    return total

def peak_energy_reading(readings_list: list[dict]) -> dict | None:
    peak_reading = None
    for reading in readings_list:
        val = reading['energy_kwh']
        if val and isinstance(val, (float, int)):
            if peak_reading is None or (val > peak_reading['energy_kwh']):
                peak_reading = reading
    return peak_reading

def main():
    print("For readings, find a building-a readings, the total energy used, and peak.")
    l = filter_by_meter('building-a', readings)
    for o in l:
        print(o)
    print(f'total: {total_energy(readings)}')
    print(f'peak energy: {peak_energy_reading(readings)}\n')

    print("For single_reading, find a building-a single_reading, the total energy used, and peak.")
    l = filter_by_meter('building-a', single_reading)
    for o in l:
        print(o)
    print(f'total: {total_energy(single_reading)}')
    print(f'peak energy: {peak_energy_reading(single_reading)}\n')

    print("For empty_readings, find a building-a empty_readings, the total energy used, and peak.")
    l = filter_by_meter('building-a', empty_readings)
    for o in l:
        print(o)
    print(f'total: {total_energy(empty_readings)}')
    print(f'peak energy: {peak_energy_reading(empty_readings)}\n')


if __name__ == '__main__':
    main()