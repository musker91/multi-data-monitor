
"""
name: jobs name
job: cron job lib path and class name
time: cron run time
"""
INTERAVL_CRON_JOBS = [
    {
        "name": "Cherry Swap White Token List New Coin",
        "job": "monitor.new_coin.CherrySwapWhiteTokenList",
        "time": {
            # "seconds": 100
            "minutes": 5
        }
    },
    {
        "name": "KSwap White Token List New Coin",
        "job": "monitor.new_coin.KSwapWhiteTokenList",
        "time": {
            # "seconds": 100
            "minutes": 5
        }
    },
    {
        "name": "Gate.io New Coin Market",
        "job": "monitor.new_coin.GateIoAllMarkets",
        "time": {
            # "seconds": 5
            "minutes": 5
        }
    }
]