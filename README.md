# airflow-ETL-pipeline-project
This project extracts user information using Twitter API, uses python to transform data, deploy the code on Airflow/EC2 and save the final result on Amazon S3.

## Prerequisites
1. Twitter APIs - To avail the Twitter APIs (Tweepy package), setup an tweeter account and get api credentials.
2. AWS Account - To use EC2 and S3 instance.

## Steps to follow:
1. Create an EC2 instace with:
  - name: airflow-test
  - OS: Ubuntu
  - Instance type: t2.medium (free tier - t2.micro runs out of memory while executing the airflow).  
  - key-pair(name, type, file format): airflow-ec2-key, RSA, ".pem" (default)
  - Network settings: check "Allow HTTPS traffic from Internet" and "Allow HTTP traffic from Internet".
  - Now, Launch the EC2 instance
2. Login into the instance using SSH client and update the instance as follow:
    ```
    sudo apt-get update
    sudo apt install python3-pip
    sudo pip install apache-airflow
    sudo pip install pandas 
    sudo pip install s3fs
    sudo pip install tweepy
    ```
    Now, Check the airflow is working
    ```
    airflow
    ```
    ```
    airflow standalone
    ```
    Note down: the username and password to login the airflow dashboard later.
3. Create AWS S3 bucket with name 'ami-airflow-etl-test' with EC2.
4. Create IAM role with name 'ec2_s3_airflow_role' (note: use underscore instead of hyphens) with S3 full access and EC2 Full Access.
5. Associate it to our EC2 instance. Go to Action --> security --> Modify IAM Role and Add 'ec2_s3_airflow_role'.
6. Open a new terminal of EC2 instance.
    ```
    cd airflow
    ```
    ```
    mkdir tweeter_dag && cd tweeter_dag
    ```
    Copy two files 'dag_tweeter.py' and 'etl_tweeter.py' in the folder tweeter_dag.
7. Go to first terminal and restart the airflow.


### Go to Dashboard :
* Use Public-IPv4-DNS:8080 on web browser
* Check console:
  ![image](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/3f409ef0-e0bf-46c4-9937-bacf9f67381e)

* Click on 'dag_tweeter'
  ![image](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/a921d599-2687-42db-944e-bfe53faaa023)

* Go to Graph
  ![image](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/a7559cba-5a16-4b98-8a6c-8d7ffa17977f)

* The node turns Green on successful execution
  ![Screenshot from 2023-08-18 11-53-55](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/7833f30f-31ab-49dc-9823-77b4d3aa0aa6)

* Click on the node --> Check logs
  ![image](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/3acb2fee-85da-446f-bbda-d4164eb5720f)

  ![image](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/88715a63-8545-4366-98f8-05dcd548d195)

* Go to the AWS home --> S3 bucket
  ![Screenshot from 2023-08-18 11-49-13](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/9057315d-d140-4151-9877-fde102fdcb48)

  ![Screenshot from 2023-08-18 11-49-43](https://github.com/amishah137/airflow-ETL-pipeline-project/assets/11003645/008253eb-13da-48d3-8270-8de50b02925b)

### After steps:
* After completion of this excercise, Delete your EC2 and S3 instances.
* Revoke the access token keys for Twitter API
