<h1 align="center">
  Browser History Analytics 2
</h1>
<p align="center">
  A Python package that analyzes and visualizes your browser history data with interactive charts and insights.
</p>

<br>

<table style="width:100%; border-collapse:collapse; font-family:sans-serif;">
  <th>
    Features Overview
  </th>
  <th>
    Preview
  <tr>
    <td style="vertical-align:top; padding:10px; width:60%;">
      <ul>
        <li><strong>Category Analysis</strong>: Automatically categorizes websites (Social Media, Development, Entertainment, etc.)</li>
        <li><strong>Time-based Insights</strong>: Hourly and daily browsing patterns with heatmaps</li>
        <li><strong>Summary Statistics</strong>: Key metrics about your browsing habits</li>
        <li><strong>Interactive Filters</strong>: Filter by date range and categories</li>
        <li><strong>Raw Data View</strong>: Search and export your browsing data</li>
        <li><strong>Multi-browser Support</strong>: Works with Chrome, Firefox, Safari, and more</li>
      </ul>
    </td>
    <td style="vertical-align:top; padding:10px; width:40%;">
      <img src="https://github.com/user-attachments/assets/b60be8bf-f6f3-4b1f-9d1e-311d40587b31" alt="Preview GIF" style="max-width:100%; border-radius:8px; box-shadow:0 0 8px rgba(0,0,0,0.1);">
    </td>
  </tr>
</table>



## Installation

### Option 1: Install from source

```bash
git clone https://github.com/arpy8/browser-history-analytics-2.git
cd browser-history-analytics-2
pip install -e .
```

### Option 2: Install directly

```bash
pip install https://github.com/arpy8/browser-history-analytics-2/archive/main.zip
```

## Usage
Command prompt: 
```
pip install https://github.com/arpy8/browser-history-analytics-2/archive/main.zip && bha
```
Powershell: 
```
pip install https://github.com/arpy8/browser-history-analytics-2/archive/main.zip ; bha
```

This will launch the web application in your default browser.

## What You'll See

### Dashboard Tabs

1. **Home**: Main dashboard with visualizations and summary statistics
2. **Raw Data**: Searchable table with export functionality
3. **Additional Info**: Detailed insights and browsing habits analytics

### Visualizations

* **Top Domains**: Bar chart of most visited websites
* **Activity Timeline**: Daily visits over time
* **Activity Heatmap**: Browsing patterns by hour and day of week
* **Category Distribution**: Pie chart of website categories
* **Hourly Patterns**: Bar chart showing peak browsing hours

## Requirements

* Python 3.7+
* Browser history data (automatically detected)

## Dependencies

* `streamlit`
* `plotly`
* `pandas`
* `browser-history`
* `numpy`
* `seaborn`
* `matplotlib`
* `urllib3`

## Privacy Note

This tool only reads your local browser history files. No data is sent to external servers – everything runs locally on your machine.

## Supported Browsers

* Google Chrome
* Mozilla Firefox
* Safari
* Microsoft Edge
* Opera

## Contributing

Feel free to open issues and submit pull requests!

## License

[MIT License](LICENSE)

## Author

Arpit Sengar ([@arpy8](https://github.com/arpy8))
