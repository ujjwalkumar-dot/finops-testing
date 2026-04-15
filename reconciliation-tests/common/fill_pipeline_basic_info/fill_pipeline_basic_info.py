DATA_LABEL_SINGULAR = "data"

def fill_pipeline_basic_info(page, pipeline_name, pipeline_code):
    # ── Step 2: Create Pipeline ───────────────────────────────────────────

    page.get_by_role("textbox", name="Enter Pipeline Name").fill(pipeline_name)
    page.get_by_role("textbox", name="Enter Pipeline Code").fill(pipeline_code)
    page.get_by_role("textbox", name="Enter Data Label Singular").fill(DATA_LABEL_SINGULAR)

    page.get_by_role("textbox", name="Enter Data Label Plural").click()
    page.locator(".flex.flex-col.h-\\[calc\\(100vh-90px\\)\\]").click()

    page.get_by_role("button", name="SAVE & CONTINUE").click()
    print(f"✅ Step 2 – Pipeline created: {pipeline_name}")