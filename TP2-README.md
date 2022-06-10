# Rapport - TP-1

## Choix techniques : 
En sachant que l'application etait extremement légère  et qu'il n'yavais pas besoin d'un gros pasckage, j'ai choisis python:alpine3.16 
pour l'image Docker car elle était extremement légère.

Au niveau de l'affichage des différentes infos météo, il n'y avait pas de consignes précies, j'ai donc afficher quelques infos que je trouvais intéressantes.
## Commandes effectuées :
Après l'installation de docker, j'ai d'abord installé les différentes libraires que j'ai utilisé :
```
pip install requests
```
requests pour requeter l'API openweather
```
pip install pipreqs
```
pipreqs pour générer facilement le fichier requirements.txt

Une fois mon code terminé, je l'ai ensuite tester une première fois avec 
```
python weather.py
```

Après avoir bugfix, j'ai ensuite start Docker pour ensuite build, test et publish mon container :
```
systemctl start docker
```
start
```
docker login -u adrientarcy
```
login
```
docker build . -t tp1_weather:0.0.1
```
build

```
docker run tp1_weather:0.0.1
```
test (les variables d'environnement etait ici spécifiée dans le fichier Dockerfile)
```
docker tag tp1_weather:0.0.1 adrientarcy/tp1-weather:0.0.1
docker push adrientarcy/tp1-weather:0.0.1
```
publish

## Difficultés rencontrées :
J'ai eu quelques difficultés au niveau de la création du container. J'avais un peu de mal avec l'ordre des différentes commande.
