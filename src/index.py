import sqlite3
conn = sqlite3.connect('airbnb.db')
cursor = conn.cursor()

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
    

    
    

    
    

    
    
