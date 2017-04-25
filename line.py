for line in exampleFile:
    try:
        firmscreen = str('https://tracker.serengetilaw.com/tracker/MasterFirmInfo?id=' + str(line))
        browser.visit(firmscreen)
        alert = browser.get_alert()
        alert.accept()
        browser.find_by_text("ACTIONS").first.click()
        browser.find_link_by_partial_text('Add This Firm').first.click()
        office = browser.find_by_id('idcboClassID').first
        office.select('5000')
        with open("FirmLog.txt", "a") as myfile:
            myfile.write(line)
        time.sleep(1)
    except Exception as e: print(e)
    continue
