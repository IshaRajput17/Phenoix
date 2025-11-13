# skincare_products_mongo.py

from pymongo import MongoClient

# ---- STEP 1: MongoDB Atlas Connection ----
# Replace <username>, <password>, and <cluster-url> with your own Atlas credentials
uri = "mongodb+srv://<username>:<password>@<cluster-url>/skincareDB?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["skincareDB"]
collection = db["products"]

# ---- STEP 2: Sample Skincare Product Data ----
products = [
    {
        "product_name": "Hydrating Facial Cleanser",
        "category": "Cleanser",
        "skin_type": ["Dry", "Normal"],
        "ingredients": ["Hyaluronic Acid", "Ceramides"],
        "uses": "Removes dirt and makeup while keeping skin hydrated.",
        "price": 499
    },
    {
        "product_name": "Vitamin C Serum",
        "category": "Serum",
        "skin_type": ["All"],
        "ingredients": ["Vitamin C", "Ferulic Acid", "Hyaluronic Acid"],
        "uses": "Brightens skin tone and reduces dark spots.",
        "price": 899
    },
    {
        "product_name": "Oil-Free Moisturizer",
        "category": "Moisturizer",
        "skin_type": ["Oily", "Combination"],
        "ingredients": ["Niacinamide", "Glycerin"],
        "uses": "Provides lightweight hydration without clogging pores.",
        "price": 699
    },
    {
        "product_name": "Sunscreen SPF 50",
        "category": "Sunscreen",
        "skin_type": ["All"],
        "ingredients": ["Zinc Oxide", "Titanium Dioxide"],
        "uses": "Protects against harmful UV rays and prevents tanning.",
        "price": 549
    }
]

# ---- STEP 3: Insert Data ----
if collection.count_documents({}) == 0:
    result = collection.insert_many(products)
    print(f"Inserted {len(result.inserted_ids)} products successfully!")
else:
    print("Products already exist in the database.")

# ---- STEP 4: Fetch and Display Data ----
print("\n--- Skincare Products in Database ---")
for product in collection.find():
    print(f"{product['product_name']} - {product['category']} - ₹{product['price']}")
    print(f"Uses: {product['uses']}\n")

# ---- Optional: Close Connection ----
client.close()
