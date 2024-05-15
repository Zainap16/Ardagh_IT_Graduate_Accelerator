Power BI (Business Intelligence) 

# Getting Started

* Microsoft Power BI is a collection of software services, apps, and connectors that work together to turn your unrelated sources of data into coherent, visually immersive, and interactive insights

* Power BI lets you easily connect to your data sources, clean, and model your data without affecting the underlying source, visualize (or discover) what's important, and share that with anyone or everyone you want.

3 elements:

1. Power BI Desktop
2. Power BI Service
3. Power BI Mobile

Elements: datasets, reports and dashboards.
All elements are organized into workspaces and created on capacities.

Capacities:

Capacities are a core Power BI concept representing a set of resources used to host and deliver your Power BI content. Capacities are either shared or dedicated. A shared capacity is shared with other Microsoft customers, while a dedicated capacity is fully committed to a single customer. Dedicated capacities require a subscription. By default, workspaces are created on a shared capacity.

Workspaces:

- containers for dashboards, reports, datasets and dataflows in Power BI. 2 types of workpaces, namely: My Worspace and Workspaces.

* my workspace: is the personal workspace for any Power BI customer to work with your own content. Only you have access to your My workspace. You can share dashboards and reports from your My Workspace. If you want to collaborate on dashboards and reports or create an app, then you want to work in a workspace.
* Workspace: are used to collaborate and share content with colleagues. You can add colleagues to your workspaces and collaborate on dashboards, reports, and datasets. With one exception, all workspace members need Power BI Pro licenses.

### Semantic models
A semantic model is a collection of data that you import or connect to. Power BI lets you connect to and import all sorts of semantic models and bring all of them together in one place. Semantic models can also source data from dataflows.

### Reports
A Power BI report is one or more pages of visualizations such as line charts, maps, and other elements. You can create reports in Power BI from scratch, import them from shared dashboards, or have Power BI generate them when connecting to datasets

### Dashboards 

Why do people create dashboards? Here are just some of the reasons:

* To see all information needed to make decisions in one glance.

* To monitor the most important information about your business.

* To ensure all colleagues are on the same page, viewing and using the same information.

* To monitor the health of a business, product, business unit, or marketing campaign, etc.

* To create a personalized view of a larger dashboard and show all the metrics that matter to them.

### Describe cleaning and transforming data in Power BI Desktop

Power BI Desktop has three views:

- Report view: You can create queries to build compelling visualizations that you can share with others. You can arrange them as you want them to appear.

- Data view: See the data in your report in data model format, where you can add measures, create new columns, and manage relationships.

- Model view: Get a graphical representation of the relationships that are established in your data model and manage or modify them as needed.

* Power BI Desktop includes the Power Query Editor tool, which can help you shape and transform data so that it's ready for your models and visualization

### Transforming data
As mentioned previously, transforming data is the process of putting data into a format that is useable in your reports.

### AI Insights

Power BI’s insights feature helps organizations easily identify insights such as anomalies and trends in your data as you interact and consume elements such as reports, dashboards, and visualizations. It notifies you if there are interesting insights and provides explanations for them. It works out-of-the-box on any report, so you can automatically start getting insights from your reports without any setup.

* Power BI has multiple insights features that use artificial intelligence (AI):

* Insights for reports: Analyzes data and finds anomalies and trends in your data as you interact with reports.

* Insights for individual visuals: Analyzes and explains the fluctuations of data points in visuals.

* Insights for dashboard tiles: Looks at the data being used to render that tile and presents them in interactive visuals.

* Quick Insights for datasets: Automatically generate data insights on a dataset in the Power BI service.

* AI Insights for data models in Power Query: Provide access to pretrained machine learning models from Azure Cognitive Services.

### Insights
The Insights pane currently shows three types of insights:

* Anomalies: Represents something that is out of the ordinary from what is expected. For example, a smart thermostat that suddenly reads the temperature as 100 F when it's typically 72 F would be considered an anomaly.

* Trends: Represents a pattern that is found in time-series datasets. For example, if a company’s sales are steadily increasing through the month of April that would represent a trend.

* Key Performance Indicator (KPI) analysis: Helps you evaluate the current value against a defined target. For example, a company might set a sales goal at 1.2 million, but currently they are at 1 million.

  
### Anomalies

There are three types of anomaly insights:

* Significant anomaly: The anomaly has a high score. Anomaly score indicates how far the point is from the expected range.

* Recent anomaly: The most recent anomaly in the measure.

* Anomaly summary: This insight type summarizes multiple anomalies in the measure.

Trends
A trend occurs when there's a prolonged increase or decrease in time-series data.

There are four main trends flagged:

Long trend: The trend is significant and is the longest trend within a single series or across multiple series in a visual.

Steep trend: The trend is significant and is the steepest trend within a single series or across multiple series in a visual.

Recent trend: The trend is significant and is the most recent trend within a single series or across multiple series in a visual.

Trend reversal: Recent trend in a single series or across multiple series in a visual where the reversal is significant, compared to the previous trend segment.

### Build a basic dashboard

You need to take the following steps:

Prepare your data: Preparing the data ensures that it's in a format that Power BI can easily consume.

Build a report: The report contains the visuals that you want to include in your dashboard. Depending on the scenario, reports can be built in either Power BI Desktop or using the Power BI Service.

Pin the report visuals to a dashboard: Dashboards are the primary element that users use for viewing data. They can include data from multiple reports as needed.

Share a link to the dashboard: Any users with the link and the necessary permissions are easily able to view and interact with the data.








