# Import web3 library
from tkinter import *
from web3 import Web3

root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Write Import API url
# Copy the API url from Infura and paste it in the 'url' variable
url = "https://mainnet.infura.io/v3/5159ef0311f84be386dea286d1719579"  # Replace with your Infura API URL

# Connect to Web3
web3 = Web3(Web3.HTTPProvider(url))

# Task 02: Calculate and Print the Ethereum value
def ethereum_block():
    number = int(block_entry.get())
    block_data = web3.eth.get_block(number)
    
    if block_data and 'transactions' in block_data and len(block_data['transactions']) > 0:
        transaction = web3.eth.get_transaction(block_data['transactions'][-1])
        Value = transaction['value']
        value_in_ether = Value / 10**18
        # Get current Ethereum value in dollars by searching "1 eth in dollar" on the web
        value_in_dollar = value_in_ether * 1796  # Replace CURRENT_ETH_TO_USD_VALUE with the actual value

        gas = transaction['gas']

        # Update labels with the calculated values
        gasused_info_label["text"] = "Value: $" + str(value_in_dollar)
        gaslimit_info_label["text"] = "Gas: " + str(gas)
    else:
        gasused_info_label["text"] = "No transactions in this block."
        gaslimit_info_label["text"] = ""

    block_entry.destroy()
    search_btn.destroy()

search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()
