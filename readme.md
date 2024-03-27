
# Neo4j CSV Importer

This Python script is designed to import CSV data into a Neo4j graph database. It utilizes the `neo4j` Python driver to connect to a Neo4j database and process CSV files containing data about relationships between papers.

## Prerequisites

Before using this script, make sure you have the following installed:

- Python 3.x
- `neo4j` Python driver (`pip install neo4j`)
- A running Neo4j instance with access via Bolt protocol (`bolt://`)

## Setup

1. Clone or download this repository to your local machine.
2. Install dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Update the `uri`, `user`, and `password` variables in `importer.py` with your Neo4j credentials.

## Usage

1. Place your CSV files containing paper relationship data inside a directory.
2. Configure the Neo4j server to specify the directory containing CSV files for import. Edit the `neo4j.conf` file and add the following line:
   ```
   server.directories.import=/path/to/csv
   ```
   Replace `/path/to/csv` with the actual path to the directory containing your CSV files.
   
3. Run the script `importer.py`:
   ```
   python importer.py
   ```
4. The script will process each CSV file in the directory, importing the data into Neo4j.

## Estimated Remaining Time

The script provides an estimate of the remaining time based on the average speed of processing CSV files. This estimate is updated after processing each file.

## Neo4j Configuration

### Memory Size

To increase memory size in Neo4j, follow these steps:

1. Locate your Neo4j configuration file. It is typically named `neo4j.conf`.
2. Open the configuration file in a text editor.
3. Find the `dbms.memory.heap.initial_size` and `dbms.memory.heap.max_size` properties.
4. Adjust the values of these properties to increase memory allocation. For example:
   ```
   dbms.memory.heap.initial_size=2G
   dbms.memory.heap.max_size=4G
   ```

   This allocates 2GB of memory initially, with a maximum of 4GB. Adjust the values according to your system's resources and requirements.

## Directory Structure

```
.
├── importer.py        # Python script for importing CSV data into Neo4j
├── readme.md          # This README file
├── requirements.txt   # List of Python dependencies
└── text data          # Directory for storing CSV files
    └── 2023-05-09T174629_0_1.csv   # Example CSV file
```

Make sure to replace the example CSV file with your own data files.

---

Feel free to customize this README further according to your specific requirements or preferences.
```

This revision adds a section to the "Usage" part of the README, explaining how to configure the Neo4j server to specify the directory containing CSV files for import.