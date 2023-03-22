import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#removed spacing before
manualDataset = pd.read_csv('/Users/I565652/PycharmProjects/360_Degrees_Of_Data/EuropeHotelBookingSatisfactionScore.csv')
AverageRatingColumn = "AverageRating"

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
    output = pd.read_csv('/Users/I565652/PycharmProjects/360_Degrees_Of_Data/output.csv')
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
    with open('output.csv') as input_file, open('4starHotels.csv', 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Write the header row to the output file
        header = next(reader)
        writer.writerow(header)

        # Loop through each row in the input file
        for row in reader:
            validate = float(row[17])
            # Check if the row meets the specific requirement
            if validate > 4:  # replace 'value' with your specific requirement
                # Write the row to the output file if it meets the requirement
                writer.writerow(row)

def print_welcome(name):
    print(f'Hi! {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_welcome("Welcome to my project for 360 degrees of data!")
    verifyManualLoad()

    #Overview about dataset
    #manualDataset.info()

    #Calculate rating average, plot averages and then filter the ones that have more than 4 on average
    addAverage()
    plotAverage()
    filterOnlyAbove4Stars()



