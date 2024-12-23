from dotenv import load_dotenv
import os

# if __name__ == "__main__":
# Load the environment variables from the .env file . Use .env for local development only
load_dotenv()
print("Hello World")
print(os.getenv("TEST_ENV"))
