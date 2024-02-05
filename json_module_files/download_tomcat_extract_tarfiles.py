import requests
import tarfile

source_url="https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"
file_path="tomcat.tar.gz"


def download_tomy(source_url, file_path):
    try:
       response=requests.get(source_url)
       with open(file_path, "wb") as f:
           f.write(response.content)
           print("tomcat downloaded successfully")
       with tarfile.open(file_path,"r" ) as p:
           p.extractall("/home/ubuntu/PythonPractice/json_module_files")
           print("extracted tar files successfully")
    except requests.exceptions.RequestException as e:
        print("tomcat downloading failed!!!")

download_tomy(source_url, file_path)           
