from azure.cosmos import CosmosClient, PartitionKey, exceptions
import uuid

# Configuration
ENDPOINT = "https://pvn-cosmos.documents.azure.com:443/"
KEY = "v9yLunEyWENmelHuYeoyAvvUHbfRsahMwmbQbxmgsjJoFXIFK9FFbpo01SEtVJr2hhEIYJelKX7yACDbrk9uPg=="
DATABASE_NAME = "Retaildb"
CONTAINER_NAME = "Products"

# Initialize client
client = CosmosClient(ENDPOINT, KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Create item
product = {
    "id": str(uuid.uuid4()),  # Unique ID
    "category": "Electronics",
    "name": "Laptop",
    "price": 999.99,
    "inStock": True
}
try:
    container.create_item(product)
    print(f"Created product: {product['name']}")
except exceptions.CosmosResourceExistsError:
    print("Product already exists")

# Read item
read_item = container.read_item(item=product["id"], partition_key=product["category"])
print(f"Read product: {read_item['name']}, Price: {read_item['price']}")

# Update item
read_item["price"] = 1099.99
container.replace_item(item=read_item["id"], body=read_item)
updated_item = container.read_item(item=read_item["id"], partition_key=read_item["category"])
print(f"Updated product price: {updated_item['price']}")

# Query items
query = "SELECT * FROM c WHERE c.category = @category"
params = [{"name": "@category", "value": "Electronics"}]
results = list(container.query_items(query=query, parameters=params, enable_cross_partition_query=True))
for item in results:
    print(f"Queried: {item['name']}, Price: {item['price']}")

# Delete item
container.delete_item(item=product["id"], partition_key=product["category"])
print(f"Deleted product ID: {product['id']}")