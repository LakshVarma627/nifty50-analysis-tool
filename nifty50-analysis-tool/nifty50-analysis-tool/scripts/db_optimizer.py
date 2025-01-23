import django
from django.db import connection
from django.core.cache import cache

# Initialize Django settings
django.setup()

# Import your models here
# from your_app.models import YourModel

def create_index(table_name, column_name):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{column_name} ON {table_name} ({column_name});")
    print(f"Index on {column_name} in {table_name} created or updated.")

def optimize_query():
    # Example: optimizing a query using select_related and prefetch_related
    # optimized_query = YourModel.objects.select_related('related_model').all()
    # For demonstration, just a placeholder
    print("Query optimized.")

def perform_maintenance():
    with connection.cursor() as cursor:
        cursor.execute("VACUUM;")
        cursor.execute("REINDEX;")
    print("Database maintenance tasks completed.")

def partition_table(table_name, partition_column):
    with connection.cursor() as cursor:
        # Example partitioning by year
        cursor.execute(f"ALTER TABLE {table_name} PARTITION BY RANGE ({partition_column});")
    print(f"Table {table_name} partitioned by {partition_column}.")

def implement_caching(key, value, timeout=300):
    cache.set(key, value, timeout)
    print(f"Data cached with key {key}.")

def archive_data(table_name, archive_table_name, condition):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO {archive_table_name} SELECT * FROM {table_name} WHERE {condition};")
        cursor.execute(f"DELETE FROM {table_name} WHERE {condition};")
    print(f"Data archived from {table_name} to {archive_table_name} where {condition}.")

def update_schema():
    # Example: adding a new column
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE your_table ADD COLUMN new_column VARCHAR(255);")
    print("Database schema updated.")

if __name__ == "__main__":
    # Example usages
    create_index('nifty_data', 'stock_symbol')
    create_index('nifty_data', 'date')
    optimize_query()
    perform_maintenance()
    partition_table('nifty_data', 'date')
    implement_caching('example_key', 'example_value')
    archive_data('nifty_data', 'nifty_data_archive', 'date < NOW() - INTERVAL \'5 years\'')
    update_schema()