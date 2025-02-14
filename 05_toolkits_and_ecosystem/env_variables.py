'''
environemnt variables are key-value pairs used for configuration, credentials and cross-platform support

- os module allows accessing environment variables

export DATABASE_URL="postgresql://user:pass@localhost/db"
python script.py
'''

import os

db_url = os.getenv("DATABASE_URL", "sqlite:///:memory:")  # Default if not set
print(f"Database URL: {db_url}")


'''
dotenv
- env variables are stored in .env file

'pip install python-dotenv'

.env
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=mysecret

'''

from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

db_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")

print(f"DB: {db_url}, Secret: {secret_key}")
