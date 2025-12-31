import duckdb
from loguru import logger

# Connect to/create the DucDB database

con = duckdb.connect("sharp_npq.duckdb")


# Create table for monitoring stations
con.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            id INTEGER PRIMARY KEY,
            code TEXT UNIQUE,
            name TEXT,
            lake TEXT,
            latitude DOUBLE,
            longitude DOUBLE
    );
    """)

# Create table for CTD profile metadata
con.execute("""
CREATE TABLE IF NOT EXISTS ctd_profiles (
            id INTEGER PRIMARY KEY,
            station_code TEXT, 
            profile_date DATE,
            source_file TEXT, 
            file_year INTEGER
            );
""")

# Create table for CTD profile measurements
con.execute("""
CREATE TABLE IF NOT EXISTS ctd_measurements (
            id INTEGER PRIMARY KEY,
            profile_id INTEGER,
            depth_m DOUBLE,
            temperature_c DOUBLE,
            chla_ugL DOUBLE,
            other_data TEXT
);
""")

# Create table for fluorometer deployment metadata
con.execute("""
CREATE TABLE IF NOT EXISTS fluorometer_deployments (
            id INTEGER PRIMARY KEY,
            station_code TEXT,
            isntrument_model TEXT,
            deployment_date DATE,
            deploymnet_depth_m DOUBLE,
            source_file TEXT
);          
""")

# Create table for fluorometer time series measurements
con.execute("""
CREATE TABLE IF NOT EXISTS fluorometer_measurements(
            id INTEGER PRIMARY KEY,
            deployment_id INTEGER,
            timestamp TIMESTAMP,
            chla_ugL DOUBLE,
            temperature_c DOUBLE,
            corrected_chla_ugL DOUBLE,
            notes TEXT
);
""")

con.close()
logger.info("DuckDB schema created in shape_npq.duckdb")