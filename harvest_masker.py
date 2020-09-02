from PIL import Image, ImageDraw
import glob
import os
mask=Image.open("data/sentinel-2a-tile-7680x-10240y/masks/sugarcane-region-mask.png")
arr= os.listdir("data/sentinel-2a-tile-7680x-10240y/timeseries")
for k in arr:
    if "TCI" in k:
        tile= Image.open("data/sentinel-2a-tile-7680x-10240y/timeseries/"+k)
        date=k[15:25]
        pixels=tile.load()
        overlay=mask.load()
        for y in range(512):
            for x in range(512):
                if overlay[y,x]==(0, 0, 0, 255):
                    red=pixels[y,x][0]
                    green=pixels[y,x][1]
                    blue=pixels[y,x][2]
                    channelPortion=(green/(green+red+blue))
                    if channelPortion <0.32:
                        pixels[y,x]=(255,0,0)
        tile.save("data/harvested/"+date+".png")
