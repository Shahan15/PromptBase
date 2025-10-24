import os
from dotenv import load_dotenv
from supabase import create_client, Client
from uuid import uuid4
from datetime import datetime

load_dotenv()

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

try:
    client: Client = create_client(url, key)

    # insert
    favourite = {
        'id': str(uuid4()),
        'created_at': datetime.now().isoformat(),
        'prompt_id': 'c58ef35d-0e3d-4173-92b3-ee19bd6fbf0b'
    }

    # c58ef35d-0e3d-4173-92b3-ee19bd6fbf0b

    # prompt = {
    #     'id': str(uuid4()),
    #     'created_at': datetime.now().isoformat(),
    #     'original_prompt': 'This is a test prompt 2',
    #     'optimised_prompt': 'This is a test opt prompt the second',
    #     'is_private': False,
    #     'tags': 'abc, def, ghi',
    #     'user_id': '01c462b4-3751-4d1b-8034-c507e9b6205e'
    # }

    # {"idx":0,"id":"01c462b4-3751-4d1b-8034-c507e9b6205e","created_at":"2025-10-17 23:41:52.131056+00","first_name":"John","last_name":"Doe","email":"abc@example.com","password":"test12312"}

    # user = {
    #     'id': str(uuid4()),
    #     'created_at': datetime.now().isoformat(),
    #     'first_name': 'John',
    #     'last_name': 'Doe',
    #     'email': 'abc@example.com',
    #     'password': 'test12312'
    # }
    client.table('favourites').insert(favourite).execute()
except Exception as e:
    print(e)
