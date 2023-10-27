Project Report: 
Name: Inventory Management System for Retail Store

List of the implemented functionalities:
1. Product class:
   - A 'Product' class is created to represent individual products.
   - Each product has attributes: a unique product identifier, name, category, price, and quantity in stock.
   
2. Inventory class:
  - A 'Inventory' class is implemented to manage the store's inventory.
  - It provides methods for adding products to the inventory, updating stock levels, and retrieving product information
   
3. Sales and Transactions
   - This records sales transactions through a 'Transcation' class.
   - Each transaction includes the products sold, amount, and the total transaction amount.
     
4. Stock management
   - Methods are provides for updating stock levels when products are purchased or restocked.
   - The system ensures tracking of stock levels.
     
5. Reports:
   - A 'ReportGenerator' class is used to generate various types of reports like stock reports and sales reports.
   - The system can display the current stock levels and sales history.
      
6.  Command-Line Interface (CLI):
   - This allows users to interact with the system by selecting options
   - Users can add products, make sales, generate stock and sales reports, and exit the program.
     
The test result for each functionality with figure and explaination: 
1. Product Class:
Test Scenario: Adding a new product to the inventory.
Expected Result: After executing this test, you should see the product added to the inventory with a unique product identifier. The figure should show the new product and its attributes.



3. Inventory Class:
Test Scenario: Adding products to the inventory and updating stock levels.

Expected Result: Products should have been successfully added to the inventory, and when stock levels are updated, the quantity of the product in stock changes as expected. The figure should display the updated inventory.

3.Sales and Transactions:
Test Scenario: Recording a sales transaction, including multiple products.

Expected Result: After recording the sales transaction, you should see the total amount accurately calculated based on the products and quantities sold. The figure should display the transaction details, including the products sold and the total amount.

4.Stock Management:
Test Scenario: Attempting to update stock levels for a product that exists and one that doesn't exist in the inventory.

Expected Result: When updating stock levels for an existing product, the figure should reflect the updated quantity. For a non-existent product, an error message should be displayed, and the figure should show the error message.

5. Reports:
Test Scenario: Generating stock and sales reports.

Expected Result: The stock report should display the current stock levels of all products in the inventory, including their product ID, name, and quantity. The sales report should provide a summary of each recorded transaction, showing the total amount for each transaction. The figure should display these reports.

6.Command-Line Interface (CLI):
Test Scenario: Interacting with the IMS through the command-line interface by selecting various options (e.g., adding a product, making a sale, generating reports).
Expected Result: Users should be able to interact with the system as intended. Each option chosen should trigger the corresponding functionality, and users should be able to exit the program when they are done. The figure should illustrate the CLI interface and the selected options.

Discussion on the project result
The project's goal was to develop an IMS for a retail establishment that would make it possible for report generating, stock management, sales recording, and product management. These goals have mostly been achieved by the implemented functionality.
The Product class allows the creation of products with essential attributes like name, category, price, and quantity. Testing confirmed that new products are added successfully and product details are accurately stored. The Inventory class is effective in managing product inventory. Products can be added, and stock levels can be updated. This functionality meets the requirement of managing product inventory. Sales transactions can be recorded through the Transaction class, accurately calculating total amounts and reducing stock levels as expected. This ensures that sales are correctly reflected in the inventory. Stock levels can be updated for existing products, maintaining accuracy in tracking inventory. An appropriate error message is displayed when attempting to update non-existent products. The ReportGenerator class can successfully generate stock and sales reports. The stock report displays product details and quantities, while the sales report summarizes transaction history. The CLI provides a user-friendly means of interacting with the IMS. Users can add products, record sales, generate reports, and exit the program with ease. The system demonstrates accuracy and reliability in managing products, sales, and stock levels. It consistently updates data correctly and provides meaningful feedback to users. The CLI interface offers a simple and intuitive way for users to perform tasks.
