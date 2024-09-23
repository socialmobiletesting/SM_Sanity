1. Folder Structure

bash
Copy code
├── framework
│   ├── tests               # Folder for Android and Web test scripts
│   │   ├── mambo_airplane_mode.py  # The main test case script
│   ├── drivers             # Folder for Appium and Selenium driver files
│   │   ├── appium_driver.py     # Appium driver operations
│   │   ├── selenium_driver.py   # Selenium driver operations
│   ├── logs                # Logs folder for screenshots, logcat, and test logs
│   ├── reports             # HTML reports folder
│   ├── testcases.csv       # CSV file to define test case order
│   └── execute_tests.py    # Main controller script to execute test cases


2. CSV File Structure (testcases.csv)
We will define test cases and link them to the relevant scripts and execution iterations in the CSV file.


3. Test Case Script (tests/mambo_airplane_mode.py)
The main test case Mambo_airplane_mode will be placed here.


4. Drivers Folder
Appium Driver (drivers/appium_driver.py)
Move the appium-related functions into this file and make it reusable.

Selenium Driver (drivers/selenium_driver.py)
Move the selenium-related functions into this file.


5. Main Controller (execute_tests.py)
This script will read from the CSV and execute the correct test script.


6. Logging and Reporting
All logs will be stored in the logs directory.
You can later integrate a reporting tool like pytest-html for better test results visualization in the reports folder.