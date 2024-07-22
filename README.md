## Flask Application for Monthly Budget Tracking

### HTML Files

- `index.html`: This HTML file serves as the homepage of the application. It displays an input form for users to enter their budget and list their expenses.
- `expenses.html`: This HTML file lists all the expenses entered by the user. It includes buttons for editing and deleting expenses.

### Routes

- `/`: This route handles the home page. It renders the `index.html` file.
- `/add_expense`: This route handles adding a new expense. It checks if the expense is valid and adds it to the database if so.
- `/edit_expense`: This route handles editing an existing expense. It fetches the expense from the database, displays it in a form, and updates the database with any changes made.
- `/delete_expense`: This route handles deleting an expense. It removes the expense from the database.
- `/expenses`: This route displays the expenses in the database. It renders the `expenses.html` file.