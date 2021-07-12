# algoPyCreateAccount
Algorand Blockchain using Python and PureStake API service for querying account balance and sending algo from one account to another. On **TESTNET**.

Inspired by original tutorial here: https://developer.algorand.org/tutorials/creating-python-transaction-purestake-api/

and here: https://www.purestake.com/blog/algorand-python-sdk/

and here: https://developer.purestake.io/code-samples


## Install Python 3
Go here and install python 3.9.x for Win, Mac or Linux here: 
https://www.python.org/downloads/

## Install miniconda
Go here and install miniconda 3.9.x for Win, Mac or Linux here: 
https://docs.conda.io/en/latest/miniconda.html

Can be done other ways but it can be a can of worms.  Google is your friend. Use it!.

## Setting Python Path
Setting path is tricky but doable as above section.
```bash
# Mac, Linux
export PATH=”$PATH:/usr/local/bin/python”
```

Windows 10 is more complicated.

- Go into "Run" prompt and enter "**sysdm.cpl**"
- This should open up the **System Properties** window. Go to the **Advanced** tab and click the **Environment Variables** button.
- In the **System variable** window, find the **Path** variable and click **Edit**:
- Position your cursor at the end of the **Variable** **value** line and add the path to the **python.exe** file, preceded with the semicolon character (**;**). 
- Example:
  -  **;C:\Python\Python39**


## Deposit Algo into existing accounts
See create accounts https://deephomebrew.com/2021/06/30/project-blockchain-algorand-tutorial-1-create-account/

To fund accounts on TestNet go here for free algos (fake monies to work on the algorand blockchain): https://bank.testnet.algorand.network/

*Note these are TestNet Accounts so private and public key are not so important. Only for demonstration purposes ONLY!


## Create a PureStake API Account
Register for a free account at https://developer.purestake.io/


## Follow Prompts
Go thru all the prompts and save your API key for later reference.


## Change to Target Directory
Where u want to put the project directory and its files.
```bash
# Mac, Linux and Windows
cd <your target dir>
```


## Clone Repo
Copy the code.
```bash
# Mac, Linux and Windows
git clone https://github.com/csalinasonline/algoPyTxPureStakeApi.git
```

## Change to Repo Directory
```bash
# Mac, Linux and Windows
cd algoPyTxPureStakeApi
```

## Activating a Virtual Environment
Close current terminal.
Change directory to '../algoPyTxPureStakeApi'

Turn on the sandbox.
```bash
# Mac, Linux and Windows
conda create -n algoPyTxPureStakeApi python=3.9

# activate environment
conda activate algoPyTxPureStakeApi
```

## Run Pip
Install dependencies.
```bash
# Mac, Linux and Windows
pip install -r requirements.txt
```

## Run program
Finally run the program.
```bash
# Mac, Linux and Windows
python main.py
```
If all went well we should see on the console a transaction of 1 micro algo to another account.

```bash
Sending 1 microalgo from 2DH43BSEWVQZ2XSVKWFMS5SGFDHV5EBXDSFCQHCODCPXJYIOGL7WEOID6I to OLOCVXHXMOLOV4BN2FHXS23S46UWJIKFDVZJ2WL3KOSX3JFRMTJWYW2OIY...Done.

Sent 1 microalgo in transaction: LQ3Q7OAZA6PPWSV6ANJBISVZIRFTE4STDDKJRCSN6BTO7Q5G7QCQ

Resulting balances
2DH43BSEWVQZ2XSVKWFMS5SGFDHV5EBXDSFCQHCODCPXJYIOGL7WEOID6I: 9992993 microalgo
OLOCVXHXMOLOV4BN2FHXS23S46UWJIKFDVZJ2WL3KOSX3JFRMTJWYW2OIY: 10000007 microalgo
```

## Deactivating the Virtual Environment
Turn off sandbox.
```bash
conda deactivate
```