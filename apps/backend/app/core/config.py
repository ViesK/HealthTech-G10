import os; from dotenv import load_dotenv; load_dotenv()
API_PREFIX = "/api"
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET", "G0n6X2iWq9Zb7pK4rN8uV1tY5mQ3cS0fD6hJ2lP9aR7yT4wE1kB8uM5xC2vZ0qL")
