# Module One

## Chpater 1

### Data Analytics:
* Conceptional understanding of data (theoretical aspect)
* Hands-on manipulation of data (practical aspect)

1. What the role of a Data Analyst is and the scope of data analytics.
2. The process of data analytics. 
3. The techniques of data analytics.
4. The role of data governance

Data analyst role is to transform raw data into actionable insights that guide decision-making processes within an organization. Key responsibilities:

1. Data Collection & Preparation:
    * Sourcing data from various channels (databases, spreadsheets and external sources).
    *  Cleaning & organizing data to ensure: accuracy, consistency and ready for analysis.
2. Data Analytics:
    *  Employing statistical methods, machine learning techniques/other analytic tools to interpret data.
    *  Identify trends, patterns & correlations that might not be immediately obvious.
3. Data visualization & storytelling:
    *  Creating visual representations of the data (charts, graphs, & dashboards to make complex info easily understandable)
    *  Articulating findings I a compelling narrative to comms the significance of data to stakeholders.
4. Decision Support
    *  Making recommendations based on data-driven insights to help guide business decisions
    *  Providing context around data, including potential implications & future trends
5. Collaboration & Comms
    *  Working closely with other departments, like marketing, finance & operations to understand their data needs & provide insight.
    *  Effectively comms complex data findings in a clear & concise manner to non-technical stakeholders.
6. Continuous learning & adaptation:
    *  Keeping up to date with the latest industry trends, tools & technologies in data analysis.
Adapting new types of data & analytical methods as the organization's needs to evolve.


### Responsibilties of DA: 

<img src="/Data_Analytics/Module_1/respos_da.png" width="400" height="250">

*Moore's Law* _is a prediction made by Gordon Moore, co-founder of Intel, in 1965. Simply put, it states that the number of transistors (tiny switches) on a computer chip doubles about every two years, leading to an exponential increase in computing power. This doubling occurs while the cost of computer chips remains roughly the same. In simpler terms, it means that over time, computers become faster, more powerful, and cheaper to produce. This law has held true for many decades and has been a driving force behind the rapid advancement of technology._ 

### Occupation of DA: 

<img src="/Data_Analytics/Module_1/job_da.png" width="400" height="250">

### Analytic Process:

    • Data acquisition.
    • Cleaning and manipulation
    • Analysis
    • Visualization
    • Reporting and communication

### Notes:

    • The analytic process is iterative.
    • Analytics:
        ○ Descriptive A
        ○ Predictive A
        ○ Prescriptive A

### Machine learning, artificial intelligence and deep learning:

    • ML - uses algorithms to discover knowledge in your dataset. Some cases where machine learning commonly adds value:
        ○ Discovering anomalies in system and application logs that may be indicative of cybersecurity incident.
        ○ Forecasting product sales based on market and environmental conditions.
        ○ Setting prices for hotel rooms far in advanced based on forecasted demand.
        ○ Forecasting product sales based on market & environmental conditions.
    • Artificial Intelligence (AI) - includes any type of technique where you are attempting to get a computer system to imitate human behavior. Basically asking the computer system to artificiality behave as if they were intelligent.
    • Machine Learning (ML) - subset of AI techniques attempt to apply stats to data problems in an effort to discover new knowledge. 
    • Deep Learning - subdivision of ML uses complex techniques, known as neural networks, to discover knowledge in a certain way. Its commonly used for image, video, & sound analysis.

### Relationship between AI, ML & DL

<img src="/Data_Analytics/Module_1/relationship_ai.png" width="400" height="250">

#### DA tools
    • Spreadsheets (excel) & google sheets
    • R programming (advanced) - RStudio

CHAPTER 2: UNDERSTADING DATA

*data element* is an attribute about a person, place or thing which contains data within a range of values. They also s=describe characteristics of activities including orders/transaction/events. (pet name, animal type -- heading names)

*data type* limits the values a data element can have.

## Tabular Data

* Tabular data is data organized into a table, made up of columns and rows. 

* A table represents information about a single topic. Each column represents a uniquely named field within a table, also called a variable, about a single characteristic.

* Relational database management system (RDMS), - named as a database, extends the tabular model. Instead of having all data in a single table, a database organizes related data across multiple tables.

* The connection between tables is known as a relationship. Oracle, Microsoft SQL Server, MySQL, and PostgreSQL are examples of database software. Tabular data is the concept that underpins both spreadsheets and relational databases.

### Structured Data Types:

* Structured data is tabular in nature and organized into rows and columns. Structured data is what typically comes to mind when looking at a spreadsheet. With clearly defined column headings, spreadsheets are easy to work with and understand. In a spreadsheet, cells are where columns and rows intersect.

#### Character:

The character data type limits data entry to only valid characters. Characters can include the alphabet that you might see on your keyboard, as well as numbers. Depending on your needs, multiple data types are available that can enforce character limits.

