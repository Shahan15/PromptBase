import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


class SupabaseClient:
    def __init__(self):
        """Private initializer to load environment variables and create a Supabase client."""
        self.__url: str = os.getenv('SUPABASE_URL')
        self.__key: str = os.getenv('SUPABASE_KEY')

        if not self.__url or not self.__key:
            raise ValueError(
                "Missing Supabase URL or Key. Check environment variables.")

        self.__supabase: Client = create_client(self.__url, self.__key)

    def insert(self, table: str, data: dict):
        """Insert data into a table."""
        response = self.__supabase.table(table).insert(data).execute()
        return response.data

    def fetch(self, table: str, columns: str = "*", filters: dict = None):
        """
        Fetch data from a table with optional filters.

        Supports:
        - Equality filters: { "id": 5 }
        - In filters: { "stock_code__in": ["A", "B"] }
        """
        query = self.__supabase.table(table).select(columns)

        if filters:
            for key, value in filters.items():
                if "__in" in key:
                    field = key.replace("__in", "")
                    query = query.in_(field, value)
                else:
                    query = query.eq(key, value)

        response = query.execute()
        return response.data

    def update(self, table: str, filters: dict, updates: dict):
        """Update data in a table."""
        query = self.__supabase.table(table).update(updates)
        for key, value in filters.items():
            query = query.eq(key, value)
        response = query.execute()
        return response.data

    def delete(self, table: str, filters: dict):
        """Delete data from a table."""
        query = self.__supabase.table(table).delete()
        for key, value in filters.items():
            query = query.eq(key, value)
        response = query.execute()
        return response.data
