import streamlit as st
import pandas as pd

# -------------------- MENU DATA --------------------
menu_data = {
    'Dish Name': [
        'Paneer Butter Masala', 'Dal Makhani', 'Veg Biryani',
        'Aloo Gobi', 'Tandoori Roti', 'Gulab Jamun', 
        'Paneer Tikka', 'Chole Bhature', 'Veg Pulao', 'Mix Veg Curry'
    ],
    'Price (₹)': [250, 180, 220, 160, 25, 90, 240, 200, 190, 210],
    'Offer': ['10% off', 'No offer', '5% off', 'No offer', 
              'No offer', 'Buy 1 Get 1', '10% off', 'No offer', 
              '5% off', 'No offer']
}

menu_df = pd.DataFrame(menu_data)

# -------------------- APP TITLE --------------------
st.title("🥗 Taj Hotel Veg Billing Dashboard")
st.markdown("Welcome to the **Taj Hotel**! Select your dishes and generate your bill below.")

# -------------------- SHOW MENU --------------------
st.subheader("Today's Veg Menu")
st.dataframe(menu_df)

# -------------------- ORDER SELECTION --------------------
st.subheader("Select Your Dishes")
selected_dishes = {}
for dish in menu_df['Dish Name']:
    qty = st.number_input(f"Enter quantity for {dish}", min_value=0, max_value=10, step=1)
    if qty > 0:
        selected_dishes[dish] = qty

# -------------------- BILL CALCULATION --------------------
if selected_dishes:
    bill_items = []
    total_price = 0
    total_discounted = 0

    for dish, qty in selected_dishes.items():
        price = menu_df.loc[menu_df['Dish Name'] == dish, 'Price (₹)'].values[0]
        offer = menu_df.loc[menu_df['Dish Name'] == dish, 'Offer'].values[0]
        
        original_cost = price * qty
        discount = 0

        if '10%' in offer:
            discount = 0.10 * original_cost
        elif '5%' in offer:
            discount = 0.05 * original_cost
        elif 'Buy 1 Get 1' in offer and qty >= 2:
            discount = price  # 1 item free per pair

        discounted_cost = original_cost - discount

        bill_items.append([dish, qty, price, offer, original_cost, discounted_cost])
        total_price += original_cost
        total_discounted += discounted_cost

    bill_df = pd.DataFrame(bill_items, columns=[
        'Dish Name', 'Quantity', 'Price (₹)', 'Offer', 
        'Original Total (₹)', 'Discounted Total (₹)'
    ])

    st.subheader("🧾 Your Bill Summary")
    st.dataframe(bill_df)

    st.write(f"**Original Total:** ₹{total_price:.2f}")
    st.write(f"**Total After Discounts:** ₹{total_discounted:.2f}")

    # -------------------- CSV DOWNLOAD --------------------
    csv = bill_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Bill as CSV",
        data=csv,
        file_name="Taj_Hotel_Bill.csv",
        mime="text/csv"
    )

else:
    st.info("Please select at least one dish to generate your bill.")
