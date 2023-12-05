from tkinter import *
from web3 import Web3

# Task 1: Define the ethereum_block function
def ethereum_block():
    wei_price = web3.eth.gas_price
    gwei_price = wei_price / 10**9
    gas_price_in_ether = gwei_price / 10**9

    # Task 2: Convert gas price to different currencies
    ether_to_dollar = 4500  # Replace with the current value of 1 ETH in dollars
    ether_to_rupees = 60000  # Replace with the current value of 1 ETH in Indian Rupees
    ether_to_pounds = 3500  # Replace with the current value of 1 ETH in Pounds

    gas_price_in_dollar = gas_price_in_ether * ether_to_dollar
    gas_price_in_rupees = gas_price_in_ether * ether_to_rupees
    gas_price_in_pounds = gas_price_in_ether * ether_to_pounds

    # Task 3: Display the prices in the application
    value_in_ether["text"] = "Value of gas in Ether: ETH " + str(gas_price_in_ether)
    value_in_dollar["text"] = "Value of gas in Dollar: $ " + str(gas_price_in_dollar)
    value_in_rupees["text"] = "Value of gas in Rupees: ₹ " + str(gas_price_in_rupees)  # Use the Indian Rupee symbol
    value_in_pounds["text"] = "Value of gas in Pounds: £ " + str(gas_price_in_pounds)  # Use the Pound symbol

root = Tk()
root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)

value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)

value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.48, anchor=CENTER)

value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.58, anchor=CENTER)

value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.68, anchor=CENTER)

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)

root.mainloop()