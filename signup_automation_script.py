from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser= p.chromium.launch(headless=False)      
    page=browser.new_page()
    page.goto("https://authorized-partner.vercel.app/")
    #page.get_by_text("Get Started").click()
    page.get_by_role("link", name="Get Started").click()
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Continue").click()

    #place holder for the next step of the signup process
    ##setup account
    page.get_by_placeholder("Enter Your First Name").fill("Kuber")
    page.get_by_placeholder("Enter Your Last Name").fill("Rana")
    page.get_by_placeholder("Enter Your Email").fill("babin.rana2060@gmail.com")
    page.get_by_placeholder("00-00000000").fill("9812700000")

    # page.get_by_label("Password", exact=True).fill("Kuber@123")
    # page.get_by_label("Confirm Password").fill("Kuber@123")

    page.locator('input[type="password"]').first.fill("Test@12345")
    page.locator('input[type="password"]').last.fill("Test@12345")

    page.get_by_role("button", name="Next").click()

    # OTP Verification
    otp = input("Enter the 6-digit OTP from your email: ").strip()
    page.locator("input").first.fill(otp)
    page.get_by_role("button", name="Verify Code").click()
   

    page.wait_for_timeout(20000)  # wait 10 seconds so that the page is loaded completely

    browser.close()
