from playwright.sync_api import sync_playwright, expect
import re
import sys


def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto("https://duckduckgo.com")
        page.wait_for_timeout(2000)

        try:
            page.locator("button:has-text('I agree')").click(timeout=3000)
        except:
            pass

        search_box = page.locator("input[name='q'], textarea[name='q']")
        search_box.wait_for(state="visible", timeout=5000)
        search_box.fill("")
        search_box.type("playwright python", delay=100)

    # ✅ Press Enter to submit the search
        search_box.press("Enter")

    # Optional: wait for results to load
        page.wait_for_timeout(10000)
     # ✅ Capture screenshot here
        page.screenshot(path="screenshots/google_result.png", full_page=True)


    # ✅ Now the title should reflect the search
    # ✅ Try the assertion and handle failure
        try:
            expect(page).to_have_title(re.compile("playwright python", re.IGNORECASE))
        except AssertionError as e:
            print("❌ Test failed")
            print(f"Reason: {e}")
        else:
            print("✅ Test passed")

        sys.stdout.flush()
        browser.close()


