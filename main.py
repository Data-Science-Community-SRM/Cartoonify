from keep_alive import keep_alive
import discord
import os
from discord.ext import commands
from PIL import Image
from io import BytesIO
import asyncio
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray
from skimage import img_as_uint
from scipy.signal import convolve2d
client = commands.Bot(command_prefix='$')
kernel_edgedetection = np.array([[-1, -1, -1],
                                 [-1, 8.5, -1],
                                 [-1, -1, -1]])


def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)


@client.command()
async def filter1(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    #pfp=cv2.cvtColor(pfp, cv2.COLOR_BGR2GRAY)
    pfp.save('profile.jpg')
    image = cv2.imread('profile.jpg')
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(
        img_gray_inv, ksize=(21, 21), sigmaX=0, sigmaY=0)
    final = dodgeV2(img_gray, img_blur)
    cv2.imwrite('profile1.jpg', final)
    await ctx.send(file=discord.File('profile1.jpg'))


@client.command()
async def filter2(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    #pfp=cv2.cvtColor(pfp, cv2.COLOR_BGR2GRAY)
    pfp.save('profile.jpg')
    image = cv2.imread('profile.jpg')
    morph_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    final = convolve2d(morph_gray, kernel_edgedetection)

    cv2.imwrite('profile1.jpg', final)
    await ctx.send(file=discord.File('profile1.jpg'))

keep_alive()
client.run(os.getenv('TOKEN'))
