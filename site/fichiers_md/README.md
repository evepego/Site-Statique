# TP4 - Spéléologie réseau : descente dans les couches

## I. Mise en place du lab :
### 1. Création des réseaux :
### 2. Création des VMs :
### 3. Mise en place du routage :

## II. Spéléologie réseau :
### 1. ARP :

#### A. Manip 1
##### 1 : 
Pour vider la table ARP, j'utilise la commande suivante :
```bash
sudo ip neigh flush all
```
##### 2 :
- Pour afficher la table ARP, j'utilise la commande suivante :
```bash
ip neigh show
```
- On obtiendra :
```bash
10.1.0.1 dev enp0s3 lladdr 0a:00:27:00:00:11 DELAY
```
- C'est la connexion entre putty et mon oridinateur.
##### 3 : 
- J'effectue la commande pour afficher la table ARP vue ci-dessus.
```bash
10.2.0.1 dev enp0s3 lladdr 0a:00:27:00:00:12 DELAY
```
- C'est la connexion entre putty et mon oridinateur.
##### 4 :
- J'effectue la commande : 
```bash
ping server1.tp4
```
- J'effectue la commande pour afficher la table ARP vue ci-dessus.
```bash
10.1.0.254 dev enp0s3 lladdr 08:00:27:16:c7:61 REACHABLE
10.1.0.1 dev enp0s3 lladdr 0a:00:27:00:00:11 REACHABLE
```
- 1ère ligne : C'est la connexion entre mon client et mon routeur.
- 2ème ligne : C'est la connexion entre putty et mon oridinateur.
##### 5 :
- J'effectue la commande pour afficher la table ARP vue ci-dessus.
```bash
10.2.0.1 dev enp0s3 lladdr 0a:00:27:00:00:12 DELAY
10.2.0.254 dev enp0s3 lladdr 08:00:27:1a:55:e9 STALE
```
- 1ère ligne : C'est la connexion entre putty et mon oridinateur.
- 2ème ligne : C'est la connexion entre mon client et mon routeur.

#### B. Manip 2
##### 1.
Pour vider la table ARP, j'utilise la commande suivante :
```bash
sudo ip neigh flush all
```
##### 2.
- Pour afficher la table ARP, j'utilise la commande suivante :
```bash
ip neigh show
```
- AFFICHER ET EXPLIQUER LES LIGNES

##### 3.
- J'effectue la commande : 
```bash
ping server1.tp4
```
- AFFICHER ET EXPLIQUER DES LIGNES

##### 4.
- J'effectue la commande vue ci-dessus pour afficher la table ARP.
- AFFICHER ET EXPLIQUER DES LIGNES

#### C. Manip 3
##### 1.
- Pour vider la table ARP sur mon PC, j'utilise la commande suivante :
```bash
arp -d
```
##### 2.
- Sur mon PC, j'effectue la commande suivante :
```bash
arp -a
``` 
- EXPLIQUER CHANGEMENTS

#### D. Manip 4
##### 1.
- Pour vider la table ARP, j'utilise la commande suivante :
```bash
sudo ip neigh flush all
```
##### 2.
- J'affiche la table ARP de client1.
- Pour activer la carte NAT :
    - J'éteind la machine client1
    - Dans **configurations** puis dans **réseau**, je crée une nouvelle carte en NAT.
    - Je rallume la VM client1.


### 2. Wireshark :
#### A. Interception d'ARP
#### B. Interception d'une communication
#### C. Interception d'un trafic HTTP
## Annexe 1 : Installation d'un client graphique
 
 faire les cadre:
 ```bash

```








table arp avant internet

```
[root@client ~]# sudo ip neigh show
10.1.0.1 dev enp0s3 lladdr 0a:00:27:00:00:11 REACHABLE
```

table arp après curl sur google.com

```
[root@client ~]# ip neigh show
10.1.0.1 dev enp0s3 lladdr 0a:00:27:00:00:11 REACHABLE
10.0.3.2 dev enp0s8 lladdr 52:54:00:12:35:02 REACHABLE
```