from playwright.sync_api import sync_playwright

# ── Static Config ─────────────────────────────────────────────────────────────
BASE_URL = "https://dev.finance-ops.ai/en/sign-in"
EMAIL = "chirag.bhatia@paymentoptions.com"
PASSWORD = "tmj3sPFwwRc5Kjx@"



def login():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(BASE_URL)
    page.get_by_role("textbox", name="johndoe@test.com").fill(EMAIL)
    page.get_by_role("textbox", name="* Password question-circle").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/en/**")
    print(f"✅ Step 1 – Logged in as {EMAIL}")
    
    return page, browser, p
     