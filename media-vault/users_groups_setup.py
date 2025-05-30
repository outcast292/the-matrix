import os


class UserGroupSetup:
    def __init__(self, root_dir='/'):
        self.root_dir = root_dir
        os.system('sudo groupadd mediacenter -g 200')

    def create_config_dir(self, service_name):
        os.system(
            f'sudo mkdir -p {self.root_dir}/config/{service_name}-config'
            f' ; sudo chown -R {service_name}:mediacenter {self.root_dir}/config/{service_name}-config'
            f' ; sudo chown $(id -u):mediacenter {self.root_dir}/config'
        )

    def sonarr(self):
        os.system(
            '/bin/bash -c "sudo useradd sonarr -u 201'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/tv -m 775'
            ' ; sudo chown -R sonarr:mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}/tv'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('sonarr')
        os.system('sudo usermod -a -G mediacenter sonarr')

    def radarr(self):
        os.system(
            '/bin/bash -c "sudo useradd radarr -u 202'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/movies -m 775'
            ' ; sudo chown -R radarr:mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}/movies'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('radarr')
        os.system('sudo usermod -a -G mediacenter radarr')

    def bazarr(self):
        os.system('/bin/bash -c "sudo useradd bazarr -u 213"')
        self.create_config_dir('bazarr')
        os.system('sudo usermod -a -G mediacenter bazarr')

    def lidarr(self):
        os.system(
            '/bin/bash -c "sudo useradd lidarr -u 203'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/music -m 775'
            ' ; sudo chown -R lidarr:mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}/music'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('lidarr')
        os.system('sudo usermod -a -G mediacenter lidarr')

    def readarr(self):
        os.system(
            '/bin/bash -c "sudo useradd readarr -u 204'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/books -m 775'
            ' ; sudo chown -R readarr:mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}/books'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('readarr')
        os.system('sudo usermod -a -G mediacenter readarr')

    def mylar3(self):
        os.system(
            '/bin/bash -c "sudo useradd mylar -u 205'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/comics -m 775'
            ' ; sudo chown -R mylar:mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}/comics'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('mylar')
        os.system('sudo usermod -a -G mediacenter mylar')

    def audiobookshelf(self):
        os.system(
            '/bin/bash -c "sudo useradd audiobookshelf -u 209'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/audiobooks -m 775'
            ' ; sudo chown -R audiobookshelf:mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}/audiobooks'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):mediacenter ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('audiobookshelf')
        os.system('sudo usermod -a -G mediacenter audiobookshelf')

    def prowlarr(self):
        os.system('sudo useradd prowlarr -u 206')
        self.create_config_dir('prowlarr')
        os.system('sudo usermod -a -G mediacenter prowlarr')

    def qbittorrent(self):
        os.system('sudo useradd qbittorrent -u 207')
        os.system('sudo usermod -a -G mediacenter qbittorrent')

    def overseerr(self):
        os.system('sudo useradd overseerr -u 209')
        self.create_config_dir('overseerr')
        os.system('sudo usermod -a -G mediacenter overseerr')

    def plex(self):
        os.system('sudo useradd plex -u 210')
        self.create_config_dir('plex')
        os.system('sudo usermod -a -G mediacenter plex')

    def sabnzbd(self):
        os.system('sudo useradd sabnzbd -u 211')
        self.create_config_dir('sabnzbd')
        os.system('sudo usermod -a -G mediacenter sabnzbd')

    def jellyseerr(self):
        os.system('sudo useradd jellyseerr -u 212')
        self.create_config_dir('jellyseerr')
        os.system('sudo usermod -a -G mediacenter jellyseerr')

    def maintainerr(self):
        os.system('sudo useradd maintainerr -u 214')
        self.create_config_dir('maintainerr')
        os.system('sudo usermod -a -G mediacenter maintainerr')
