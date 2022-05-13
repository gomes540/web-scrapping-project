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
      
 
## Run the Aiflow DAG

   After all those configuration steps now, in the Aiflow Web UI, you can see the dag. Congratulations!
   
   ![image](https://user-images.githubusercontent.com/72705868/168208816-2dc0c669-5fbe-4fe2-a6bf-e5ca36c30ecc.png)
   
   Note: To run your dag, first you need to verify if your dag is unpaused
   
   ![image](https://user-images.githubusercontent.com/72705868/168209068-aeb05766-0b5a-43f7-8d95-43312b650541.png)

   To start your dag you can click here:
   
   ![image](https://user-images.githubusercontent.com/72705868/168209230-4db24bf7-2fd4-47bf-9451-b2b068510b4b.png)


## See the results

1. Results in Airflow

   Click in the dag and you can see all tasks and if they were a success or a failure
   
   ![image](https://user-images.githubusercontent.com/72705868/168209599-8a6cda65-213a-47af-a441-26c3d867d0c9.png)
   
   Also you can see the tasks dependencies accessing the `Graph` button
   
   ![image](https://user-images.githubusercontent.com/72705868/168210222-34f8a984-f742-44c6-9797-2d980157c7aa.png)
   
2. Google Cloud Platform

  1. Data Lake
     
     Accessing `Google Cloud Storage (GCS)` you'll see the bucket `cayena-bucket`
     
     ![image](https://user-images.githubusercontent.com/72705868/168210811-c1d5fc9c-fca6-40a5-9b9a-9728b747fa6d.png)
     
     Inside this bucket you can see a folder called `books-daily-data` which contains all the data extracted in the proccess
     
     ![image](https://user-images.githubusercontent.com/72705868/168211101-64347273-1bae-44b1-a108-466606810662.png)
     
  2. Data Warehouse

     Accessing the `BigQuery` you can see all the data in a partitioned table called `books_history`
     
     ![image](https://user-images.githubusercontent.com/72705868/168211518-5bf4a315-5621-4131-bced-e55a3fd148f5.png)
     
     Table content in a specific partition:
     
     ![image](https://user-images.githubusercontent.com/72705868/168212974-1f886c20-d450-446b-90af-6528d92812b9.png)
     
     
## Dashboard

   https://datastudio.google.com/reporting/c50ede6d-998f-407e-b2e2-c25c70003702


## Diagram

   ![image](https://user-images.githubusercontent.com/72705868/168224732-dcd10ff5-7b1f-4aa1-8a85-de4c2db62010.png)








   
   

      
      








