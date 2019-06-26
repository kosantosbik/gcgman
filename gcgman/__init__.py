#!/usr/bin/env python3
name = "gcgman"

import datetime
import os
from time import sleep
from tqdm import tqdm

OFFSET_VALUE = 42
LETTERS = {
    'A': [7,8,9,10,11,12,13,14,17,21,24,28,29,30,31,32,33,34],
    'B': [7,8,9,10,11,12,13,14,17,20,21,24,27,29,30,32,33],
    'C': [8,9,10,11,12,14,20,21,27,28,34],
    'D': [7,8,9,10,11,12,13,14,20,21,27,29,30,31,32,33],
    'E': [7,8,9,10,11,12,13,14,17,20,21,24,27,28,31,34],
    'F': [7,8,9,10,11,12,13,14,17,21,24,28],
    'G': [1,2,3,4,5,7,13,14,17,20,21,24,27,28,31,32,33],
    'H': [7,8,9,10,11,12,13,17,24,28,29,30,31,32,33,34],
    'I': [0,6,7,13,14,15,16,17,18,19,20,21,27,28,34],
    'J': [0,5,7,13,14,15,16,17,18,19,20,21,28],
    'K': [7,8,9,10,11,12,13,16,17,22,25,26,28,34],
    'L': [7,8,9,10,11,12,13,20,27,34],
    'M': [0,1,2,3,4,5,6,8,16,22,28,29,30,31,32,33,34],
    'N': [0,1,2,3,4,5,6,7,8,16,17,25,26,28,29,30,31,32,33,34],
    'O': [1,2,3,4,7,12,14,19,21,26,29,30,31,32],
    'P': [7,8,9,10,11,12,13,14,17,21,24,28,29,30,31],
    'R': [7,8,9,10,11,12,13,14,17,18,21,24,26,28,29,30,31,34],
    'S': [0,1,2,3,6,7,10,13,14,17,20,21,24,27,28,31,32,33,34],
    'T': [0,7,14,15,16,17,18,19,20,21,28],
    'U': [0,1,2,3,4,5,13,20,27,28,29,30,31,32,33],
    'V': [0,1,2,10,11,12,20,24,25,26,28,29,30],
    'Y': [0,1,8,9,16,17,18,19,20,22,23,28,29],
    'Z': [0,6,7,12,13,14,17,18,20,21,23,24,27,28,29,34],
    'X': [0,6,8,9,11,12,17,22,23,25,26,28,34],
    'W': [0,1,2,3,4,5,13,16,17,18,19,27,28,29,30,31,32,33],
    'Q': [1,2,3,4,7,12,14,19,21,26,29,30,31,32,33,41],
    'space': [],
    1: [9,13,15,20,21,22,23,24,25,26,27,34],
    2: [8,9,12,13,14,18,20,21,24,27,29,30,34],
    3: [8,12,14,20,21,24,27,29,30,32,33],
    4: [10,11,16,18,22,25,28,29,30,31,32,33,34,39],
    5: [7,8,9,10,13,14,17,20,21,24,27,28,32,33],
    6: [7,8,9,10,11,12,13,14,17,20,21,24,27,28,31,32,33,34],
    7: [7,13,14,18,19,21,24,28,29,30],
    8: [7,8,9,10,11,12,13,14,17,20,21,24,27,28,29,30,31,32,33,34],
    9: [7,8,9,10,13,14,17,20,21,24,27,28,29,30,31,32,33,34],
    0: [7,8,9,10,11,12,13,14,20,21,27,28,29,30,31,32,33,34]
}

def get_weekday(dtime):
    weekday = dtime.weekday()
    if weekday == 6:
        return 0
    else:
        return weekday+1

def get_start_date(year):
    if year:
        year_start = datetime.datetime(year=year, month=1, day=1)
        weekday = get_weekday(year_start)
        start_date = year_start - datetime.timedelta(days=weekday)
    else:
        now = datetime.datetime.now()
        week_start = now - datetime.timedelta(days=get_weekday(now))
        start_date = week_start - datetime.timedelta(days=52*7)

    return start_date

def get_word_offsets(word):
    global OFFSET_VALUE
    global LETTERS
    commit_offsets = []
    offset = 0

    word = word.upper()
    for letter in word:
        if letter == ' ':
            letter_vals = LETTERS['space']
        else:
            letter_vals = LETTERS[letter]
        for pixel in letter_vals:
            commit_offsets.append(14+OFFSET_VALUE*offset+pixel)

        offset += 1

    return commit_offsets

def create_commit(timestamp, count):
    for i in range(count):
        command = 'git commit --date ' + timestamp + ' --allow-empty --allow-empty-message -m "" > /dev/null 2>&1'
        os.system(command)

def gcgman(word, count, year):
    start_date = get_start_date(year)
    commit_offsets = get_word_offsets(word)
    print("Generating commits...")

    for offset in tqdm(commit_offsets):
        commit_date = start_date + datetime.timedelta(days=offset)
        commit_timestamp = str(int(commit_date.timestamp()))
        create_commit(commit_timestamp, count)

    print("\nGenerated {} commits.".format(count * len(commit_offsets)))
