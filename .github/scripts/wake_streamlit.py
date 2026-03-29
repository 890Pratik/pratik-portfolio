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
    
    # Increased timeout + less strict wait
    try:
        print("Loading page...")
        page.goto(url, wait_until="domcontentloaded", timeout=120000)  # 2 minutes
        time.sleep(10)   # Give extra time for the sleep screen to appear if needed
        
        try:
            button = page.get_by_role("button", name="Yes, get this app back up!")
            if button.is_visible(timeout=10000):
                print("⏰ App is sleeping → Clicking wake-up button...")
                button.click()
                time.sleep(15)   # Wait longer for app to start
                print("✅ Wake-up button clicked!")
            else:
                print("✅ App appears to be already awake.")
        except Exception as e:
            print(f"Note: Could not find wake button (likely already awake or slow). {e}")
            
    except Exception as e:
        print(f"⚠️ Page load timed out or failed: {e}")
        print("The app might be very slow to wake up. We'll try again next run.")
    
    browser.close()
    print("✅ Workflow finished.")
