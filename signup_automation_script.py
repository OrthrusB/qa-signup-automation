from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser= p.chromium.launch(headless=False)      
    page=browser.new_page()
    page.goto("https://authorized-partner.vercel.app/")
    page.wait_for_timeout(10000)  # wait 10 seconds so that the page is loaded completely
    browser.close()
