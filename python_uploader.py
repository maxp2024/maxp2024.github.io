import requests  # type: ignore

# Define the URL of your Flask server's upload endpoint
url = "https://maxp2024.github.io/upload"  # Replace with your server's URL if hosted online

# Open the file you want to upload
file_path = "response_log.txt"  # Ensure this file exists in your working directory
with open(file_path, "rb") as file:
    # Create a dictionary for the file to send
    files = {"logfile": file}
    
    # Send the POST request to the server
    response = requests.post(url, files=files)

# Print the server's response
print(response.text)