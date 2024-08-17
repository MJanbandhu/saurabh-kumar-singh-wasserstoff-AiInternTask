import json

def map_data(objects, text_data, identified_objects, descriptions=None, summaries=None):
    mapped_data = {}
    
    for i, (obj, text, identification) in enumerate(zip(objects, text_data, identified_objects)):
        obj_id = f'object_{i}'
        mapped_data[obj_id] = {
            "image": obj,
            "text": text,
            "identification": identification,
        }
        # Optionally add descriptions and summaries if provided
        if descriptions:
            mapped_data[obj_id]["description"] = descriptions[i]
        if summaries:
            mapped_data[obj_id]["summary"] = summaries[i]
    
    return mapped_data

# Example usage
if __name__ == "__main__":
    objects = ['object_image_1.png', 'object_image_2.png']
    text_data = ["License plate: ABC123.", "Brand: Tesla."]
    identified_objects = [{'label': 'dog', 'confidence': 0.9}, {'label': 'car', 'confidence': 0.8}]
    descriptions = ["This is a dog.", "This is a car."]
    summaries = ["Dog with license plate.", "Tesla car."]
    
    mapped_data = map_data(objects, text_data, identified_objects, descriptions, summaries)
    
    with open("data/output/mapped_data.json", "w") as file:
        json.dump(mapped_data, file, indent=4)
    
    print(mapped_data)