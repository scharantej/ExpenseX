
# Flask imports
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Database to store expenses
expenses = []

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Add expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense = request.form.get('expense')
    amount = request.form.get('amount')
    expenses.append({'expense': expense, 'amount': amount})
    return redirect(url_for('expenses'))

# List expenses
@app.route('/expenses')
def expenses():
    return render_template('expenses.html', expenses=expenses)

# Edit expense
@app.route('/edit_expense/<int:index>', methods=['GET', 'POST'])
def edit_expense(index):
    if request.method == 'POST':
        expense = request.form.get('expense')
        amount = request.form.get('amount')
        expenses[index]['expense'] = expense
        expenses[index]['amount'] = amount
        return redirect(url_for('expenses'))
    else:
        expense = expenses[index]['expense']
        amount = expenses[index]['amount']
        return render_template('edit_expense.html', expense=expense, amount=amount, index=index)

# Delete expense
@app.route('/delete_expense/<int:index>')
def delete_expense(index):
    expenses.pop(index)
    return redirect(url_for('expenses'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
