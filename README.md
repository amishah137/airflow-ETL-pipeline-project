# airflow-ETL-pipeline-project
This project extracts data using Twitter API, uses python to transform data, deploy the code on Airflow/EC2 and save the final result on Amazon S3.

## Prerequisites
1. Twitter APIs - To avail the Twitter APIs (Tweepy package), setup an tweeter account and get api credentials.
2. AWS Account - To use EC2 and S3 instance.

## Steps to follow:
1. Create an EC2 instace with:
  - name: airflow-test
  - OS: Ubuntu
  - Instance type: t2.micro
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
    note down the username and password
3. 
