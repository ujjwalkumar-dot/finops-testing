import datetime
import re
import pytest
from playwright.sync_api import sync_playwright, expect
import os
from datetime import datetime


# ── Static Config ─────────────────────────────────────────────────────────────
BASE_URL = "https://dev.finance-ops.ai/en/sign-in"
EMAIL = "chirag.bhatia@paymentoptions.com"
PASSWORD = "tmj3sPFwwRc5Kjx@"

LEFT_FILE = r"C:\Users\ghans\Downloads\wp-11oct-31oct\28oct.xlsx"
RIGHT_FILE = r"C:\Users\ghans\Downloads\wp-11oct-31oct\2025-10-29\report.csv"


def test_full_reconciliation_flow(pytestconfig):

    PIPELINE_NAME = pytestconfig.getoption("--pipeline_name")
    PIPELINE_CODE = pytestconfig.getoption("--pipeline_code")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ── Step 1: Login ─────────────────────────────────────────────────────
        page.goto(BASE_URL)
        page.wait_for_timeout(3000)

        page.get_by_role("textbox", name="johndoe@test.com").fill(EMAIL)
        page.get_by_role("textbox", name="* Password question-circle").fill(PASSWORD)
        page.get_by_role("button", name="Sign In").click()

        page.wait_for_url("**/en/**")
        print(f"✅ Step 1 – Logged in as {EMAIL}")

        # ── Step 2: Create Pipeline ───────────────────────────────────────────
        page.get_by_role("link", name="Pipelines").click()
        page.get_by_role("button", name="plus   Create Pipeline").click()

        page.get_by_role("textbox", name="Enter Pipeline Name").fill(PIPELINE_NAME)
        page.get_by_role("textbox", name="Enter Pipeline Code").fill(PIPELINE_CODE)
        page.get_by_role("textbox", name="Enter Data Label Singular").fill("data")

        page.get_by_role("textbox", name="Enter Data Label Plural").click()
        page.locator(".flex.flex-col.h-\\[calc\\(100vh-90px\\)\\]").click()

        page.get_by_role("button", name="SAVE & CONTINUE").click()
        print(f"✅ Step 2 – Pipeline created: {PIPELINE_NAME}")

        # ── Step 3: Configure Sides & Upload Files ────────────────────────────
        page.get_by_role("textbox", name="* LEFT SIDE question-circle").click()
        page.get_by_role("textbox", name="* LEFT SIDE question-circle").fill("PO")

        page.get_by_role("textbox", name="* RIGHT SIDE question-circle").click()
        page.get_by_role("textbox", name="* RIGHT SIDE question-circle").fill("WP")
        

        # Left Source → Computer
        page.get_by_text("Computer").first.click()
        page.locator("#sourceL_list_0").get_by_text("Computer").click()

        # Right Source → Computer
        page.get_by_text("Computer").nth(2).click()
        page.locator("#sourceR_list_0").get_by_text("Computer").click()

        # File Type Left → XLSX
        page.locator("#fileType1").click()
        page.get_by_text("XLSX").click()

        # File Type Right → XLSX
        page.locator("#fileType2").click()
        page.locator("#fileType2_list_11").get_by_text("CSV").click()

        # Upload LEFT file
        with page.expect_file_chooser() as fc_left:
            page.get_by_role("button", name="inbox Maximum file size 50 MB").first.click()
        fc_left.value.set_files(LEFT_FILE)
        page.wait_for_timeout(3000)
        print(f"✅ Step 3a – Left file uploaded: {LEFT_FILE}")

        # Upload RIGHT file
        with page.expect_file_chooser() as fc_right:
            page.get_by_role("button", name="inbox Maximum file size 50 MB").nth(1).click()
        fc_right.value.set_files(RIGHT_FILE)
        page.wait_for_timeout(2000)
        print(f"✅ Step 3b – Right file uploaded: {RIGHT_FILE}")

        # Wait for files to register then click Save & Continue
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Save & Continue").click()
        print("✅ Step 3 – Save & Continue clicked")

        # ── Wait 5s then re-enter pipeline for refresh workaround ─────────────
        page.wait_for_timeout(15000)
        # page.reload()
        

        # ── Step 4: Configure Column Types ───────────────────────────────────
       
        page.locator("#L_edit_button_for_AMOUNT").click()
        page.locator(".ant-select.ant-select-outlined.ant-select-in-form-item > .ant-select-selector").click()
        page.get_by_title("AMOUNT").locator("#L_field_type_AMOUNT").click()
        page.get_by_role("button", name="SAVE", exact=True).click()
        page.locator("#L_edit_button_for_CURRENCY").click()
        page.get_by_role("tooltip").get_by_title("TEXT").click()
        page.get_by_title("CURRENCY").nth(1).click()
        page.get_by_role("button", name="SAVE", exact=True).click()
        page.reload();
        page.wait_for_timeout(2000)
        page.locator("#R_edit_button_for_Amount").click()
        page.locator(".ant-select.ant-select-outlined.ant-select-in-form-item > .ant-select-selector").click()
        page.get_by_title("AMOUNT").locator("#R_field_type_AMOUNT").click()
        page.get_by_role("button", name="SAVE", exact=True).click()
        page.wait_for_timeout(7000)
        page.get_by_role("button", name="SAVE & CONTINUE").click()
        page.wait_for_timeout(2000)
        
        print("✅ Step 4 – Column types configured")

        # ── Step 5: Field Mapping ──
        page.locator("[id=\"schema_left_schema_item_TRANSACTION REF ID\"]").click()
        page.locator("#schema_right_schema_item_OrderCode").click()
        page.get_by_role("button", name="Show all fields").click()
        page.locator("[id=\"schema_left_schema_item_TRANSACTION EVENT\"]").click()
        page.locator("#schema_right_schema_item_Status").click()
        page.get_by_role("button", name="Show all fields").click()
        page.locator("#schema_left_schema_item_AMOUNT").click()
        page.locator("#schema_right_schema_item_Amount").click()
        page.get_by_role("button", name="Show all fields").click()
        page.locator("#schema_left_schema_item_CURRENCY").click()
        page.locator("#schema_right_schema_item_CurrencyCode").get_by_text("JPY").click()
        page.get_by_role("button", name="Show all fields").click()



        #Transformation Rules
       #1. Transaction Ref ID
        page.get_by_text("TRANSACTION REF ID").nth(2).click()
        page.locator("div").filter(has_text=re.compile(r"^Something$")).nth(2).click()
        page.get_by_role("option", name="If Something Then Something").click()
        page.locator("div").filter(has_text=re.compile(r"^Please Select$")).nth(3).click()
        page.get_by_role("option", name="Something is not equal to").click()
        page.locator("div").filter(has_text=re.compile(r"^Select Value Type$")).nth(2).click()
        page.get_by_role("option", name="A Field", exact=True).click()
        page.locator("div").filter(has_text=re.compile(r"^Please Select a Field$")).nth(3).click()
        page.get_by_role("option", name="ORIGINAL TRANSACTION ID", exact=True).click()
        #page.locator("#rc_select_7_list_24").get_by_text("ORIGINAL TRANSACTION ID").click()
        page.locator("div").filter(has_text=re.compile(r"^Select Rule Type$")).nth(2).click()
        page.get_by_role("option", name="Set to Something").click()
        page.locator("div").filter(has_text=re.compile(r"^Select Value Type$")).nth(5).click()
        page.get_by_role("option", name="A Field", exact=True).click()
        page.locator("div").filter(has_text=re.compile(r"^Please Select a Field$")).nth(3).click()
        page.get_by_role("option", name="ORIGINAL TRANSACTION ID", exact=True).click()
        #page.locator("#rc_select_9_list_24").get_by_text("ORIGINAL TRANSACTION ID").click()
        page.locator("div").filter(has_text=re.compile(r"^Select Value Type$")).nth(2).click()
        page.get_by_role("option", name="A Text").click()
        page.get_by_text("Click to edit").click()
        page.get_by_role("textbox", name="Enter text").fill("N/A")
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(2000)


        #2. status

        page.locator("span").filter(has_text="Status").click()
        page.get_by_text("Something").click()
        page.get_by_text("If Something Then Something").click()
        page.get_by_text("Please Select").click()
        page.get_by_role("option", name="Something is equal to").click()
        page.get_by_text("Select Value Type").first.click()
        page.get_by_text("A Field", exact=True).click()
        page.locator("div").filter(has_text=re.compile(r"^Please Select a Field$")).nth(3).click()
        page.get_by_role("option", name="Status", exact=True).click()
        page.get_by_text("Select Value Type").click()
        page.get_by_text("A Text").click()
        page.get_by_text("Select Rule Type").click()
        page.get_by_text("Set to Something").click()
        page.locator("div").filter(has_text=re.compile(r"^Select Value Type$")).nth(2).click()
        page.get_by_text("A Text").click()
        page.get_by_text("Click to edit").nth(1).click()
        page.get_by_role("textbox", name="Enter text").fill("REFUNDED")
        page.get_by_text("Click to edit").click()
        page.get_by_role("textbox", name="Enter text").fill("REFUNDED_BY_MERCHANT")
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(1000)
        print(" Step 5 - Mapping completed And Rules applied")
        page.get_by_role("button", name="SAVE & CONTINUE").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="MARK AS COMPLETE & EXIT").click()
        page.wait_for_timeout(5000)

        page.get_by_text(PIPELINE_CODE).first.click()
        page.wait_for_timeout(2000)


         #FILTER RULE FOR WP
        
        page.get_by_role("button", name="Run").click()
        page.wait_for_timeout(3000)
        #screenshot

        file_name = os.path.basename(__file__).replace(".py", "")
        os.makedirs("test_failures", exist_ok=True)

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        page.screenshot(path=f"test_failures/{file_name}_{timestamp}.png")

        page.locator("div").filter(has_text=re.compile(r"^Search and select a field mapping$")).nth(1).click()
        page.get_by_text("TRANSACTION REF ID").click()
        page.get_by_role("button", name="Apply & Run").click()





       


   
