import csv
import sqlite3

con = sqlite3.connect("echelon.db")
cursor = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'instagram','shell:AppsFolder\Facebook.InstagramBeta_8xx8rvfyw5nnt!App')"
#query = "DELETE FROM sys_command WHERE id = 2"
#cursor.execute(query)
#con.commit()



#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'figma','https://www.figma.com/')"
#cursor.execute(query)
#con.commit()

# Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
#desired_columns_indices = [0, 18]

# Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    #csvreader = csv.reader(csvfile)
    #for row in csvreader:
        #selected_data = [row[i] for i in desired_columns_indices]
        #cursor.execute(''' INSERT INTO contacts (id, 'Name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
#con.commit()
#con.close()


#query = 'mummy'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])




#name = "Batuk"
#mobile_no = "+919825373035"

#cursor.execute('''
    #INSERT INTO contacts (id, Name, mobile_no)
    #VALUES (NULL, ?, ?)
#''', (name, mobile_no))

# Commit and close
#con.commit()
#con.close()

