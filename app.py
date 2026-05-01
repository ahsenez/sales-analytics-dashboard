from flask import Flask
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    products = ["T-Shirt", "Dress", "Bag", "Shoes"]
    sales = [120, 90, 60, 150]
    total = sum(sales)

    plt.figure()
    plt.bar(products, sales)
    plt.title("Sales Overview")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/chart.png")
    plt.close()

    return f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial;
            background: #1e1e2f;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        h1 {{
            color: #00c3ff;
        }}
        img {{
            margin-top: 20px;
            border-radius: 10px;
            background: white;
            padding: 10px;
        }}
    </style>
</head>
<body>
    <h1>🚀 Sales Dashboard</h1>
    <h3>Product Performance Overview</h3>
    <h2>Total Sales: {total}</h2>
    <img src="/static/chart.png">
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
