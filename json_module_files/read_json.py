import json

source_file="org.springframework_spring-core.json"
destination_file="destination.json"

with open(source_file, "r") as f:

   data=json.load(f)
   for package, version in data.items():
       for version_numbers, oneversion in version.items():
           if version_numbers=="5.3.26":
               with open(destination_file, "w") as p:
                   dumped_value=json.dump(oneversion, p, indent=4)
                   print("version 5.3.26 related values dumped into destination file successfully")
   

