import streamlit as st

st.set_page_config(layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js"></script>
</head>
<body>
    <div id="interactive" class="viewport"></div>
    <h2 id="result">Scanning...</h2>
    <script>
        Quagga.init({
            inputStream: { type: "LiveStream", target: document.querySelector('#interactive') },
            decoder: { readers: ["ean_reader"] }
        }, function(err) { Quagga.start(); });
        
        Quagga.onDetected(function(data) {
            document.getElementById('result').innerHTML = "Barcode: " + data.codeResult.code;
            // You can add a redirect here to your search logic
        });
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=500)
