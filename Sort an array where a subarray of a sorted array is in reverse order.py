import requests
import os

# Set the URL to which you want to send the POST request
url = "https://prodapi.phot.ai/external/api/v2/user_activity/object-replacer"

headers = {
    "x-api-key": "6527bda872574f78671315bc_71341b8a994020a1b84d_apyhitools",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# Define the data you want to include in the request's body
data = {
    "file_name": "NewImage.webp",
    "input_image_link": "https://production-cloudastra-co.s3.ap-south-1.amazonaws.com/icons/replace-the-sofa.jpeg",
    "mask_image": "",  # You can include the base64 encoded masked image here
    "prompt": "Replace with new blue sofa"
}

# Define the file path to the image you want to upload
image_path = "../WhatsApp Image 2023-10-12 at 15.53.01.jpeg"

# Check if the image file exists
if not os.path.exists(image_path):
    print("Image file does not exist.")
    exit()

# Read the image file and encode it as base64
with open(image_path, 'rb') as image_file:
    image_data = base64.b64encode(image_file.read()).decode()

# Set the base64-encoded image data in the data dictionary
data["input_image_link"] = image_data

# Send the POST request with the headers and data
response = requests.post(url, headers=headers, json=data)

# Check the response status and content
if response.status_code == 200:
    print("POST request successful. Response content:")
    print(response.text)
else:
    print(f"POST request failed with status code {response.status_code}.")
    print("Response content:")
    print(response.text)
