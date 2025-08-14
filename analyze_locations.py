#!/usr/bin/env python3
import json

# Load the data
with open('_data/listings.json', 'r') as f:
    data = json.load(f)

# Collect unique regions and sub_regions
regions = set()
sub_regions = set()
properties_with_location = 0

for item in data:
    region = item.get('region')
    sub_region = item.get('sub_region')
    
    if region and region != 'None':
        regions.add(region)
        properties_with_location += 1
    
    if sub_region and sub_region != 'None':
        sub_regions.add(sub_region)

print(f"Total properties: {len(data)}")
print(f"Properties with location data: {properties_with_location}")
print(f"Regions: {sorted(list(regions))}")
print(f"Sub Regions: {sorted(list(sub_regions))}")

# Show some sample data
print("\nSample properties with location:")
count = 0
for item in data:
    if item.get('region') and item.get('region') != 'None' and count < 5:
        print(f"- {item.get('name', 'No name')}: {item.get('region')}, {item.get('sub_region', 'N/A')}")
        count += 1
