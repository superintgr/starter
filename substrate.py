# 1. A sphere contains points with cartesian coordinates and polar coordinates
# 2. For each point, the state of the object encodes the position and orientation within the sphere with 6 parameters,
# 3. For each state, we can associate a label and a set of labeled states maps each label uniquely,
# 4. For each label and states within a spherical object, can be composed in series into a new unique labeled state of a different sphere.

## The goal is to create a connection group of tasks where a task is represented as {Input attribute of substrate -> Output attribute of substrate} where the substrate ia a an object with spherical-cartesian coordinate system.

import pickle
import numpy as np
from itertools import permutations
from collections import defaultdict

class Substrate:
    def __init__(self, attributes_dict=None):
        self.intrinsic_attributes = {}  # Intrinsic parameters mapped to permutations
        self.parent_pairs = {}  # Mapping of permutations to unique parent pairs
        self.state = None

        if attributes_dict:
            self.construct_from_dict(attributes_dict)

    def construct_from_dict(self, attributes_dict):
        # Custom construction process based on the input attributes_dict
        self.intrinsic_attributes = {label: list(perm) for label, perm in zip(attributes_dict.keys(), permutations(attributes_dict.values()))}
        unique_parent_pairs = defaultdict(list)
        for label, perm in self.intrinsic_attributes.items():
            unique_parent_pairs[tuple(perm)].append(label)
        self.parent_pairs = dict(unique_parent_pairs)

    def encode_attributes(self, query_variable):
        # Encode attributes based on specified rules
        intrinsic_properties = self.intrinsic_attributes.get(query_variable, [])
        cartesian_properties = [np.random.rand() for _ in range(len(intrinsic_properties))]  # Placeholder for extrinsic attributes
        self.state = {'intrinsic': intrinsic_properties, 'extrinsic': cartesian_properties}

    def to_cartesian(self, spherical_coordinates):
        # Placeholder, replace with actual encoding logic
        return [np.random.rand() for _ in range(len(spherical_coordinates))]

    def to_spherical(self, cartesian_coordinates):
        # Placeholder, replace with actual encoding logic
        return [np.random.rand() for _ in range(len(cartesian_coordinates))]

    def save_model(self, file_path):
        # Save the model using pickle
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_model(cls, file_path):
        # Load the model from a saved file
        with open(file_path, 'rb') as file:
            loaded_model = pickle.load(file)
        return loaded_model

# Example usage:
# Create a Substrate instance with attributes from a dictionary
attributes_dict = {'param1': 1, 'param2': 2, 'param3': 3}
substrate = Substrate(attributes_dict=attributes_dict)

# Encode attributes for a query variable
query_variable = 'param2'
substrate.encode_attributes(query_variable)
print(f"Encoded state for {query_variable}: {substrate.state}")
