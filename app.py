from flask import Flask
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    products = ["T-Shirt", "Dress", "Bag", "Shoes"]
    sales = [120, 90, 60, 150]

    plt.figure()
    plt.bar(products, sales)
    plt.title("Sales Overview")

    if not os.path.exists("static"):
        os.makedirs("static")

    plt.savefig("static/chart.png")
    plt.close()

    return f"""
    <html>
    <body>
        <h1>Sales Dashboard</h1>
        <img src="/static/chart.png">
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)