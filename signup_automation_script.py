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
    page.get_by_placeholder("Enter Your Email").fill("gotas85388@chuwel.com")
    page.get_by_placeholder("00-00000000").fill("9812702323")

    # page.get_by_label("Password", exact=True).fill("Kuber@123")
    # page.get_by_label("Confirm Password").fill("Kuber@123")

    page.locator('input[type="password"]').first.fill("Test@12345")
    page.locator('input[type="password"]').last.fill("Test@12345")

    page.get_by_role("button", name="Next").click()

    # OTP Verification
    otp = input("Enter the 6-digit OTP from your email: ").strip()
    page.locator("input").first.fill(otp)
    page.get_by_role("button", name="Verify Code").click()

    #next page(Agency Details)
    page.get_by_placeholder("Enter Agency Name").fill("Kuber Agency haha")
    page.get_by_placeholder("Enter Your Role in Agency").fill("Secret Agent")
    page.get_by_placeholder("Enter Your Agency Email Address").fill("kuberagency@gmail.com")
    page.get_by_placeholder("Enter Your Agency Website").fill("kuberagency.com")
    page.get_by_placeholder("Enter Your Agency Address").fill("Shankhamul, Lalitpur")

    page.get_by_text("Select Your Region of Operation").click()
    page.get_by_text("Nepal").click()
    page.get_by_role("button", name="Next").click()

    #next page (professional experience)
    page.get_by_text("Select Your Experience Level").click()
    page.locator('[role="option"]').first.click()

    page.get_by_placeholder("Enter an approximate number.").fill("200")
    page.get_by_placeholder("E.g., Undergraduate admissions to Canada.").fill("Undergraduate admissions to Canada.")
    page.get_by_placeholder("E.g., 90%").fill("90")

    page.get_by_text("Career Counseling").click()
    page.get_by_text("Admission Applications").click()
    page.get_by_text("Visa Processing").click()

    page.get_by_role("button", name="Next").click()


    #final page(Verification and preferences )
    # Step 4: Verification and Preferences
    page.get_by_placeholder("Enter your registration number").fill("123")

    page.get_by_text("Select Your Preferred Countries").click()
    page.get_by_text("Eleven").click()
    # page.keyboard.press("Escape")

    page.get_by_text("Colleges").click()

    page.get_by_placeholder("E.g., ICEF Certified Education Agent").fill("ICEF Certified Education Agent")

    page.locator('input[type="file"]').first.set_input_files("doc.docx")
    page.get_by_role("button", name="Submit").click()
    
   
    page.wait_for_timeout(20000)  # wait 10 seconds so that the page is loaded completely
    browser.close()
