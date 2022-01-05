########################
# AUTHOR: slurpxbt
# api reference: https://synapse.dorime.org/#overview
########################

import requests
import datetime as dt

server = "https://synapse.dorime.org"

# ------------------------------------------------
# Bridge volume
# ------------------------------------------------
def get_chain_usd_volume():

    endpoint = f"{server}/api/v1/analytics/volume/total"
    data = requests.get(endpoint)
    if data.status_code == 200:
        return data.json()["data"]
    else:
        print("request failed")


def get_chain_total_tx():

    endpoint = f"{server}/api/v1/analytics/volume/total/tx_count"
    data = requests.get(endpoint)
    if data.status_code == 200:
        return data.json()["data"]
    else:
        print("request failed")


def get_token_volume_by_direction_and_chain(chain:str, token:str, direction:str):

    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora
    token: Allowed: nusd ┃ syn
    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    token = token.lower()
    direction = direction.lower()

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    tokens = ["nusd", "syn"]
    directions = ["in", "out"]

    params_ok = False
    if chain in chains and token in tokens and direction in directions:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/volume/{chain}/filter/{token}/{direction}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()["data"]
        else:
            print("request failed")
    else:
        print("wrong parameters")


def get_all_token_volume_by_direction(chain:str, direction:str):

    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    direction = direction.lower()

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    directions = ["in", "out"]

    params_ok = False
    if chain in chains and direction in directions:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/volume/{chain}/{direction}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()["data"]
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Bridge Pools
# ------------------------------------------------
def get_virtual_price_of_pool_for_chain(chain:str):

    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/pools/price/virtual/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")


def get_virtual_price_of_pool_for_all_chains():

    endpoint = f"{server}/api/v1/analytics/pools/price/virtual"
    data = requests.get(endpoint)
    if data.status_code == 200:
        return data.json()
    else:
        print("request failed")


def get_swap_volume_and_fees_for_pool_on_chain(chain:str, pool:str):
    """
   chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

   direction: Allowed: in ┃ out
   """

    chain = chain.lower()
    pool = pool.lower()

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    pools = ["nusd", "neth"]

    params_ok = False
    if chain in chains and pool in pools:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/pools/volume/{chain}/{pool}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Emissions
# ------------------------------------------------
def get_wkly_syn_emissions_on_all_chains():

    endpoint = f"{server}/api/v1/analytics/emissions/weekly"
    data = requests.get(endpoint)
    if data.status_code == 200:
        return data.json()
    else:
        print("request failed")


def get_wkly_syn_emissions_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/emissions/weekly/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Admin Fees
# ------------------------------------------------
def get_admin_fees_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/admin/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")


def get_pending_admin_fees_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/admin/{chain}/pending"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Airdrop
# ------------------------------------------------
def get_airdrop_amount_given_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/airdrop/{chain}/"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()["data"]
        else:
            print("request failed")
    else:
        print("wrong parameters")


def get_airdrop_amount_given_on_chain_by_token(chain:str, token:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora
    token: Allowed: nusd ┃ syn
    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    token = token.lower()

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    tokens = ["nusd", "syn"]

    params_ok = False
    if chain in chains and token in tokens:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/airdrop/{chain}/{token}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()["data"]
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Bridge Fees
# ------------------------------------------------
def get_bridge_fees_on_chain_by_token(chain:str, token:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora
    token: Allowed: nusd ┃ syn
    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    token = token.lower()

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    tokens = ["nusd", "syn"]

    params_ok = False
    if chain in chains and token in tokens:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/bridge/{chain}/{token}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()["data"]
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Validator Gas Fees
# ------------------------------------------------
def get_validator_gas_fees_paid_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/validator/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")


def get_validator_gas_fees_paid_for_token_on_chain(chain:str, token:str):
    """
   chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora
   token: Allowed: nusd ┃ syn
   direction: Allowed: in ┃ out
   """

    chain = chain.lower()
    token = token.lower()

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    tokens = ["nusd", "syn"]

    params_ok = False
    if chain in chains and token in tokens:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/fees/validator/{chain}/{token}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Treasury Balance
# ------------------------------------------------
def get_treasury_balance_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/analytics/treasury/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Circulating supply
# ------------------------------------------------
def get_circ_supply_for_all_chains():

    endpoint = f"{server}/api/v1/circ/"
    data = requests.get(endpoint)
    if data.status_code == 200:
        return data.json()
    else:
        print("request failed")


def get_circ_supply_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/circ/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Market Cap
# ------------------------------------------------
def get_market_cap_for_all_chains():

    endpoint = f"{server}/api/v1/mcap/"
    data = requests.get(endpoint)
    if data.status_code == 200:
        return data.json()
    else:
        print("request failed")


def get_market_cap_on_chain(chain:str):
    """
    chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora

    direction: Allowed: in ┃ out
    """

    chain = chain.lower()
    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/mcap/{chain}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

# ------------------------------------------------
# Utils
# ------------------------------------------------
def get_chain_block_from_date(chain:str, date:dt):
    """
   chain: Allowed: ethereum ┃ avalanche ┃ bsc ┃ polygon ┃ arbitrum ┃ fantom ┃ harmony ┃ boba ┃ optimism ┃ moonriver ┃ aurora
   token: Allowed: nusd ┃ syn
   direction: Allowed: in ┃ out
   """

    chain = chain.lower()

    year = f"{date.year}"
    month = f"{date.month}"
    if date.month < 10:
        month = f"0{date.month}"

    day = f"{date.day}"
    if date.day < 10:
        day = f"0{date.day}"

    date = f"{year}-{month}-{day}"

    chains = ["ethereum", "avalanche", "bsc", "polygon", "arbitrum", "fantom", "harmony", "boba", "optimism", "moonriver", "aurora"]
    tokens = ["nusd", "syn"]

    params_ok = False
    if chain in chains:
        params_ok = True

    if params_ok:
        endpoint = f"{server}/api/v1/utils/date2block/{chain}/{date}"
        data = requests.get(endpoint)
        if data.status_code == 200:
            return data.json()
        else:
            print("request failed")
    else:
        print("wrong parameters")

