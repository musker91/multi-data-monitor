
"""
name: jobs name

"""
INTERAVL_CRON_JOBS = [
    {
        "name": "Gate.io New Coin",
        "job": "monitor.new_coin.GateNewCoin",
        "time": {
            "seconds": 10
        }
    }
]