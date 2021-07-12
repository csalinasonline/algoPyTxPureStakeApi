# ******************************************************************************
# Project               :   algoPyTxPureStakeApi
# Filename              :   main.py
# Author                :   csali
# Origin Date           :   7/11/2021 
# License               :   MIT
# Notes                 :   Algorand Blockchain using Python and PureStake 
# API service for querying account balance and sending algo from one account 
# to another.
# 
# Inspired by original tutorial here: 
# https://developer.algorand.org/tutorials/creating-python
# -transaction-purestake-api/
#
# and here: https://www.purestake.com/blog/algorand-python-sdk/
#
# and here: https://developer.purestake.io/code-samples
# ******************************************************************************

from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk import transaction

def main():
    """
    Main hook

    """

    # fund these 2 accounts with some initial algo via the dispenser:
    # https://bank.testnet.algorand.network/
    # address a: 2DH43BSEWVQZ2XSVKWFMS5SGFDHV5EBXDSFCQHCODCPXJYIOGL7WEOID6I
    # address b: OLOCVXHXMOLOV4BN2FHXS23S46UWJIKFDVZJ2WL3KOSX3JFRMTJWYW2OIY
    mnemonic_secret = "swarm transfer border digital gather wage blouse knee frozen cart taxi balance festival helmet radio ill bicycle notice fade hungry stomach shiver kidney abstract bronze"
    account_a_private_key = mnemonic.to_private_key(mnemonic_secret)
    account_a = mnemonic.to_public_key(mnemonic_secret)
    account_b = 'OLOCVXHXMOLOV4BN2FHXS23S46UWJIKFDVZJ2WL3KOSX3JFRMTJWYW2OIY'
    
    # Setup client with PureStake key
    # purestake_key = 'INSERT YOUR PURESTAKE API KEY HERE'
    endpoint_address = 'https://testnet-algorand.api.purestake.io/ps2'
    purestake_header = {'X-Api-key': algod_token }
    algod_client  = algod.AlgodClient(algod_token, endpoint_address, headers=purestake_header)

    # get suggested parameters
    params = algod_client.suggested_params()
    gen = params.gen
    gh = params.gh
    first_valid_round = params.first
    last_valid_round = params.last
    tx_fee = params.min_fee
    send_amount = 1

    #
    send_to_address = account_b    

    # Create and sign transaction
    tx = transaction.PaymentTxn(account_a, tx_fee, first_valid_round, last_valid_round, gh, send_to_address, send_amount, flat_fee=True)
    signed_tx = tx.sign(account_a_private_key)

    try:
        # Send the transaction
        print("Sending " + str(send_amount) + " microalgo from " + account_a + " to " + account_b + "...", end='', flush=True)
        # note that the PureStake api requires the content type for the following call to be set to application/x-binary
        tx_confirm = algod_client.send_transaction(signed_tx)
        algod_client.status_after_block(first_valid_round + 2) # wait 2 blocks to make sure our tx has been committed

        print("Done.")
        print("Sent " + str(send_amount) + " microalgo in transaction: " + str(tx_confirm))
        print("")

        # Query resulting balances
        result_a = algod_client.account_info(account_a)
        result_b = algod_client.account_info(account_b)

        print("Resulting balances")
        print(result_a["address"] + ": " + str(result_a["amount"]) + " microalgo")
        print(result_b["address"] + ": " + str(result_b["amount"]) + " microalgo")

    except Exception as e:
        print(e)    

if __name__ == "__main__":
    main()
