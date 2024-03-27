import os
from neo4j import GraphDatabase
import time

uri = "bolt://localhost:7687"
user = "aaaaaaaa"
password = "aaaaaaaa"  # Make sure to replace this with your actual password

driver = GraphDatabase.driver(uri, auth=(user, password))

def process_file(session, file_path):
    start_time = time.time()
    query = """
    LOAD CSV WITH HEADERS FROM $file_uri AS row
    WITH row
    WHERE row.citing IS NOT NULL AND row.cited IS NOT NULL AND row.id IS NOT NULL
    CALL {
        WITH row
        MERGE (citing:Paper {id: row.citing})
        MERGE (cited:Paper {id: row.cited})
        MERGE (citing)-[:CITED {id: row.id}]->(cited)
    } IN TRANSACTIONS OF 100000 ROWS;
    """

    session.run(query, file_uri=f"file:///{os.path.basename(file_path)}")
    return time.time() - start_time

def estimate_remaining_time(directory_path):
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    total_size = sum(os.path.getsize(os.path.join(directory_path, f)) for f in csv_files)
    processed_size = 0
    total_time_taken = 0
    
    with driver.session() as session:
        for file_name in csv_files:
            file_path = os.path.join(directory_path, file_name)
            file_size = os.path.getsize(file_path)
            print(f"Processing {file_name} (Size: {file_size} bytes)")
            
            time_taken = process_file(session, file_path)
            processed_size += file_size
            total_time_taken += time_taken
            
            average_speed = total_time_taken / processed_size
            remaining_size = total_size - processed_size
            estimated_time_remaining = remaining_size * average_speed
            
            print(f"Completed {file_name}. Time taken: {time_taken:.2f} seconds")
            print(f"Estimated time remaining: {estimated_time_remaining:.2f} seconds")
    
    print("All files processed.")

# Set your directory path
directory_path = '/media/veracrypt5/as/'
estimate_remaining_time(directory_path)

driver.close()
