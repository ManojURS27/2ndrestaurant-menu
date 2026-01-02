import streamlit as st

menu_data = {
    "Starters": {"Gobi Manchurian": 130.0, "Mushroom Manchurian": 150.0, "Paneer Manchurian": 150.0, "Baby Corn Manchurian": 140.0},
    "Soups": {"Hot and Sour": 200.0, "Manchow Soup": 150.0, "Garlic Soup": 180.0, "Tomato Soup": 150.0},
    "Main Course": {"Veg biryani": 120.0, "Paneer biryani": 140.0, "Mushroom biryani": 140.0, "Ghee Rice": 100.0, "Jeera Rice": 100.0, "White Rice": 80.0, "Curd Rice": 100.0},
    "Juice/Shakes": {"Lemon Soda": 60.0, "Dry Fruit Shake": 120.0, "Banana Shake": 80.0, "Litchi Shake": 120.0, "Double Sundae": 100.0, "Gud Bud Ice Cream": 140.0}
}

if 'cart' not in st.session_state:
    st.session_state.cart = {}

st.set_page_config(page_title="Manu Restaurant", layout="wide")
st.title("🍴 Manu Restaurant Menu")

col1, col2 = st.columns([2, 1])

with col1:
    for category, items in menu_data.items():
        st.subheader(f"--- {category} ---")
        for name, price in items.items():
            c1, c2, c3 = st.columns([3, 1, 1])
            c1.write(name)
            c2.write(f"₹{price:.2f}")
            if c3.button("Add", key=name):
                if name in st.session_state.cart:
                    st.session_state.cart[name]['qty'] += 1
                else:
                    st.session_state.cart[name] = {'price': price, 'qty': 1}
                st.rerun()

with col2:
    st.header("🛒 Your Cart")
    if not st.session_state.cart:
        st.write("Your cart is empty.")
    else:
        total = 0
        for name, details in list(st.session_state.cart.items()):
            item_total = details['price'] * details['qty']
            total += item_total
            st.write(f"**{name}** x{details['qty']} - ₹{item_total:.2f}")
            if st.button("Remove", key=f"rem_{name}"):
                del st.session_state.cart[name]
                st.rerun()
        
        st.divider()
        st.subheader(f"Total: ₹{total:.2f}")
        
        if st.button("Clear Cart"):
            st.session_state.cart = {}

            st.rerun()
