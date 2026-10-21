#  Interactive FinTech Sales Analytics & Dashboard

An end-to-end data analytics project featuring interactive data models and visualizations built in Microsoft Excel and Power BI Desktop. This project analyzes multi-region FinTech transactional data, key performance metrics (KPIs), product volume breakdowns, and revenue growth trends.

---

##  Project Overview

The goal of this project is to model and visualize transactional data for a FinTech platform across multiple financial product lines (Equity Funds, Treasury Bills, Fixed Income, Mutual Funds, and ETFs).

It delivers a fully interactive **Power BI Dashboard** connected to structured dataset tables, offering deep insight into overall revenue, active transaction volumes, regional distributions, and monthly revenue trajectories.

---

##   Tech Stack & Tools

- **Data Processing & Analytics:** Microsoft Excel (Calculated Fields, Dynamic Slicers, Pivot Tables)
- **Business Intelligence & Visualization:** Power BI Desktop (Interactive Slicers, KPI Cards, Drill-down Charts, DAX/Aggregations)
- **Version Control:** Git & GitHub

---

##  Dashboard Features & Key Metrics

1. **Top-Level KPI Cards:**
   - **Total Revenue:** Displays live aggregated gross transaction volume ($233K+).
   - **Total Transactions:** Dynamic count of distinct transactions (10 completed transactions filtered).
2. **Interactive Status Slicer:**
   - Allows real-time dynamic filtering across all canvas visuals by transaction status (`Completed`, `Pending`, `Failed`).
3. **Product Type Breakdown (Column Chart):**
   - Ranks revenue across product categories, highlighting Equity Funds and Treasury Bills as top performance drivers.
4. **Regional Share (Donut Chart):**
   - Visualizes global revenue distribution across South (41.82%), North (39.48%), West, and East regions.
5. **Monthly Trajectory (Line Chart):**
   - Sequential monthly trend analysis tracking revenue momentum across Q1 (January – March).

---

## Repository Structure

```text
├── Data/
│   └── SalesData.xlsx                  # Clean transactional dataset
├── Dashboards/
│   └── FinTech_Sales_Dashboard.pbix    # Interactive Power BI Report File
├── Screenshots/
│   └── dashboard_overview.png          # Visual preview of the live dashboard
└── README.md                           # Project Documentation
