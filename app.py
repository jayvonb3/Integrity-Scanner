import streamlit as st
import requests

FORBIDDEN_INGREDIENTS = [
    "natural flavors", "soy lecithin", "carrageenan", "bha", "bht", 
    "high-fructose corn syrup", "red 40", "yellow 5", "partially hydrogenated", 
    "fortified", "enriched", "canola oil", "soybean oil", "sunflower oil"
]

st.title("Elite Nutrition Integrity Scanner")
barcode = st.text_input("Enter Product Barcode:")

if barcode:
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url).json()
    
    if response.get('status') == 1:
        product = response['product']
        ingredients = product.get('ingredients_text', '').lower()
        st.write(f"### Product: {product.get('product_name', 'Unknown')}")
        
        found_violations = [item for item in FORBIDDEN_INGREDIENTS if item in ingredients]
        
        if found_violations:
            st.error(f"REJECTED: Contains forbidden items: {', '.join(found_violations)}")
        else:
            st.success("APPROVED: Meets Integrity Standards")
    else:
        st.warning("Product not found in database.")
