# Use VPN at school 


# Import necessary libraries
import time
from openai import OpenAI

# Define the API key and Assistant's ID
API_KEY = "API KEY"
ASSISTANT_ID = "Assistant ID"

# Initialize the OpenAI client
client = OpenAI(api_key=API_KEY)

# Prompt the user for input
user_prompt = input("Enter your prompt:")

# Create a thread with a user message
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

# Submit the thread
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)

# Inform the user that the process has started
print("Processing your request, please wait...")

# Wait for the run to complete
while run.status != "completed":
    # Retrieve the run status
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    
    # Print a loading animation
    for _ in range(3):
        print(".", end="")
        time.sleep(1)
    print()

# Once completed, print a confirmation message
print("Operation completed!")

# Retrieve the latest message from the thread
message_response = client.beta.threads.messages.list(thread_id=thread.id)
latest_message = message_response.data[0]

# Print the Assistant's response
print(f"Assistant's Response: {latest_message.content[0].text.value}")