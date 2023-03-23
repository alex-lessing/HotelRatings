import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import sqlite3

manualDataset = pd.read_csv('/Users/I565652/PycharmProjects/360_Degrees_Of_Data/EuropeHotelBookingSatisfactionScore.csv')
AverageRatingColumn = "AverageRating"

def print_welcome(name):
    print(f'Hi! {name}')  # Press ⌘F8 to toggle the breakpoint.

def setupSQLite():
    conn = sqlite3.connect('mySmallDb.db')
    c = conn.cursor()
    conn.execute('DROP TABLE IF EXISTS data')
    insertData(c)

    #1st SQL query: Calculate rating average
    c.execute('''
               SELECT id, round((Hotel_wifi_service+Departure_Arrival_convenience+ 
                            Ease_of_online_booking+Hotel_location+Food_and_drink+Stay_comfort+ 
                            Common_room_entertainment+Checkin_Checkout_service+Other_service+ 
                            Cleanliness+satisfaction)/(11*1.0), 1) as averageRating
               FROM data
                 ''')
    # fetch the results
    results = c.fetchall()
    # print the results
    print("\nHotel ID, Average Rating")
    #Print first 20 results
    for row in results[20:30]:
        print(row)

    #2nd SQL query: Filter to keep only hotels with an averge rating above 4 stars
    c.execute('''SELECT id, round((Hotel_wifi_service+Departure_Arrival_convenience+ 
                            Ease_of_online_booking+Hotel_location+Food_and_drink+Stay_comfort+ 
                            Common_room_entertainment+Checkin_Checkout_service+Other_service+ 
                            Cleanliness+satisfaction)/(11*1.0), 1) as averageRating
               FROM data
               WHERE averageRating > 3.9
               --ORDER BY averageRating desc
                     ''')
    # fetch the results
    results = c.fetchall()
    # print the results
    print("\nHotel ID with rating of at least 4.0, Average Rating")
    # Print first 20 results
    for row in results[:20]:
        print(row)

    #end database connection
    conn.commit()

def insertData(c):
    c.execute('''CREATE TABLE data
                     (id text,gender text,age text,purpose_of_travel text,Type_of_travel text,type_of_booking text,
                     Hotel_wifi_service text,
                     Departure_Arrival_convenience text,
                     Ease_of_online_booking text,
                     Hotel_location text,Food_and_drink text,Stay_comfort text,Common_room_entertainment text,Checkin_Checkout_service text,
                     Other_service text,Cleanliness text,satisfaction text)''')

    with open('EuropeHotelBookingSatisfactionScore.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            c.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

def verifyManualLoad():
    # Verify if the DataFrame is not empty
    if not manualDataset.empty:
        print('CSV file loaded successfully')
    else:
        print('Error loading CSV file')

def addAverage():
    """Summarize all values to create a new column with average of all given reviews ( 9 in total)"""

    # Open the input CSV file for reading and create a new CSV file for writing
    with open('EuropeHotelBookingSatisfactionScore.csv', 'r') as \
            input_file, open('output.csv', 'w', newline='') as output_file:
        # Create CSV reader and writer objects
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Read the header row and add the new column header
        header_row = next(reader)
        header_row.append(AverageRatingColumn)
        writer.writerow(header_row)

        # Process each data row and add the new column value
        for row in reader:
            rowList = row[6:15]
            # Compute the new column value for the current row
            new_column_value = sum(map(int, rowList))
            new_column_value /= len(rowList)

            # Add the new column value to the row and write it to the output file
            row.append(round(new_column_value, 1))
            writer.writerow(row)

def plotAverage():
    # plot those count of how many hotels between 1-2, 2-3, 3-4, 4-5
    # Create a histogram plot of the attribute values
    output = pd.read_csv('output.csv')
    plt.hist(output[AverageRatingColumn], bins=[1, 2, 3, 4, 5], edgecolor='black', label='Test')

    # Set the plot title and axis labels
    plt.title('Number of hotels per rating\n')
    plt.xlabel('Customer rating (out of 5 stars)')
    plt.ylabel('Number of hotels')
    # Set the x-tick frequency to every 1.0
    plt.xticks(np.arange(1, 6, 1))

    # Display the plot
    plt.show()

def filterOnlyAbove4Stars():
    """This method shows all hotels with an average rating of above 4 stars"""

    # Open the input and output CSV files
    with open('output.csv') as input_file, open('4starHotels.csv', 'w', newline='') \
            as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Write the header row to the output file
        header = next(reader)
        writer.writerow(header)

        # Loop through each row in the input file
        for row in reader:
            validate = float(row[17])
            # Check if the row meets the specific requirement
            if validate > 3.9:  # replace 'value' with your specific requirement
                # Write the row to the output file if it meets the requirement
                writer.writerow(row)

if __name__ == '__main__':
    print_welcome("Welcome to my project for 360 degrees of data!")
    verifyManualLoad()
    # Overview about dataset
    print("\nProviding some general information about the dataset:")
    manualDataset.info()

    #Do it via SQL
    setupSQLite()

    #Calculate rating average, plot averages and then filter the ones that have more than 4 on average
    addAverage()
    plotAverage()
    filterOnlyAbove4Stars()



