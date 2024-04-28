#!/bin/bash

# Make users and group
sudo useradd sonarr -u 201
sudo useradd radarr -u 202
sudo useradd lidarr -u 203
sudo useradd readarr -u 204
sudo useradd mylar -u 205
sudo useradd prowlarr -u 206
sudo useradd qbittorrent -u 207
sudo useradd jackett -u 208
sudo useradd overseerr -u 209
sudo useradd plex -u 210
sudo useradd sabnzbd -u 211
sudo useradd jellyseerr -u 212
sudo useradd bazarr -u 213
sudo groupadd mediacenter -g 200
sudo usermod -a -G mediacenter sonarr
sudo usermod -a -G mediacenter radarr
sudo usermod -a -G mediacenter lidarr
sudo usermod -a -G mediacenter readarr
sudo usermod -a -G mediacenter mylar
sudo usermod -a -G mediacenter prowlarr
sudo usermod -a -G mediacenter qbittorrent
sudo usermod -a -G mediacenter jackett
sudo usermod -a -G mediacenter overseerr
sudo usermod -a -G mediacenter plex
sudo usermod -a -G mediacenter sabnzbd
sudo usermod -a -G mediacenter jellyseerr
sudo usermod -a -G mediacenter bazarr

# Make directories
sudo mkdir -pv config/{sonarr,radarr,lidarr,readarr,mylar,prowlarr,qbittorrent,jackett,audiobookshelf,overseerr,plex,tautulli,sabnzbd,jellyseerr,bazarr}-config
sudo mkdir -pv data/{torrents,usenet,media}/{tv,movies,music,books,comics,audiobooks,podcasts,audiobookshelf-metadata}

# Set permissions
sudo chmod -R 775 data/
sudo chown -R $(id -u):mediacenter data/
sudo chown -R sonarr:mediacenter config/sonarr-config
sudo chown -R radarr:mediacenter config/radarr-config
sudo chown -R lidarr:mediacenter config/lidarr-config
sudo chown -R readarr:mediacenter config/readarr-config
sudo chown -R mylar:mediacenter config/mylar-config
sudo chown -R prowlarr:mediacenter config/prowlarr-config
sudo chown -R qbittorrent:mediacenter config/qbittorrent-config
sudo chown -R jackett:mediacenter config/jackett-config
sudo chown -R overseerr:mediacenter config/overseerr-config
sudo chown -R plex:mediacenter config/plex-config
sudo chown -R sabnzbd:mediacenter config/sabnzbd-config
sudo chown -R jellyseerr:mediacenter config/jellyseerr-config
sudo chown -R bazarr:mediacenter config/bazarr-config

echo "UID=$(id -u)" >> .env
