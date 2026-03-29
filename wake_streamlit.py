import os
import time
from playwright.sync_api import sync_playwright

def wake_streamlit_app(url):
    print(f"🔄 Visiting: {url}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Go to the app
        response = page.goto(url, wait_until="networkidle", timeout=60000)
        
        print(f"Page loaded with status: {response.status if response else 'Unknown'}")
        
        # Wait a bit for the sleep screen to appear if it's sleeping
        time.sleep(8)
        
        # Check if the wake-up button exists and click it
        try:
            wake_button = page.get_by_role("button", name="Yes, get this app back up!")
            if wake_button.is_visible():
                print("⏰ App is sleeping → Clicking wake-up button...")
                wake_button.click()
                time.sleep(10)  # Wait for the app to start
                print("✅ App should now be awake!")
            else:
                print("✅ App is already awake or button not found.")
        except Exception as e:
            print(f"Note: Could not find wake button (app probably already awake). Error: {e}")
        
        # Take a screenshot for debugging (optional but useful)
        page.screenshot(path="streamlit_status.png")
        
        browser.close()

if __name__ == "__main__":
    url = os.getenv("STREAMLIT_URL")
    if not url:
        raise ValueError("STREAMLIT_URL environment variable is not set!")
    
    wake_streamlit_app(url)
