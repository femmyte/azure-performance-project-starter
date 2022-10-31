"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each
    output row corresponds to the information in a single close
    approach from the `results` stream and its associated
    near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the
    data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    with open(filename, 'w') as o:
        write = csv.DictWriter(o, fieldnames=fieldnames)
        header = write.writeheader()
        for row in results:
            write.writerow({
                'datetime_utc': row.time_str,
                'distance_au': row.distance,
                'velocity_km_s': row.velocity,
                'designation': row.neo.designation,
                'name': row.neo.name,
                'diameter_km': row.neo.diameter,
                'potentially_hazardous': row.neo.hazardous
            })


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly,
    the output is a list containing dictionaries, each mapping
    `CloseApproach` attributes to their values and the 'neo' key
    mapping to a dictionary of the associated NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where
    the data should be saved.
    """
    my_result = []
    for result in results:
        output = {
            'datetime_utc': result.time_str,
            'distance_au': result.distance,
            'velocity_km_s': result.velocity,
            'neo': {
                'designation': result.neo.designation,
                'name': result.neo.name,
                'diameter_km': result.neo.diameter,
                'potentially_hazardous': result.neo.hazardous
            }
        }
        my_result.append(output)

    with open(filename, 'w') as outfile:
        json.dump(my_result, outfile, indent=2)
