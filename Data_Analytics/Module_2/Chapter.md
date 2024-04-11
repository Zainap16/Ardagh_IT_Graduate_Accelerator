# Chapter 2

## Exploring Databases

    1. Relational
    2. Non-relational

### The Relational Model
<img src="/Data_Analytics/Module_2/image.png" width="400" height="250">
<img src="/Data_Analytics/Module_2/image copy.png" width="400" height="250">
>unary relationship is when an entity has a connection with itself
<img src="/Data_Analytics/Module_2/image copy 2.png" width="400" height="250">

Binary relationships are the most common and easy to explore,whereas unary and ternary are comparatively complex and rare.
    
Relational Database:

<img src="/Data_Analytics/Module_2/image copy 3.png" width="400" height="250">

    
    associative table is both a table and a relationship.
    primary key is one or more attributes that uniquely identify a specific row in a table. 
    
    synthetic primary key is a primary key that is generated artificially by the database system, rather than being derived from the actual data being stored.
     foreign key is one or more columns in one table that points to corresponding columns in a related table. 
    
    You compose queries using a programming language called Structured Query Language (SQL).
    
    JOIN operation is used to combine rows from two or more tables based on a related column between them. This operation allows you to retrieve data from multiple tables simultaneously by specifying how the tables are related.
    
     a composite primary key is a primary key with more than one column. 
    
     database administrator (DBA) is a highly trained person who understands how database software interacts with computer hardware.
    DBA looks after how the database uses the underlying storage, memory, and processor resources assigned to the database. A DBA also looks for processes that are slowing the entire database down.
    
## Address Referential Integrity

