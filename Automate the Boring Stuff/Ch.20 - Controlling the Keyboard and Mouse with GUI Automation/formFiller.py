#! python3
# formFiller.py - Automatically fills in the form.
import pyautogui, time, openpyxl
# below is the link of said form
# https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform
# Opening the excel files and compiling into a dict_
wb = openpyxl.load_workbook('Automate the Boring Stuff\Ch.20 - Controlling the Keyboard and Mouse with GUI Automation\GenericFormInfo.xlsx')
sheet = wb['Sheet1']
column_len =  sheet.max_column
row_len = sheet.max_row
formData = []
for row in range(2, row_len + 1):
    dict_= {}
    for column in range(1, column_len + 1):
        dict_key = sheet.cell(row = 1, column = column).value
        dict_value = sheet.cell(row = row, column = column).value
        dict_[dict_key] = dict_value
    formData.append(dict_)
# brief pause
pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')
for person in formData:
    # Gives the user a chance to kill the script by keyboard interrupt or mouse out of screen
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t', '\t'])
    # Fill out the Name filed.
    pyautogui.write(person['name'] + '\t')
    pyautogui.write(person['fear'] + '\t')
    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)
    # Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui.write(['space', '\t'], 0.5)
    if person['robocop'] == 2:
        pyautogui.write(['right', '\t'], 0.5)
    if person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'], 0.5)
    if person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
    if person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right','\t'], 0.5)
    # Fill out the Additional Comments field.
    pyautogui.write('\t' + person['comments'] + '\t')
    # 'Click' Submit button by pressing Enter.
    time.sleep(0.5)  # Wait for the button to activate.
    pyautogui.press('enter')
    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)
    # CLick the Submit another response link.
    pyautogui.click('Automate the Boring Stuff\Ch.20 - Controlling the Keyboard and Mouse with GUI Automation\Submit.png')
