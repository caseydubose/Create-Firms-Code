from splinter import Browser
import time

# You'll need to install Splinter and Chromium's pack to be able to run Chrome
# However, this should be able to run with Splinter's IE process
# I haven't bothered with relative paths to the files yet so that'll need updates
# as well as you'll need to create a cred file and define the absolute path.

#select Company
print('What is the Company Name?')
CompanyName = input()

# import files
exampleFile = open("C:\\Users\\U0127576\Dropbox\Programming\Python\Create Firms\\firmlist.txt")
with open('C:\\Users\\U0127576\Dropbox\Programming\Python\Credentials\creds.txt') as credFile:
    cred_lines = list(credFile)


# initialize browser
browser = Browser('chrome')

# login
browser.visit('https://tracker.serengetilaw.com/tracker/Logon?szReturn=/')
browser.find_by_id('logonUserID').first.fill(cred_lines[0])
browser.find_by_id('btnLogon').first.click()
browser.find_by_id('logonPassword').first.fill(cred_lines[1])
browser.find_by_id('btnLogon').first.click()

# pick company DB
browser.find_by_text(CompanyName).first.click()
time.sleep(1)

# Create Firm Loop | Comment the Save & Close line if you want to test
for line in exampleFile:
    try:
        firmscreen = str('https://tracker.serengetilaw.com/tracker/MasterFirmInfo?id=' + str(line))
        browser.visit(firmscreen)

        try:
            alert = browser.get_alert()
            alert.accept()
        except Exception as e:
            pass

        browser.find_by_text("ACTIONS").first.click()
        browser.find_link_by_partial_text('Add This Firm').first.click()
        time.sleep(2)
        office = browser.find_by_id('idcboClassID').first
        office.select('5000')
        browser.find_by_text("ACTIONS").first.click()
        browser.find_link_by_partial_text('Save & Close').first.click()
        with open("C:\\Users\\U0127576\Dropbox\Programming\Python\Create Firms\FirmLog.txt", "a") as myfile:
            myfile.write(line)
        time.sleep(1)
    except Exception as e:
        print(e)
        with open("C:\\Users\\U0127576\Dropbox\Programming\Python\Create Firms\FirmLog.txt", "a") as myfile:
            myfile.write(line + str(e))
