import time
from Selenium.DemoQA.reusablefiles.General import *


def test_webtables():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    time.sleep(1)
    select_submenu_item(driver, "Web Tables")
    table = dict()
    headers = [ele_header.text for ele_header in driver.find_elements(By.XPATH, '//div[@role="row"]/div[@role="columnheader"]/div[text()]')]
    for header in headers:
        table[header] = []
    print(table)
    for i in range(1, len(table)):
        for ele_column_value in driver.find_elements(By.XPATH, f'//div[@role="rowgroup"]//div[@role="gridcell" and text()][{i}]'):
            table[headers[i-1]].append(ele_column_value.text)
    print(table[headers[0]])

    col_firstname = table['First Name']
    for i in range(len(col_firstname)):
        if col_firstname[i] == 'Alden':
            print('Value based on table')
            print(table['Email'][i])
            break

    records = []
    for ele_row in driver.find_elements(By.XPATH, '//div[@role="rowgroup"]'):
        records.append([])
        for ele_cell in ele_row.find_elements(By.XPATH, 'div/div[@role="gridcell" and text()]'):
            records[-1].append(ele_cell.text)
    print(records)

    for record in records:
        if record[headers.index('First Name')] == 'Alden':
            print('Value based on records')
            print(record[headers.index('Email')])
            break

    time.sleep(2)
    tear_down(driver)
