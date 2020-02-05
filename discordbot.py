if not discord.opus.is_loaded(): 
    #もし未ロードだったら
    discord.opus.load_opus("heroku-buildpack-libopus")
