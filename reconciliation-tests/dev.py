from turtle import fill
import pytest
import os
import re
from datetime import datetime
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://dev.finance-ops.ai/en/sign-in"
EMAIL = "chirag.bhatia@paymentoptions.com"
PASSWORD = "tmj3sPFwwRc5Kjx@"

REFERENCE_DATA_FILE = r"C:\Users\ghans\OneDrive\Desktop\reference table test.csv"




def test_full_reconciliation_flow(pytestconfig):
    PIPELINE_NAME = pytestconfig.getoption("--pipeline_name")
    PIPELINE_CODE = pytestconfig.getoption("--pipeline_code")
    REFERENCE_DATA_NAME = pytestconfig.getoption("--reference_data_name")
    REFERENCE_DATA_NAME2 = pytestconfig.getoption("--reference_data_name2")
    REFERENCE_DATA_NAME3 = pytestconfig.getoption("--reference_data_name3")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(BASE_URL)
        page.wait_for_timeout(3000)

        page.get_by_role("textbox", name="johndoe@test.com").fill(EMAIL)
        page.get_by_role("textbox", name="* Password question-circle").fill(PASSWORD)
        page.get_by_role("button", name="Sign In").click()

        page.wait_for_url("**/en/**")
        print(f"✅ Step 1 – Logged in as {EMAIL}")


        #Reference Table CREATION

        # MANUAL

        page.get_by_role("link", name="Reference Data").click()
        # page.get_by_role("button", name="plus CREATE TABLE").click()
        # page.get_by_role("textbox", name="Enter Name").click()
        # page.get_by_role("textbox", name="Enter Name").fill("TEST"+REFERENCE_DATA_NAME)
        # page.get_by_role("button", name="Column", exact=True).click()
        # page.get_by_role("textbox", name="Column name").fill("PO")
        # page.get_by_role("button", name="Add column").click()
        # page.get_by_role("textbox", name="Column name").fill("AB")
        # page.get_by_role("button", name="Row", exact=True).click()
        # page.get_by_role("textbox", name="—").first.click()
        # page.get_by_role("textbox", name="—").first.fill("AMEX")
        # page.get_by_role("textbox", name="—").nth(1).click()
        # page.get_by_role("textbox", name="—").nth(1).fill("american expressway")
        # page.get_by_role("button", name="Row", exact=True).click()
        # page.get_by_role("textbox", name="—").nth(2).click()
        # page.get_by_role("textbox", name="—").nth(2).fill("VISA")
        # page.get_by_role("textbox", name="—").nth(3).click()
        # page.get_by_role("textbox", name="—").nth(3).fill("visa")
        # page.get_by_role("button", name="Row", exact=True).click()
        # page.get_by_role("textbox", name="—").nth(4).click()
        # page.get_by_role("textbox", name="—").nth(4).fill("JCB")
        # page.get_by_role("textbox", name="—").nth(5).click()
        # page.get_by_role("textbox", name="—").nth(5).fill("JCB")
        # page.get_by_role("button", name="Add a row").click()
        # page.locator("tr:nth-child(4) > td:nth-child(2) > .w-full").click()
        # page.locator("tr:nth-child(4) > td:nth-child(2) > .w-full").fill("MASTERCARD")
        # page.locator("tr:nth-child(4) > td:nth-child(3) > .w-full").click()
        # page.locator("tr:nth-child(4) > td:nth-child(3) > .w-full").fill("mastercard")
        # page.get_by_role("button", name="SAVE").click()
        
        # page.wait_for_timeout(1800)

        # #IMPORT

        # page.get_by_role("button", name="plus CREATE TABLE").click()
        # page.get_by_role("textbox", name="Enter Name").click()
        # page.get_by_role("textbox", name="Enter Name").fill("TEST"+REFERENCE_DATA_NAME2)
        # page.get_by_role("button", name="Import/Export").click()
        # page.get_by_text("Import CSV").click()
        # page.wait_for_timeout(3000)
        # with page.expect_file_chooser() as fc_right:
        #      page.locator("div").filter(has_text="Import CSVUpload a CSV file").nth(4).click()
        #      fc_right.value.set_files(REFERENCE_DATA_FILE)
        #      page.get_by_role("button", name="Import 4 rows").click()
        #      page.get_by_role("button", name="SAVE").click()


        #POPULATE from PIPELINE 


        page.get_by_role("button", name="plus CREATE TABLE").click()
        page.get_by_role("textbox", name="Enter Name").click()
        page.get_by_role("textbox", name="Enter Name").fill("TEST"+REFERENCE_DATA_NAME3)
        page.get_by_role("button", name="Import/Export").click()
        page.get_by_role("menuitem", name="Populate from Pipeline").click()
        page.locator("#rc_select_52").click()
        page.locator("#rc_select_52").fill("KhbwyH")
        page.get_by_text("KhbwyH").click()
        page.locator("#rc_select_53").click()
        page.get_by_text("TRANSACTION EVENT").click()
        page.get_by_role("button", name="Preview").click()
        page.get_by_role("button", name="Populate Table").click()
        page.get_by_role("button", name="SAVE").click()








        page.wait_for_timeout(2000)

        file_name = os.path.basename(__file__).replace(".py", "")
        os.makedirs("test_failures", exist_ok=True)

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        page.screenshot(path=f"test_failures/{file_name}_{timestamp}.png")