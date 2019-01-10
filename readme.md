**Install packages**

`pip install -r requirements.txt`

**Run this command to generate Allure report**

`behave -f allure_behave.formatter:AllureFormatter -o allure-results /features/*.feature`

**Run this command to view Allure report**

`allure serve report`