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

## Configure Airflow

1. Variable

    1. You'll need to import the variables in JSON file to your airflow. Download the file and extract the json file.
    
       file: [cayena_variables.zip](https://github.com/gomes540/cayena/files/8683926/cayena_variables.zip)
    
       Go to `Admin` -> `Variables` -> `Choose file`
    
       ![image](https://user-images.githubusercontent.com/72705868/168206789-e6d98edd-0ed1-4c4d-9db9-aed63ede58b6.png)
       
    2. Get your GCP project id

        ![image](https://user-images.githubusercontent.com/72705868/168207227-c2d8bbae-94f4-4f28-81d4-33a97d44dfb4.png)

    
    2. Create a new variables called `cayena_project_id` and paste your GCP project id

        ![image](https://user-images.githubusercontent.com/72705868/168207321-8f9bcf32-ac61-41ba-8dee-86eaea2aae5a.png)
        
        ![image](https://user-images.githubusercontent.com/72705868/168207411-6bf2b261-fdcc-49a3-baf1-fb92f49e01d4.png)


2. Connections

   1. Create a new connection for your GCP project called `gcp_cayena`

      ![image](https://user-images.githubusercontent.com/72705868/168207602-e98d0631-c734-4be9-8a3b-cc2171d2f3b6.png)
      
      Connection Configuration:
      
      `Connection Id: gcp_cayena`
      
      `Connection Type: Google Cloud`
      
      `Keyfile JSON: Your Service Account Key file`
      
      Note: Remember that your created and downloaded your Key in the step `Google Cloud Platform setup` 
      
      
      ![image](https://user-images.githubusercontent.com/72705868/168207721-bfbb84fa-450e-431f-9cf3-9abc5c1262a3.png)

      
      








