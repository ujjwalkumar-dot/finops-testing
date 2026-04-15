import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://dev.finance-ops.ai/en/sign-in"
EMAIL = "chirag.bhatia@paymentoptions.com"
PASSWORD = "tmj3sPFwwRc5Kjx@"

LEFT_FILES = [
    r"C:\Users\ghans\Downloads\MCB\MCB\02-09.xlsx"
]

RIGHT_FILES = [
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_08_02.828+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_08_34.177+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_09_21.973+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_09_45.892+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_10_05.500+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_10_32.145+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_10_59.623+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_11_31.439+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_11_52.894+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_12_27.619+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_13_19.150+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_13_46.283+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_14_06.082+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_14_26.468+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_18_53.486+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_19_25.559+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_19_59.490+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_20_01.134+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_20_27.914+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_20_37.794+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_21_02.679+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_21_18.911+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_21_33.362+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_21_58.209+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_22_02.673+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_22_38.541+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_23_05.620+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_23_09.823+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_23_31.824+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_23_59.807+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_24_09.628+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_24_42.192+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_25_20.059+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_26_05.050+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_26_06.360+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_26_37.988+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_26_42.033+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_27_02.592+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_27_36.095+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_28_09.613+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_28_50.188+04_00.csv",
    r"C:\Users\ghans\Downloads\MCB\MCB\2024-09-03\search2024-09-03T09_29_22.783+04_00.csv",
]

def test_full_reconciliation_flow(pytestconfig):
    PIPELINE_NAME = pytestconfig.getoption("--pipeline_name")
    PIPELINE_CODE = pytestconfig.getoption("--pipeline_code")

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

        page.get_by_role("link", name="Pipelines").click()
        page.get_by_role("button", name="plus   Create Pipeline").click()

        page.get_by_role("textbox", name="Enter Pipeline Name").fill(PIPELINE_NAME)
        page.get_by_role("textbox", name="Enter Pipeline Code").fill(PIPELINE_CODE)
        page.get_by_role("textbox", name="Enter Data Label Singular").fill("data")

        page.get_by_role("textbox", name="Enter Data Label Plural").click()
        page.locator(".flex.flex-col.h-\\[calc\\(100vh-90px\\)\\]").click()

        page.get_by_role("button", name="SAVE & CONTINUE").click()
        print(f"✅ Step 2 – Pipeline created: {PIPELINE_NAME}")

        page.get_by_role("textbox", name="* LEFT SIDE question-circle").fill("PO")
        page.get_by_role("textbox", name="* RIGHT SIDE question-circle").fill("WP")

        page.get_by_text("Computer").first.click()
        page.locator("#sourceL_list_0").get_by_text("Computer").click()

        page.get_by_text("Computer").nth(2).click()
        page.locator("#sourceR_list_0").get_by_text("Computer").click()

        page.locator("#fileType1").click()
        page.get_by_text("XLSX").click()

        page.locator("#fileType2").click()
        page.locator("#fileType2_list_11").get_by_text("CSV").click()

        for file in LEFT_FILES:
            with page.expect_file_chooser() as fc_left:
                page.get_by_role("button", name="inbox Maximum file size 50 MB").first.click()
            fc_left.value.set_files(file)
            page.wait_for_timeout(2000)
            print(f"✅ Left file uploaded: {file}")

        for file in RIGHT_FILES:
            with page.expect_file_chooser() as fc_right:
                page.get_by_role("button", name="inbox Maximum file size 50 MB").nth(1).click()
                fc_right.value.set_files(file)
                with page.expect_response(lambda res: "initiate" in res.url and res.status == 201):
                    fc_right.value.set_files(RIGHT_FILES)
            print(f"✅ Right file uploaded: {file}")

        with page.expect_response(lambda response: "v2" in response.url and response.status == 200):

            
           # Click normally (no API wait)
            page.get_by_role("button", name="Save & Continue").click()

            print("✅ Step 3 – Save & Continue clicked")

            # Wait for validation to finish (LONG process)
            page.wait_for_selector("text=Validation in progress", state="hidden", timeout=180000)

            # Wait for navigation
            page.wait_for_url("**step=2**", timeout=180000)

            file_name = os.path.basename(__file__).replace(".py", "")
            os.makedirs("test_failures", exist_ok=True)

            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            page.screenshot(path=f"test_failures/{file_name}_{timestamp}.png")