import requests

source_url="https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"
file_path="tomcat.tar.gz"
#/home/ubuntu/PythonPractice/json_module_files


def download_tomy(source_url, file_path):
    try:
       response=requests.get(source_url)
       with open(file_path, "wb") as f:
           f.write(response.content)
           print("tomcat downloaded successfully")
    except requests.exceptions.RequestException as e:
        print("tomcat downloading failed!!!")

download_tomy(source_url, file_path)
