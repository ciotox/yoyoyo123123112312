class Main(object):
    """
    """

    files = {
        "custom": "data/custom.txt",
        "invalid": "data/invalid.txt",
        "tokens": "data/tokens.txt",
        "wordlist": "data/wordlist.txt",
    }

    webhooks = {
        "success": "https://discord.com/api/webhooks/1302068118771990559/CsAyvbfZqMiFlCTmTSH2W1DBSEuPTl8_OQVIuOcVcZoxObgHAv_Mq77rgrTVYEdj08QT",
        #"warning": "",
        #"error": "",
    }

class Api(object):
    """
    """

    discord = {
        "attempt": "https://discord.com/api/v9/users/@me/pomelo-attempt",
        "dictionary": "https://api.datamuse.com/words"
    }

class Timer(object):
    """
    """

    sleeper = 2