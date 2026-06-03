import streamlit as st
import requests

FORBIDDEN_INGREDIENTS = [
    "natural flavors", "soy lecithin", "carrageenan", "bha", "bht", 
    "high-fructose corn syrup", "red 40", "yellow 5", "partially hydrogenated", 
    "fortified", "enriched", "canola oil", "soybean oil", "sunflower oil"
]

st.title("Integrity Scanner")

# Simple text input for barcode
barcode = st.text_input("Enter Barcode (Type or Paste):")

if barcode:
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url).json()
    
    if response.get('status') == 1:
        product = response['product']
        ingredients = product.get('ingredients_text', '').lower()
        st.write(f"### {product.get('product_name', 'Unknown')}")
        
        violations = [i for i in FORBIDDEN_INGREDIENTS if i in ingredients]
        
        if violations:
            st.error(f"REJECTED: Found {', '.join(violations)}")
        else:
            st.success("APPROVED: Clean Integrity")
    else:
        st.warning("Product not found.")
