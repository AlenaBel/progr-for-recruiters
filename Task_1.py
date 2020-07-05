import csv
name = input('Enter your name: ')
email = input('Enter your email: ')
phone = input('Enter your phone number: ')
github = input('Enter link to your Github profile: ')
job = input('Are you looking for a new job?')
if job == 'yes':
    np = input('What is your notice period?(asap/x days/weeks/months)')
    if np == 'asap':
        print('Dear %s, we will contact you within 1 business day' % name)
        save = input('Save to CSV? ')
        if save == 'yes':
          file = open('results.csv', 'a')
          csv_writer = csv.writer(file)
          csv_writer.writerow([name, github, email, phone, job, np])
        pass
    else:
        save = input('Save to CSV? ')
        if save == 'yes':
          file = open('results.csv', 'a')
          csv_writer = csv.writer(file)
          csv_writer.writerow([name, github, email, phone, job, np])
          pass
    pass
else:
    save = input('Save to CSV?')
    if save == 'yes':
        file = open('results.csv', 'a')
        csv_writer = csv.writer(file)
        csv_writer.writerow([name, github, email, phone, job])
    pass