#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = 5231794
    API_HASH = "3e4d1af31d3d3e39c7c9f76e7a787bfd"
    BOT_TOKEN = "6599740105:AAHi0gXbjZzfPo9HeVofhci7aBE0YVfY7KE"

    # Database Credentials

    REDIS_URI = "redis-18955.c1.us-west-2-2.ec2.cloud.redislabs.com:18955"
    REDIS_PASS = "QsBFLM9q9pVRJij1z2LodbKeWspS0aUQ"

    # Channels Ids

    BACKUP_CHANNEL = -1002122884277
    MAIN_CHANNEL = -1002046442610
    LOG_CHANNEL = -1002048310985
    CLOUD_CHANNEL = -1002122884277
    OWNER = 

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/37d9d0657d51e01a71f26.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
