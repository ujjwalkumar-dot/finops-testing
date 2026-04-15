import datetime
import re
import pytest
from playwright.sync_api import sync_playwright, expect


# ── Static Config ─────────────────────────────────────────────────────────────
BASE_URL = "https://dev.finance-ops.ai/en/sign-in"
EMAIL = "chirag.bhatia@paymentoptions.com"
PASSWORD = "tmj3sPFwwRc5Kjx@"

LEFT_FILE = r"C:\reconciliation-tests\Excel-data\New Microsoft Excel Worksheet.xlsx"
RIGHT_FILE = r"C:\reconciliation-tests\Excel-data\New Microsoft Excel Worksheet - Copy.xlsx"
LEFT2_FILE = r"C:\reconciliation-tests\Excel-data\New Microsoft Excel Worksheet -(2).xlsx"
RIGHT2_FILE = r"C:\Users\ghans\OneDrive\Desktop\New Microsoft Excel Worksheet - Copy - Copy.xlsx"


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
        page.locator("#fileType2_list_13").get_by_text("XLSX").click()

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

        with page.expect_file_chooser() as fc_left:
         page.get_by_role("button", name="inbox Maximum file size 50 MB").first.click()
        fc_left.value.set_files(LEFT2_FILE)
        page.wait_for_timeout(3000)
        print(f"✅ Step 3a – Left file uploaded: {LEFT2_FILE}")

        # Upload RIGHT file
        with page.expect_file_chooser() as fc_right:
            page.get_by_role("button", name="inbox Maximum file size 50 MB").nth(1).click()
        fc_right.value.set_files(RIGHT2_FILE)
        page.wait_for_timeout(2000)
        print(f"✅ Step 3b – Right file uploaded: {RIGHT2_FILE}")


        # Wait for files to register then click Save & Continue
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Save & Continue").click()
        print("✅ Step 3 – Save & Continue clicked")

        # ── Wait 5s then re-enter pipeline for refresh workaround ─────────────
        page.wait_for_timeout(10000)
        # page.get_by_role("link", name="Pipelines").click()
        # page.wait_for_timeout(5000)
        # page.get_by_text(PIPELINE_CODE).first.click()
        # page.wait_for_timeout(2000)
        # page.get_by_role("button", name="SAVE & CONTINUE").click()
        # page.wait_for_timeout(2000)
        # page.get_by_role("button", name="Save & Continue").click()
        # page.wait_for_timeout(4000)
        # print("✅ Step 3c – Re-entered pipeline after refresh")
        page.reload()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="Save & Continue").click()
        page.wait_for_timeout(4000)

        # ── Step 4: Configure Column Types ───────────────────────────────────
        # Column 1: TEXT → NUMBER
        page.get_by_role("button", name="edit").nth(2).click()
        page.get_by_title("TEXT").click()
        page.get_by_text("NUMBER").click()
        page.get_by_role("button", name="SAVE", exact=True).click()

        # Column 3: TEXT → NUMBER
        page.locator(
            "div:nth-child(3) > .flex.flex-col.items-start > .data-inputs-scrollable "
            "> div:nth-child(3) > .flex.justify-between.items-center > .group "
            "> .flex.flex-row.justify-between.mt-2 > .flex.flex-row > .gap-4 "
            "> .text-xs.text-\\[\\#2b7fff\\]"
        ).click()
        page.get_by_role("tooltip").get_by_title("TEXT").click()
        page.get_by_text("NUMBER").nth(3).click()
        page.get_by_role("button", name="SAVE", exact=True).click()
        page.reload();
        page.wait_for_timeout(2000)
        
        # Fix date auto-format glitch
        page.wait_for_timeout(2000)

        # Fix date auto-format glitch

        page.get_by_role("button", name="edit").nth(5).click()
        page.get_by_title("TEXT").click()
        page.get_by_title("DATETIME").click()
        page.locator("div").filter(has_text=re.compile(r"^YYYY-MM-DD HH:mm$")).nth(4).click(timeout=15000)
        page.get_by_title("YYYY-MM-DD HH:mm:ss").click()
        page.get_by_role("button", name="SAVE", exact=True).click()


         # Column 3: TEXT → NUMBER
        # page.locator(
        #     "div:nth-child(3) > .flex.flex-col.items-start > .data-inputs-scrollable "
        #     "> div:nth-child(3) > .flex.justify-between.items-center > .group "
        #     "> .flex.flex-row.justify-between.mt-2 > .flex.flex-row > .gap-4 "
        #     "> .text-xs.text-\\[\\#2b7fff\\]"
        # ).click()
       


      
        # # page.locator("div:nth-child(3) > .flex.flex-col.items-start > .data-inputs-scrollable > div:nth-child(6) > .flex.justify-between.items-center > .group > .flex.flex-row.justify-between.mt-2 > .flex.flex-row > .gap-4 > .text-xs.text-\\[\\#2b7fff\\]").click()
        # page.get_by_text("DATETIME").click()
        # page.get_by_text(r"YYYY-MM-DD HH:mm").click()
        # page.get_by_text("YYYY-MM-DD HH:mm:ss").click()
        # page.get_by_role("button", name="SAVE", exact=True).click()

        page.get_by_role("button", name="SAVE & CONTINUE").click()
        page.wait_for_timeout(2000)


        
        
        print("✅ Step 4 – Column types configured")

        # ── Step 5: Field Mapping ─────────────────────────────────────────────
        # page.locator("div").filter(has_text=re.compile(r"^PO FINAL ID0e7196f3-06f7-45d3-8dfb-4ed25c880dd9TEXT$")).nth(1).click()
        # page.get_by_text("PO STATUSNOTSUCCESSFULTEXT").first.click()
        page.locator("div").filter(has_text=re.compile(r"^PO FINAL ID0e7196f3-06f7-45d3-8dfb-4ed25c880dd9TEXT$")).nth(1).click(timeout=15000)
        page.locator("div").filter(has_text=re.compile(r"^PO FINAL ID0e7196f3-06f7-45d3-8dfb-4ed25c880dd9TEXT$")).nth(3).click(timeout=15000)
        page.get_by_role("button", name="SAVE & CONTINUE").click()
        page.get_by_role("button", name="MARK AS COMPLETE & EXIT").click()
        print("✅ Step 5 – Mapping completed")
        page.wait_for_timeout(5000)

        # ── Step 6: Run Pipeline ──────────────────────────────────────────────
        page.get_by_text(PIPELINE_CODE).first.click()
        page.wait_for_timeout(2000)
        # page.get_by_role("button", name="Run").click()
        # page.wait_for_timeout(2000)
        print("🎉 Pipeline execution triggered successfully!")

        context.close()
        browser.close()
