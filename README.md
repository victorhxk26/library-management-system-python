# Python-based Library Management System
The library management system was developed to streamline the process for students and staff at Asia Pacific University (APU) so that they can easily access the system to add, update, remove and search for any particular book record as well as view the whole book list. Besides, this system can also help streamline the process of managing and organizing large volumes of books. Python is used as the foundation for this system as it is layman-friendly and easy to use to create any system.

There are several assumptions to be made when creating and examining the functionality of this system, as listed below: 
•	The first assumption will revolve around file accessibility as we assume that Python has permission to read and manipulate the CSV file, named “Library_Booklist.csv”, that stores every book record.
•	The second assumption is about the predetermined data format in the data frame and its corresponding CSV file, where there are five columns namely Book_ID, Book_Title, Author, Borrower_Name and Book_Return_Date, and each row in both sources corresponds to every book record. 
•	The third assumption is that users are required to input information according to the predetermined rule to avoid any form of validation and type errors. For example, users are restricted and required to input the Book_ID to validate the format of the ID number and its existence in the system before proceeding with the specific operation.
•	The fourth assumption is that users can only append, update, search and delete one specific book record at a time. 
