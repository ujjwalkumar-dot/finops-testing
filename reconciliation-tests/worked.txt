import re
import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright, expect

# ── Static Config ─────────────────────────────────────────────────────────────
BASE_URL = "https://dev.finance-ops.ai/en/sign-in"
EMAIL = "chirag.bhatia@paymentoptions.com"
PASSWORD = "tmj3sPFwwRc5Kjx@"

LEFT_FILE  = r"C:\Users\ghans\Downloads\wp-11oct-31oct\28oct.xlsx"
RIGHT_FILE = r"C:\Users\ghans\Downloads\wp-11oct-31oct\2025-10-29\report.csv"


def screenshot(page, label=""):
    file_name = os.path.basename(__file__).replace(".py", "")
    os.makedirs("test_failures", exist_ok=True)
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    suffix = f"_{label}" if label else ""
    path = f"test_failures/{file_name}{suffix}_{timestamp}.png"
    page.screenshot(path=path)
    print(f"📸 Screenshot saved: {path}")


def test_full_reconciliation_flow(pytestconfig):

    PIPELINE_NAME = pytestconfig.getoption("--pipeline_name")
    PIPELINE_CODE = pytestconfig.getoption("--pipeline_code")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ── Step 1: Login ─────────────────────────────────────────────────────
        page.goto(BASE_URL)

        # Wait for login form to be ready
        email_input = page.get_by_role("textbox", name="johndoe@test.com")
        expect(email_input).to_be_visible()

        email_input.fill(EMAIL)
        page.get_by_role("textbox", name="* Password question-circle").fill(PASSWORD)
        page.get_by_role("button", name="Sign In").click()

        # Wait until redirected away from sign-in
        page.wait_for_url("**/en/**", wait_until="domcontentloaded")
        print(f"✅ Step 1 – Logged in as {EMAIL}")

        # ── Step 2: Create Pipeline ───────────────────────────────────────────
        pipelines_link = page.get_by_role("link", name="Pipelines")
        expect(pipelines_link).to_be_visible()
        pipelines_link.click()

        create_btn = page.get_by_role("button", name="plus   Create Pipeline")
        expect(create_btn).to_be_visible()
        create_btn.click()

        # Wait for the modal / form to appear
        pipeline_name_input = page.get_by_role("textbox", name="Enter Pipeline Name")
        expect(pipeline_name_input).to_be_visible()

        pipeline_name_input.fill(PIPELINE_NAME)
        page.get_by_role("textbox", name="Enter Pipeline Code").fill(PIPELINE_CODE)
        page.get_by_role("textbox", name="Enter Data Label Singular").fill("data")

        # Trigger plural field auto-fill then dismiss focus
        plural_input = page.get_by_role("textbox", name="Enter Data Label Plural")
        expect(plural_input).to_be_visible()
        plural_input.click()
        page.locator(".flex.flex-col.h-\\[calc\\(100vh-90px\\)\\]").click()

        save_continue = page.get_by_role("button", name="SAVE & CONTINUE")
        expect(save_continue).to_be_enabled()
        save_continue.click()
        print(f"✅ Step 2 – Pipeline created: {PIPELINE_NAME}")

        # ── Step 3: Configure Sides & Upload Files ────────────────────────────

        # Wait for sides configuration form
        left_side_input = page.get_by_role("textbox", name="* LEFT SIDE question-circle")
        expect(left_side_input).to_be_visible()
        left_side_input.fill("PO")

        right_side_input = page.get_by_role("textbox", name="* RIGHT SIDE question-circle")
        expect(right_side_input).to_be_visible()
        right_side_input.fill("WP")

        # Left Source → Computer
        left_computer = page.get_by_text("Computer").first
        expect(left_computer).to_be_visible()
        left_computer.click()
        page.locator("#sourceL_list_0").get_by_text("Computer").click()

        # Right Source → Computer
        right_computer = page.get_by_text("Computer").nth(2)
        expect(right_computer).to_be_visible()
        right_computer.click()
        page.locator("#sourceR_list_0").get_by_text("Computer").click()

        # File Type Left → XLSX
        left_type = page.locator("#fileType1")
        expect(left_type).to_be_visible()
        left_type.click()
        xlsx_option = page.get_by_text("XLSX")
        expect(xlsx_option).to_be_visible()
        xlsx_option.click()

        # File Type Right → CSV
        right_type = page.locator("#fileType2")
        expect(right_type).to_be_visible()
        right_type.click()
        csv_option = page.locator("#fileType2_list_11").get_by_text("CSV")
        expect(csv_option).to_be_visible()
        csv_option.click()

        # Upload LEFT file — wait for upload button to be ready
        left_upload_btn = page.get_by_role("button", name="inbox Maximum file size 50 MB").first
        expect(left_upload_btn).to_be_visible()
        with page.expect_file_chooser() as fc_left:
            left_upload_btn.click()
        fc_left.value.set_files(LEFT_FILE)

        # Wait until left file name appears somewhere in the DOM (upload complete)
        left_filename = os.path.basename(LEFT_FILE)
        expect(page.get_by_text(left_filename)).to_be_visible()
        print(f"✅ Step 3a – Left file uploaded: {LEFT_FILE}")

        # Upload RIGHT file
        right_upload_btn = page.get_by_role("button", name="inbox Maximum file size 50 MB").nth(1)
        expect(right_upload_btn).to_be_visible()
        with page.expect_file_chooser() as fc_right:
            right_upload_btn.click()
        fc_right.value.set_files(RIGHT_FILE)

        # Wait until right file name appears in DOM
        right_filename = os.path.basename(RIGHT_FILE)
        expect(page.get_by_text(right_filename)).to_be_visible()
        print(f"✅ Step 3b – Right file uploaded: {RIGHT_FILE}")

        # Save & Continue — wait until it's enabled (both files registered)
        save_continue_2 = page.get_by_role("button", name="Save & Continue")
        expect(save_continue_2).to_be_enabled()
        save_continue_2.click()
        print("✅ Step 3 – Save & Continue clicked")

        screenshot(page, label="after_step3")

        # ── Step 4: Wait for next section to load ─────────────────────────────
      