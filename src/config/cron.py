
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
            "minutes": 15
        }
    }
]