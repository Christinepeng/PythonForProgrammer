'''
The final project will be due on March 24th 2019 @ 11:59 PM. The project is for 30 points and you are expected to work on an original idea that is substantial. The final project must include a Python program or programs and must cover at least 6 Python elements from the following list.

1.  Use any data structure like list, dictionary, set or tuple
2.  List comprehension
3.  Dictionary comprehension
4.  Functions
5.  Classes
6.  User created iterators
7.  Importing external modules
8.  Error checks using try-except
9.  File input and output
10. Regular expression
11. Itertools
12. Decorators

You need to prepare a report in pdf format that will explain the work that you have done including any relevant screen-shot and Python program(s) that you have written. Each student has to work on their own individual project.
Students can work on a project of their choice or can work on the project listed in the section "Project suggestions" below.

If you have any questions, we can discuss it during the class.


Project report details


Please format the final project report according to the instruction below.  I am also enclosing the solution to mini project.


1. Introduction  - This section, you should describe the problem that you are solving, any background information that will help the instructors to understand the program


2. Requirements  - List all the Python modules that need to be installed. If some of these modules need a specific version, please indicate so. You can also list any other conditions that are needed to run the program.


3. Description of the Python program. You need to describe the programs that you wrote.


4. Screenshots of the program output  - If you are using a specific hardware and cannot obtain screenshot, please enclose appropriate photographs


5. Conclusion -  Describe in brief the problem you solved, the program you wrote and obtained output.


6. Python program  - If the program is one file, please add it as one of the pages in the report. If the code is large and spans more than one file, enclose a separate zip file.

Please make sure that the final report is in pdf format

Project suggestions
1) Go to this link http://www.car.org/marketdata/data/housingdata/ (Links to an external site.)Links to an external site. and download the Excel file in the link titled, ‘Median Prices of Existing Detached Homes.’ Based on the available data, predict the house price in various counties using linear regression. Learn more about linear regression athttps://en.wikipedia.org/wiki/Linear_regression (Links to an external site.)Links to an external site.. You can use Python module scikit learn to program linear regression. Plot house prices for two counties in separate graphs and also include the corresponding linear regression lines in the graphs. For plotting, you can use Python modules matplotlib or plotply. You might have to use Python modules like xlrd or xlwt to read and write excel files respectively.

2) Web scraping – you can choose to crawl specific websites. For example, you might want to find the stock price of a particular company over time. In such cases, you programmatically access Yahoo stock page at http://finance.yahoo.com/q/hp?s=YHOO (Links to an external site.)Links to an external site. and obtain the data using Python modules beautifulsoup and requests. Based on the data, predict the stock price using linear regression. Learn more about linear regression at https://en.wikipedia.org/wiki/Linear_regression (Links to an external site.)Links to an external site.. You can use Python module scikit learn to program linear regression. Plot stock prices and include the corresponding linear regression line in the graphs. For plotting, you can use Python modules matplotlib or plotply.

3) Imagine you are Linux administrator for a company. You are managing 10 machines. You want to write a Python program using modules like fabric or paramiko to find the usage of these machines. The information might include CPU load, memory used, available disk space, number of logged in users etc. The program must run hourly and should save the above information into a csv file, excel file or in a database. You might have to use modules like csv, xlwt, sqlite etc. If a query is made to find out load on a specific machine or the load on all the machines at a specific time, you should return the results.

4) Office visitor log- The project is on developing a desktop or web based application for visitor log. This project will require using WxPython for developing the desktop user interface or web2py or flask for web. You will also need to use a database such as Sqlite, MySQL.

Imagine an office where visitors have to register at the front desk.  The visitor will use the program to provide their name, email address, phone number and the person they are visiting. If any of the information is incorrect, you need to highlight the error and provide appropriate error message. For example, if the phone number have alphabets, you need to show it as an error. If all entries are valid, you need to store it in a database.

Additional requirements - an ability to view a list of visitors, an ability to filter the list based on from and to date, an ability to download this information as an excel file using XLWT module.
'''