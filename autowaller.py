from lxml import html
import urllib
import requests

import random

from datetime import datetime

import os

import sched, time

import argparse


class AutoWaller(object):

    # QuoteFancy website
    WEBSITE = "https://quotefancy.com/"

    def __init__(self):
        # get top categories
        page = urllib.request.urlopen("https://quotefancy.com/").read()
        tree = html.fromstring(page)
        self.topics = tree.xpath('//div[@class="gridblock-title"]/a/@href')[:20]

        # target name of download
        self.image_name = "wallpaper.jpg"

    def get_random_wallpaper(self):
        selected_topic = random.choice(self.topics)
        page = urllib.request.urlopen(selected_topic).read()
        tree = html.fromstring(page)
        imgs = tree.xpath('//div[@class="wallpaper scrollable"]/div/a/@href')

        # go to a random image page
        img_page = random.choice(imgs)
        page = urllib.request.urlopen(img_page).read()
        tree = html.fromstring(page)

        # hacky fix for getting download link as XPath was not able to
        # select the actual '3840x2160' image due to some issues
        download = tree.xpath('//div[@class="frame"]/img/@src')[0].replace(
            '800x450',
            '3840x2160'
        )

        # download the image
        image_response = requests.get(download)
        with open(self.image_name, 'wb') as image:
            image.write(image_response.content)

    def set_wallpaper(self):
        # might have to edit this depending on the environment and OS
        wall_command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri "
        wall_command += os.path.abspath(self.image_name)
        os.system(wall_command)


def change_wallpaper(wall_sched, change_freq):
    aw = AutoWaller()
    aw.get_random_wallpaper()
    aw.set_wallpaper()

    wall_sched.enter(change_freq, 1, change_wallpaper, (wall_sched, change_freq))

if __name__ == "__main__":

    # parse the input arguments
    parser = argparse.ArgumentParser(description="Automatic Wallpaper Changer")
    parser.add_argument(
        '--freq',
        dest="CHANGE_FREQ",
        action='store',
        default=3600,
        type=float,
        help="Interval to change the wallpaper (in seconds)"
    )
    args = parser.parse_args()

    # run scheduler to change in intervals
    wall_sched = sched.scheduler(time.time, time.sleep)
    wall_sched.enter(args.CHANGE_FREQ, 1, change_wallpaper, (wall_sched, args.CHANGE_FREQ))
    wall_sched.run()
    