<img src="/Data_Analytics/Module_2/image copy 4.png" width="400" height="250">

    • A specific customer can have many addresses, while a particular address belongs to a single customer.
    • A specific address has a single address type, while a particular address type can apply to many different addresses.
    • A specific address has a single state, while a particular state can exist in many different addresses. Relational DB Providers: SQL Server, MySQL, MariaDB & PostgreSQL, Aurora (AWS's cloud) 
    • relational DB:
        ○ Structured - organise rows and columns
        ○ Schema - predetermine schema that defines the structure of data including data types and relationship
        ○ SQL used to manipulate data.
        ○ ACID (Atomicity Consistency Isolation Durability) transaction 
        ○ Scalability
    • Non-relational (NoSQL) DB:
        ○ Structure -
        ○ More flexibility with the schema
        ○ Many NoSQL alternative query interface, some NoSQL support SQL query languages
        ○ CAP (Consistency, Availability, Partition)Theorem
        ○ Examples : 
         MongoDB (document store), Cassandra (wide-column store), Redis (key-value store), Neo4j (graph database)
    • NoSQL ""Not Only SQL" - is a DBSM designed to handle various types of data models beyond traditional tabular (relational) databases. NoSQL databases are often used for managing large volumes of unstructured, semi-structured, or rapidly changing data.
    
The term "NoSQL" doesn't mean that these databases don't use SQL (Structured Query Language) at all; rather, it implies that SQL is not the only query language supported by these databases. NoSQL databases may use SQL-like languages or proprietary query interfaces specific to their data model. 

## Key-value:
    
Key-value store is a type of non-relational database where data is stored as a collection of key-value pairs. Each piece of data is associated with a unique identifier (key), which is used to retrieve the corresponding value. Key-value stores offer flexibility, scalability, and high performance, making them suitable for applications requiring rapid read and write operations, such as caching, session management, and real-time analytics. Examples of key-value stores include Redis, Amazon DynamoDB, Apache Cassandra, and Riak.

<img src="/Data_Analytics/Module_2/image copy 5.png" width="400" height="250">

    • Document DB, value is restricted to a specific structured format. - ex JSON file format
    • Column-family databases are a type of NoSQL database that organizes data into columns rather than rows. In contrast to traditional relational databases where data is organized in rows and tables, column-family databases store data in column families, which are containers for rows that share the same column structure. Each column family can contain an arbitrary number of rows, and each row can have a different number of columns.
    
Graph databases are a type of NoSQL database that uses graph structures with nodes, edges, and properties to represent and store data. In a graph database, data is modelled as a network of interconnected nodes, where nodes represent entities (such as people, places, or things), edges represent the relationships between entities, and properties provide additional information about nodes and edges.

<img src="/Data_Analytics/Module_2/image copy 6.png" width="400" height="250">

    Online Transactional Processing (OLTP):
    
    • Online Transactional Processing (OLTP) is a type of database processing that manages and facilitates transaction-oriented applications. In an OLTP system, the primary focus is on managing day-to-day transactional operations of an organization, such as processing sales, orders, payments, or reservations in real-time.
    
    First Normal Form (1NF) - when it DOES NOT contain a repeating group. -> pg53 
     
    Second Normal Form - description contains duplicates -- redundancy - wasteful space 
     
    Update anomalies: 
     
    Updates - to change KH81, you need to change it twice-- update process cumbersome & time consuming. 
    Inconsistent data - KH81 may have two different descriptions or more throughout the database. 
    Additions - inefficient to add an item to the description without having the PK there. 
    Deletions - : If you delete invoice 14216 from the database and it is the only invoice that contains item CA75, deleting the invoice also deletes all information about item CA75. 
     
    Second normal form (2NF) when it is in first normal form and no non-key column (that is, a column that is not part of the primary key) is dependent on only a portion of the primary key. 
    When the primary key of a table contains only a single column, the table is automatically in second normal form 
     
    TIP for 2NF: if theres candinates keys, make a separate table for each canidante key, so that way each table has one PK. 
    
    3NF  
     
    Updates - changing sales rep name includes changing multiple rows 
    Inconsistent data - design does not prohibit multiple iterations of sales rep names example, sales rep might have 20 customers, its name will be entered 20 times! 
    Additions: To add sales rep 25 (Juanita Sanchez) to the database, she must represent at least one customer. If Juanita does not yet represent any customers, you either cannot record the fact that her name is Juanita Sanchez, or you must create a fictitious customer for her to represent until she represents an actual customer. Neither of these solutions is desirable. 
     Deletions: If you delete all the customers of sales rep 05 from the database, you will also lose all information about sales rep 05. 
    • Any column (or collection of columns) that determines another column is called a determinant (PK). 
    • Candidate key is a column or collection of columns that could function as the primary key. 
    • Third normal form (3NF) when it is in second normal form and the only determinants it contains are candidate keys. 
    
    TIP for 3NF: same as 2NF, BUT have a foreign key referencing the other table. 
    
    
    
    Online analytical Processing (OAP):
    
    Online Analytical Processing (OLAP) is a technology used for organizing, analyzing, and querying multidimensional data from data warehouses or other data sources. It enables users to perform complex, interactive analysis of data to gain insights and make informed decisions.
    
    OLAP systems are designed to handle large volumes of data and provide fast query response times, making them ideal for business intelligence and decision support applications. OLAP operates on multidimensional data models, where data is organized into dimensions and measures.
    
    
    Schema Concepts
    The design of a database schema depends on the purpose it serves. Transactional systems require highly normalized databases, whereas a denormalized design is more appropriate for analytical systems. A data warehouse is a database that aggregates data from many transactional systems for analytical purposes. Transactional data may come from systems that power the human resources, sales, marketing, and product divisions. A data warehouse facilitates analytics across the entire company.
    
    A data mart is a subset of a data warehouse. Data warehouses serve the entire organization, whereas data marts focus on the needs of a particular department within the organization. 
    
    A data lake stores raw data in its native format instead of conforming to a relational database structure. Using a data lake is more complex than a data warehouse or data mart, as it requires additional knowledge about the raw data to make it analytically useful. 
    
    Star Schema and Snowflake Schema are two common data modeling techniques used in designing data warehouses for Online Analytical Processing (OLAP) systems. Both schemas aim to optimize query performance and facilitate multidimensional analysis of data, but they differ in their approach to organizing dimensional data.
    
    1. **Star Schema**:
       - In a Star Schema, data is organized into a central fact table surrounded by multiple dimension tables. 
       - The fact table contains quantitative data or measures, such as sales revenue, quantity sold, or profit, and it typically has foreign key relationships with one or more dimension tables.
       - Dimension tables represent the various attributes or categories by which the data is analyzed, such as time, product, customer, or location. Each dimension table contains descriptive attributes related to the dimension.
       - The fact table serves as the centerpiece of the schema, with direct relationships (or "joins") to each of the dimension tables, forming a star-like structure when visualized graphically. Hence the name "Star Schema."
       - Star schemas are denormalized, meaning that dimensional data is stored redundantly in the fact table and dimension tables to optimize query performance for analytical queries. This denormalization simplifies querying and enables fast aggregation of data.
    
    2. **Snowflake Schema**:
       - The Snowflake Schema is an extension of the Star Schema, but it further normalizes dimension tables by breaking them into multiple smaller dimension tables.
       - In a Snowflake Schema, the dimension tables are normalized, meaning that they are broken down into sub-dimensions or hierarchies. For example, a single dimension table for "product" in a Star Schema might be split into separate tables for "product category," "product subcategory," and "product."
       - This normalization reduces data redundancy and improves data integrity by eliminating duplicate data, which can be advantageous for data warehousing environments where storage space is a concern.
       - However, Snowflake schemas can result in more complex queries due to the need for additional joins across multiple tables to retrieve data, which may impact query performance, especially in large-scale OLAP systems.
    
    In summary, while both Star and Snowflake schemas are effective for designing data warehouses for OLAP, the choice between them depends on factors such as the complexity of the data model, storage requirements, query performance considerations, and the specific needs of the organization. Star schemas are often favored for their simplicity and query performance benefits, while Snowflake schemas offer advantages in terms of data normalization and storage efficiency.
    
    Dimensionality refers to the number of attributes a table has. The greater the number of attributes, the higher the dimensionality. One dimension is time. One way to achieve this is by adding a start and end time of a products price.
    
    Data Acquisition Concepts
    
    Integration
    
    Extract Transform Load (ETL)
    
    Extract:  In the first phase, you extract data from the source system and place it in a staging area. The goal of the extract phase is to move data from a relational database into a flat file as quickly as possible. 
    Transform:  The second phase transforms the data. The goal is to reformat the data from its transactional structure to the data warehouse's analytical design.
    Load:  The purpose of the load phase is to ensure data gets into the analytical system as quickly as possible.
    
     
    ETL Vendors
    
    
    An initial load occurs the first time data is put into a data warehouse. After that initial load, each additional load is a delta load, also known as an incremental load. A delta load only moves changes between system.
    
    
    Data collection methods
    
    Application Programming Interfaces (APIs)
    API - method for computer systems to exchange information.
    
    Web service is an API you can call via HTTP. API does NOT have to be a web service.

<img src="/Data_Analytics/Module_2/eh.png.png" width="400" height="250">

    Web scraping
    
    Web scraping - programmatic retrieval of data from a website. 
    
    Human-in-the-loop
    
    Data exist in people minds. Ex - how customers feel about the services you provide.
    
    Surveys
    
    Surveys can collect data from your customers if they complete them.
    
    Surveys Tools
    
    Qualtrics - powerful tool for developing and administering surveys. Qualtrics API- use to integrate survey response data into a data warehouse for additional analysis.
    
    Observation
    
    Observation is the act of collecting primary source data, from either people or machines. Observational data can be qualitative or quantitative. Collecting qualitative observational data leads to unstructured data challenges.
    
Sampling

    ## Data Manipulation 
    
    • Create new data.
    • Read existing data.
    • Update existing data.
    • Delete existing data.
    
CRUD (Create, Read, Update, Delete)

<img src="/Data_Analytics/Module_2/meh.png" width="400" height="250">

SELECT 
FROM 

Filtering 

SELECT Animal_Name, Breed_Name
FROM  Animal
WHERE Animal_Type = 'Dog'

Filtering and Logical Operators

SELECT Animal_Name, Breed_Name
FROM  Animal
WHERE Animal_Type = 'Dog'
AND  Weight> 60 //  OR   Weight> 10

Sorting

SELECT  Animal_Name, Breed_Name
FROM   Animal
WHERE  Animal_Type = 'Dog'
AND   Weight> 60
ORDER BY Date_of_Birth ASC
If you want to return the youngest dog first, you change the ORDER BY clause as follows:
SELECT  Animal_Name, Breed_Name
FROM   Animal
WHERE  Animal_Type = 'Dog'
AND   Weight> 60
ORDER BY Date_of_Birth DESC
