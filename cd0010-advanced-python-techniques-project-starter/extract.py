"""Extract data on near-Earth objects and close.

approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file,
formatted as described in the project instructions, into a
collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach
data from a JSON file, formatted as described in the
project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the
arguments provided at the command line, and uses the
resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing
    data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    content = []
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        # line = {}
        for row in reader:
            designation = row.get('pdes')
            name = row.get('name')
            diameter = row.get('diameter')
            hazardous = row.get('pha')
            neo = NearEarthObject(designation, name, diameter, hazardous)
            content.append(neo)
    return content


def load_approaches(cad_json_path='data/test.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing
    data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)

        for row in contents['data']:
            des = row[0]
            cd = row[3]
            dist = row[4]
            v_rel = row[7]
            close_approach = CloseApproach(des, cd, dist, v_rel)
            approaches.append(close_approach)
    return approaches
