# This downloads NYMEX futures from the CME group FTP and prints the CSV to the console.
# View the notice at https://www.cmegroup.com/market-data/settlements.html for usage restrictions.

import ftplib
import csv

def print_csv(bytes):
    # You could write the CSV to another file here, load into a data frame, filter by product or
    # description, etc.
    for line in csv.reader(bytes.decode('utf-8').splitlines()):
        print(line)

connection = ftplib.FTP("ftp.cmegroup.com")
connection.login()
connection.retrbinary("RETR /settle/nymex_future.csv", print_csv)
connection.quit()
