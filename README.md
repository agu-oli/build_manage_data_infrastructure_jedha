A .csv file in an S3 bucket containing enriched information about weather and hotels for each french city

A SQL Database where we should be able to get the same cleaned data from S3

Two maps where you should have a Top-5 destinations and a Top-20 hotels in the area. You can use plotly or any other library to do so. It should look something like this:

# Build & Manage a Data Infrastructure Jedha's module deliverable 

## In this repository you will find the files corresponding to the Build & Manage a Data Infrastructure Jedha's module deliverable.

  - A .csv (df_final_kayak_project.csv) file containing enriched information about weather and hotels for the following list of french cities:
    
  -     cities = [
        "Mont Saint Michel", "St Malo", "Bayeux", "Le Havre", "Rouen", "Paris", 
        "Amiens", "Lille", "Strasbourg", "Chateau du Haut Koenigsbourg", "Colmar", 
        "Eguisheim", "Besancon", "Dijon", "Annecy", "Grenoble", "Lyon", "Gorges du Verdon", 
        "Bormes les Mimosas", "Cassis", "Marseille", "Aix en Provence", "Avignon", "Uzes", 
        "Nîmes", "Aigues Mortes", "Les Saintes-Maries-de-la-Mer", "Collioure", "Carcassonne", 
        "Ariege", "Toulouse", "Montauban", "Biarritz", "Bayonne", "La Rochelle"]
    
 - The .csv file was created by collecting data from Booking website and Open Weather API (https://openweathermap.org/appid) through scraping and .get requests
      - The scraping script 'scrapy3.py' is also shared in this repository.
      - the file booking5.json gathers the data collected from Booking website through Scrapy.
      - The notebook 'projet_kayak.ipynb' shows:
          - how all the .get requests were done to collect the cities coordinates and weather,
          - how the corresponding Pandas DataFrames were created and merged with the data collected with Scrapy from Booking.

- the .csv file (df_final_kayak_project.csv) is availables in the following s3 bucket: s3://projet-kayak-jedha/df_final_kayak_project.csv

- A SQL Database where it is possible to query the clean data present in the s3 bucket mentioned above at the following endpoint: jedha-db-adei.clcggo264zgf.eu-west-3.rds.amazonaws.com

  - the SQL database was created on python in notebook projet_kayak_sql_db.ipynb uploaded in this repository.
 
- A nootebook with visulizations (maps) of the data gathered in the .csv file df_final_kayak_project.csv
