#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A Python script that drives a Tik Tok lamp.'''

from time import sleep

import board
import neopixel
from TikTokAPI import TikTokAPI


# The TikTok username to track.
USERNAME = 'spaceboyr00'

# Create the TikTok api object.
api = TikTokAPI()


pixels = neopixel.NeoPixel(board.D26,
                           120,
                           auto_write=True,
                           brightness=0.2,
                           pixel_order=neopixel.RGB)

def get_user_follower_count(username):
    '''Get user follower count by name.'''
    # Get the user's current data from TikTok.
    user = api.getUserByName(USERNAME)

    # Return the follower count.
    return user['userInfo']['stats']['followerCount']


# Store for follower counts.
old_follower_count = get_user_follower_count(USERNAME)
follower_count = get_user_follower_count(USERNAME)


while True:
    pixels.fill(0xFF00FF)
    # Store the previous follower count.
    old_follower_count = follower_count

    # Get current follower count.
    follower_count = get_user_follower_count(USERNAME)

    # Check if there are any new followers.
    follower_diff = follower_count - old_follower_count
    if follower_diff > 0:
        # Cycle lights.
        if follower_diff == 1:
            print(f'{follower_diff} new follower.')
        else:
            print(f'{follower_diff} new followers.')

    # Wait to prevent slamming the API.
    sleep(15)