* Alphanumeric is the most widely used data type for storing character-based data. As the name implies, alphanumeric is appropriate when a data element consists of both numbers and letters

* Alphanumeric data type is ideal for storing product stock-keeping units (SKUs)

<img src="/Data_Analytics/Module_1/sku.png" width="400" height="250">

#### Rational Numbers:
<img src="/Data_Analytics/Module_1/image.png" width="400" height="250">

<img src="/Data_Analytics/Module_1/img_1.png" width="400" height="250">

<img src="/Data_Analytics/Module_1/img_2.png" width="400" height="250">

#### Currency

<img src="/Data_Analytics/Module_1/currency.png" width="400" height="250">

<img src="/Data_Analytics/Module_1/strong_weak_typing.png" width="400" height="250">

### Unstructured data types:

Unstructured data(digital images, audio recordings & open-minded surveys) is any type of data that does not fit neatly into the tabular model. 

<img src="/Data_Analytics/Module_1/img_3.png" width="400" height="250">

<img src="/Data_Analytics/Module_1/img_4.png" width="400" height="250">

<img src="/Data_Analytics/Module_1/img_5.png" width="400" height="250">

### Categories of Data:

#### Quantitative vs Qualitative Data

* Quantitative data consists of numeric values. 

* Quantitative data answers questions like “How many?” and “How much?” Qualitative data consists of frequent text values. They are descriptive data.

#### Discrete vs Continuous Data

1. *Discrete Data*: Discrete data consists of distinct, separate values. These values are typically counted and often represent things that can be counted in whole numbers, such as the number of students in a class, the number of cars in a parking lot, or the number of books on a shelf. Discrete data can only take specific values and usually doesn't have decimal points. For example, you can have 3 apples, but you can't have 3.5 apples.

2. *Continuous Data*: Continuous data, on the other hand, can take any value within a range. It's like a continuous flow without interruption. Continuous data is measured and can have infinite possible values within a given range. Examples of continuous data include measurements like height, weight, temperature, and time. These values can be fractions or decimals and can take on any value within a certain range. For instance, you can measure someone's height as 5.5 feet, and it could be even more precise like 5.5421 feet.

* Note: Qualitative data is discrete, but quantitative data can be either discrete or continuous data.

#### Categorical Data

Categorical data refers to data that represents categories or groups. Unlike numerical data, which represents quantities or measurements, categorical data represents characteristics or qualities. 

#### Dimensional Data

* "Dimensional data" typically refers to data organized in a dimensional model, which is a data structure optimized for data warehousing and online analytical processing (OLAP). In simpler terms, it's a way of organizing data in a database to make it easier to analyze and understand, especially for business intelligence purposes.

* Fact tables store measurement data that is of interest to a business. A veterinary practice may want to answer some questions about appointments. A table holding appointment data would be called a fact table.

* Semi-structured data is data that has structure and that is not tabular. Email is a well-known example of semi-structured data. Every email message has structural components, including recipient, sender, subject, date, and time. However, the body of an email is unstructured text, while attachments could be anything type of file.

#### Common File Format

* Text files are one of the most commonly used data file formats. As the name implies, they consist of plain text and are limited in scope to alphanumeric data

* Comma-delimited, it is known as a comma-separated values (CSV) file.
file is tab-delimited, it is called a tab-separated values (TSV) file

* JavaScript Object Notation (JSON) is an open standard file format, designed to add structure to a text file without incurring significant overhead. One of its design principles is that JSON is easily readable by people and easily parsed by modern programming languages. Languages such as Python, R, and Go have libraries containing functions that facilitate reading and writing JSON files.

* Extensible Markup Language (XML) is a markup language that facilitates structuring data in a text file. While conceptually similar to JSON, XML incurs more overhead because it makes extensive use of tags. Tags describe a data element and enclose each value for each data element. While these tags help readability, they add a significant amount of overhead.

* In 1999, XML was the data format of choice and facilitated Asynchronous JavaScript and XML (Ajax) web development techniques. AJAX allowed client applications, written in HTML, to retrieve data from a server asynchronously. Without having to wait for a server response, the speed with which dynamic web pages operated increased. 

* HyperText Markup Language (HTML) is a markup language for documents designed to be displayed in a web browser. HTML pages serve as the foundation for how people interact with the World Wide Web. Similar to XML, HTML is a tag-based language. 


* Note: Common file formats make it easy for people to read a file's contents and facilitate interoperability between tools. Delimiters separate variable-length fields in a file. The comma and the resultant CSV file are among the most commonly used formats for exchanging text files. To provide additional metadata about data values and support more complex data structures, XML and JSON were developed. JSON is a preferred format, given its low overhead, especially when compared with XML.