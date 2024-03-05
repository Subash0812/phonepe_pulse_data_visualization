# Phonepe Pulse Data Visualization
## Problem Statement
The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.

1. Extract data from the Phonepe pulse Github repository through scripting and clone it.
2. Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.
3. Insert the transformed data into a MySQL database for efficient storage and retrieval.
4. Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.
5. Fetch the data from the MySQL database to display in the dashboard.
6. Provide at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.

Work Flow:
1. Data extraction: Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a MySQL database.
2. Data transformation: Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.
3. Database insertion: Use the "SQLAlchemy" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.
4. Dashboard creation: Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different States and years to display.
5. Data retrieval: Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.

### GUI
![image](https://github.com/Subash0812/phonepe_pulse_data_visualization/assets/125037396/0f71f79a-0b42-4616-b7ff-f3daa83254f3)
![image](https://github.com/Subash0812/phonepe_pulse_data_visualization/assets/125037396/3e536de5-44a9-4ef5-8245-0983051dab7c)
![image](https://github.com/Subash0812/phonepe_pulse_data_visualization/assets/125037396/6697ccc1-b850-42cb-aa2d-0d4c291e84cf)
![image](https://github.com/Subash0812/phonepe_pulse_data_visualization/assets/125037396/c3032d01-c0c1-465c-96ad-63affdb43d9b)


We create a web app to analyse the Phonepe transaction and users depending on various Years, Quarters, States, and Types of transaction and give a Geographical and Geo visualization output based on given requirements.

Github repository, making it a valuable tool for data analysis and decision-making. Overall, the result of this project will be a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the Phonepe pulse Github repository.
