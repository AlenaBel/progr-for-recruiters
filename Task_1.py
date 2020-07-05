import csv
name = input('Enter your name: ')
email = input('Enter your email: ')
phone = input('Enter your phone number: ')
github = input('Enter link to your Github profile: ')
save = input('Save to CSV? ')
if save == 'yes':
 file = open('results.csv', 'a')
 csv_writer = csv.writer(file)
 csv_writer.writerow([name, github, email, phone])