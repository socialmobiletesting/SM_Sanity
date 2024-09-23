import csv
import logging
from tests.mambo_airplane_mode import Mambo_airplane_mode

# Configure logging
logging.basicConfig(filename='logs/framework_log.log', level=logging.INFO)
# logging.basicConfig(filename='logs/framework_log.csv', level=logging.INFO)


# Function to read and execute test cases
def execute_test_cases(csv_file):
    with open(csv_file, 'r') as file:
        print("opened csv file")    # debugging
        reader = csv.DictReader(file)
        print("reader var", reader)  # debugging
        for row in reader:
            print("entered into for loop")  # debugging
            test_case_id = row['test_case_id']
            description = row['description']
            test_type = row['test_type']
            test_script = row['test_script']
            print("test_script", test_script)   # debugging
            iteration = int(row['iteration'])

            logging.info(f"Starting Test Case {test_case_id}: {description}")

            try:
                if test_script == "mambo_airplane_mode":
                    Mambo_airplane_mode()

                logging.info(f"Test Case {test_case_id} Passed")
            except Exception as e:
                logging.error(f"Test Case {test_case_id} Failed: {e}")

# Start test execution
if __name__ == "__main__":
    execute_test_cases('testcases.csv')
