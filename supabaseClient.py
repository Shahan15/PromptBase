import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()   

class SupabaseClient:

    #this runs when you create an object of the class
    def __init__(self):
        self.__url   : str = os.getenv("SUPABASE_URL")
        self.__key : str = os.getenv("SUPABASE_KEY")

        if not self.__url or not self.__key:
            raise ValueError("Missing environment variables check environment variables")

        self.__supabase : Client = create_client(self.__url, self.__key)
    
    def insert(self, table : str, data: dict):
        response = self.__supabase.table(table).insert(data).execute()
        return response.data
    
    def fetch(self, table:str, columns : str = '*',filters : dict = None):
       
        # Fetch data from a table with optional filters.

        # Supports:
        # - Equality filters: { "user_id": 42 }
        # - In filters: { "category__in": ["AI", "Coding"] }

        # Examples:
        # - Fetch prompts created by a specific user:
        #     filters = { "user_id": 42 }
            
        # - Fetch prompts in multiple categories:
        #     filters = { "category__in": ["AI", "Coding"] }
        
        query = self.__supabase.table(table).select(columns)

        #checks if filter is true. Iterate through it and checks if there is an IN or Equality filter
        if filter:
            for key, value in filters.items():
                if "__in" in key:
                    field = key.replace("__in","")
                    query = query.in_(field,value)
                else: 
                    query = query.eq(key, value)

    

