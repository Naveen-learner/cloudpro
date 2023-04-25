# Import necessary libraries
from flask import Flask, render_template, request
from azure.cosmos import CosmosClient, PartitionKey

# Set up the Flask app
app = Flask(__name__)

# Initialize the Azure Cosmos DB client
endpoint = 'your_cosmos_db_endpoint'
key = 'your_cosmos_db_key'
client = CosmosClient(endpoint, key)
database_name = 'your_database_name'
database = client.get_database_client(database_name)
container_name = 'your_container_name'
container = database.get_container_client(container_name)

# Define the form route and method
@app.route('/form', methods=['GET', 'POST'])
def form():
    # If the request method is POST, store the form data in Azure Cosmos DB
    if request.method == 'POST':
        form_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        container.create_item(body=form_data)
        return render_template('success.html')
    # If the request method is GET, display the form
    else:
        return render_template('form.html')

# Define the success route
@app.route('/success')
def success():
    return render_template('success.html')

# Run the app
if __name__ == '__main__':
    app.run()