# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:04:11 2024

@author: zhoushus
"""

from datetime import datetime

class DataProcessor:
    def __init__(self, products):
        self.products = products
        self.unique_entries = set()

    def process_data(self, raw_data, today):
        processed_data = []
        for product in self.products:
            found = False
            for data in raw_data:
                # Check if data matches the product and today's date
                if product["name"] in data[2] and today in data[-1] and product["check"](data):
                    product_name = product.get("alias", data[2])
                    entry = f"北京新发地市场, {product_name}, {data[4]}, {data[8]}"
                    if entry not in self.unique_entries:
                        self.unique_entries.add(entry)
                        processed_data.append((product_name, data[4], data[8]))
                        found = True
            if not found:
                processed_data.append((product["name"], "", ""))
        return processed_data

    def generate_html_table(self, processed_data, today):
        # Create an HTML table with the processed data
        html_table = f"""
        <html>
          <body>
            <h2>今日水果价格 ({today})</h2>
            <table border="1" cellpadding="5" cellspacing="0">
              <thead>
                <tr>
                  <th>市场</th>
                  <th>品名</th>
                  <th>平均价</th>
                  <th>单位</th>
                </tr>
              </thead>
              <tbody>
        """
        for product_name, avg_price, unit in processed_data:
            html_table += f"<tr><td>北京新发地市场</td><td>{product_name}</td><td>{avg_price}</td><td>{unit}</td></tr>"
        html_table += """
              </tbody>
            </table>
          </body>
        </html>
        """
        return html_table
