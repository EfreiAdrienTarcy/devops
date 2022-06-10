# Rapport - TP-2

## Choix techniques : 
J'ai utilisé Flask pour créer l'API car c'etait c'est une librairie simple d'utilisation adaptée à notre besoin

Tout comme pour le TP-1, il n'y avait pas de consignes précises pour l'affichage des données météo. J'ai donc repris les meme données que la derniere fois.
## Commandes effectuées - Local/Docker:
La première étape a été d'installer flask :
```
pip install flask
```

Une fois l'importation faite, il fallait mettre à jour le fichier requirements.txt :
```
pipreqs --force

```

Une fois l'API developpée, J'ai effectué mes différents tests avec
```
flask run
```

Une fois mon code terminé, je l'ai ensuite tester une première fois avec 
```
python weather.py
```

Une fois sur du bon fonctionnement de l'API, je l'ai déployé sur Docker avec les commandes classiques :
```
systemctl start docker

docker login -u adrientarcy

docker build . -t efrei-devops-tp2:0.0.1

docker tag efrei-devops-tp2:0.0.1 adrientarcy/efrei-devops-tp2:0.0.1

docker push adrientarcy/tp1-weather:0.0.1
```

## Commandes effectuées - Github Actions
Définitino du trigger de la GitHub Action :
```
on:
  push:
    branches: [ main ]
```
login à DockerHub en utilisant les secrets
```
name: Login to DockerHub
uses: docker/login-action@v2
    with:
        username: ${{ secrets.DOCKER_USER_NAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
```
name: Build and push
uses: docker/build-push-action@v3
    with:
        context: .
        file: Dockerfile
        push: true
        ags: ${{ secrets.DOCKER_USER_NAME }}/efrei-devops-tp2:latest

```

## Difficultés rencontrées :
Pas de difficultés particulières rencontrés sauf au niveau des GitHub Actions, le temps de les prendre en main
