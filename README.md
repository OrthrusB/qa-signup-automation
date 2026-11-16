# Authorized Partner Signup Automation

End-to-end automated UI test (https://authorized-partner.vercel.app/).

## Environment & Setup
-Language: Python 3.x
-Automation Framework: Playwright (`playwright.sync_api`)
-Browser / Driver:Chromium (headed mode via Playwright bundled Chromium driver)
-OS:Windows

## Prerequisites
a. Python 3.8 or higher 
b. A valid dummy document (`doc.docx`) in the root directory
c. Access to a temporary email inbox for otp verification

## Installation & Execution Steps

1. Clone the repository:
   
   git clone https://github.com/OrthrusB/qa-signup-automation.git
   cd Task For Vrit

2. Create and activate virtual environment:
    python -m venv .venv
    .venv\Scripts\activate

3. Install Playwright and Chromium browser:
    pip install playwright
    playwright install chromium

4. Update unique test credentials (before each run):
--Open signup_automation_script.py and update the email and phone number,so that the system does not reject the number(duplication error)

    page.get_by_placeholder("Enter Your Email").fill("<NEW_TEMP_EMAIL>")
    page.get_by_placeholder("00-00000000").fill("<NEW_10_DIGIT_PHONE>")

5. Run the Script:
    python signup_automation_script.py

6. OTP Verification:
When you are in the terminal (Enter the 6-digit OTP from your email:), enter the 6-digit verification code sent to your email (within the 60-second), its the validity and press Enter. The script will automatically run

# Test Data Used

Applicant Name: Kuber Rana

Email: gotas85388@chuwel.com (unique email everytime)

Mobile Number: 9812702323 (unique number every time)

Password: Test@12345

Agency Name: Kuber Agency haha

Role in Agency: Secret Agent

Agency Email / Website: kuberagency@gmail.com / kuberagency.com

Address / Region: Shankhamul, Lalitpur / Nepal

Experience / Students / Success Rate: 1 year / 200 / 90%

Services Provided: Career Counseling, Admission Applications, Visa Processing

Registration Number: 123

Preferred Country / Institution Type: Eleven / Colleges

Certification Details: ICEF Certified Education Agent

Uploaded Document: doc.docx

