import os
import time
from playwright.sync_api import sync_playwright

url = os.getenv("STREAMLIT_URL")
if not url:
    print("❌ STREAMLIT_URL secret is missing!")
    exit(1)

print(f"🔄 Visiting: {url}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto(url, wait_until="networkidle", timeout=60000)
    time.sleep(8)

    try:
        button = page.get_by_role("button", name="Yes, get this app back up!")
        if button.is_visible(timeout=5000):
            print("⏰ App is sleeping → Clicking wake-up button...")
            button.click()
            time.sleep(12)
            print("✅ Wake-up button clicked! App should now be awake.")
        else:
            print("✅ App appears to be already awake.")
    except Exception as e:
        print(f"Note: Could not find wake button (likely already awake). Error: {e}")

    browser.close()
    print("✅ Workflow completed successfully.")
