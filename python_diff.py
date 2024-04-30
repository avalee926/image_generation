import replicate
import requests
from dotenv import load_dotenv
from pprint import pprint
import random

load_dotenv()

def download_image(image_url, filename):
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print("failure :(")

for i in range(10):
    seed = random.randint(0, 100000)

    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": "a man spending time with friends", "seed": seed}
    )
    pprint(output)
    
    if output and isinstance(output, list) and output[0].startswith('http'):
        download_image(output[0], f"output_{i+1}.jpg")
        print(f"Image {i+1} generated and saved.")
    else:
        print(f"Failed to generate Image {i+1}.")
