import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from datetime import datetime

# Step 1: Load and prepare data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Step 2: Analyze data
def analyze_data(df):
    summary = df.groupby(df['Date'].dt.date)['Revenue'].sum()
    return summary

# Step 3: Plot revenue trend
def plot_trend(summary):
    plt.figure(figsize=(10, 5))
    summary.plot(kind='line', marker='o')
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue (₹)")
    plt.tight_layout()
    plot_file = "revenue_trend.png"
    plt.savefig(plot_file)
    plt.close()
    return plot_file

# Step 4: Generate PDF
def create_pdf(summary, plot_path, output_file="sales_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="📈 Sales Revenue Report", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=2, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for date, revenue in summary.items():
        pdf.cell(200, 10, txt=f"{date} — ₹{revenue:.2f}", ln=1)

    pdf.ln(10)
    pdf.image(plot_path, w=180)

    pdf.output(output_file)
    print(f"✅ PDF Report saved as {output_file}")

# Step 5: Run all steps
def main():
    try:
        df = load_data("sales_data.csv")
        summary = analyze_data(df)
        plot_path = plot_trend(summary)
        create_pdf(summary, plot_path)
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()

