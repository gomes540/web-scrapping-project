# Cayena Project

This project consists in scrapping the website https://books.toscrape.com/, extract all book's information and deliver it to data analysts. For that we need to build a pipeline based on Data Engineer concepts. In this project we will use Python, Airflow and Google Cloud Platform stack.

## Airflow setup
 1. Initialize the database:
    ```pyhon
    docker-compose up airflow-init
    ```
 2. Start all services:
    ```pyhon
    docker-compose up
    ```
Now your airflow should be running. 

3. To access the Airflow Web UI you should access your local host port 8080:

    http://localhost:8080/

## Google Cloud Platform setup
For GCP we'll need to create a Service Account with specifics Roles, for that:

1. Visit your GCP dashbord:

    https://console.cloud.google.com/home/dashboard
    
2. Go to Service Account in IAM & Admin:

    ![image](https://user-images.githubusercontent.com/72705868/167996629-d27867ee-ba9b-48ce-a230-c463bdeedb7a.png)
    
3. Create a new Service Account:

    ![image](https://user-images.githubusercontent.com/72705868/167996917-3a45aa18-2ac5-411c-bb46-6323672d3582.png)

    1. Choose the Service Account display name and descripion (Optional)

        ![image](https://user-images.githubusercontent.com/72705868/167997753-1c0e4c5e-b0c4-48f5-af4c-7e14c4b53ca8.png) 
    
    2. Include ```BigQuery Admin``` and ```Storage Admin``` roles for this Account Service

        ![image](https://user-images.githubusercontent.com/72705868/167998552-296a1583-90fa-4486-899b-8ff0baa8320c.png)
    
    3. Create JSON Key for your Service Account

        Your Service Account has been created, so now you can create a JSON key for it. To do this click in your Service Account in ```Service Account``` page then click in ```Keys``` -> ```ADD KEY``` -> ```Create new key``` -> ```JSON```
        
        ![image](https://user-images.githubusercontent.com/72705868/167999702-bce1429f-a878-4cca-9230-6a7c668b11bd.png)
        
        It will download your json file for this Service Account. Save it because you'll need it to configure your GCP Connection in Airflow.







