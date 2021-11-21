import sqlite3
conn = sqlite3.connect('airbnb.db')
cursor = conn.cursor()

import pandas as pd
neighborhoods_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/neighborhoods.csv"
hosts_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/hosts.csv"
locations_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/locations.csv"
listings_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/listings.csv"

hosts_df = pd.read_csv(hosts_url)
neighborhoods_df = pd.read_csv(neighborhoods_url)

locations_df = pd.read_csv(locations_url)
listings_df = pd.read_csv(listings_url)

hosts_df.to_sql('hosts',conn, index = False, if_exists = 'replace')
neighborhoods_df.to_sql('neighborhoods',conn, index = False, if_exists = 'replace')
locations_df.to_sql('locations',conn, index = False, if_exists = 'replace')
listings_df.to_sql('listings', conn, index = False, if_exists = 'replace')


def display_tables():
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    return cursor.fetchall()

def display_schema(table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    cursor.fetchall()

def listing_name_of_highest_price():
    pass

def id_of_location_with_lowest_longitude():
    pass

def greatest_occupancy_of_listing():
    pass

def avg_price_of_listing():
    pass

def number_of_hosts():
    pass

def longitude_and_latitude_of_listing_with_highest_price():
    pass

def neighborhood_id_of_lowest_price_listing():
    pass

def long_lat_of_lowest_price_listing():
    pass

def host_with_most_reviews():
    pass


def host_name_with_lowest_avg_listing_price():
    pass

def neighborhood_with_most_locations():
    pass

def neighborhood_with_exactly_ten_locations():
    pass
    

    
    

    
    

    
    
