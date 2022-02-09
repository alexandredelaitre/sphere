import discord
import pickle
import guard
client=discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("£help"):
        await message.channel.send("```Hello! My commands include!:\n1. £getwallet - initialise your wallet with 30 coins\n2. £claim you can get 30 free credits to play around with!!\n3. £send <user address> <amount>\n4. £hint \nFeel free to donate to my address <3 0x330823330825240577```")
    if message.content.startswith("£hint"):
        await message.channel.send("```I feel bad if you donate too much, so please don't <3, but if you're curious then you can find the sourcecode here!```")
    if message.content.startswith("£getwallet"):
        currentUser=str(message.author.id)
        accounts=pickle.load(open("accounts.p","rb"))
        if "0x"+currentUser in accounts:
            await message.channel.send("You already have a registered wallet")
        else:
            walletAddress="0x"+currentUser
            accounts[walletAddress]=[30,0] #num of coins, number of transactions
            pickle.dump(accounts, open( "accounts.p", "wb" ))
            await message.reply("Your wallet has been created! Your wallet address is "+walletAddress+" use £info for more stats")

    if message.content.startswith("£info"):    
        currentUser=str(message.author.id)
        accounts=pickle.load(open("accounts.p","rb"))
        if "0x"+currentUser in accounts:
            walletAddress="0x"+currentUser
            value,transactionNum=accounts[walletAddress]
            await message.reply("You have "+str(value)+" coins and "+str(transactionNum)+" transactions. Your address is "+walletAddress)
        else:
            await message.reply("You do not have a current account....")

    if message.content.startswith("£send "): 
        otherPerson, amount=message.content.split("£send ")[1].strip().split(" ")
        try:
            currentUser=str(message.author.id)
            if message.content.split("£send ")[2]=="0x"+currentUser:
                await message.reply(guard.stoprepeat)

            
        except Exception as e :
            print(e)
        currentUser=str(message.author.id)
        accounts=pickle.load(open("accounts.p","rb"))
        if "0x"+currentUser in accounts:
            walletAddress="0x"+currentUser

            if accounts[walletAddress][0]>=float(amount):

                accounts[walletAddress][0]-=float(amount)
                accounts[otherPerson][0]+=float(amount)
                accounts[walletAddress][1]+=1
                pickle.dump(accounts, open( "accounts.p", "wb" ))


    if message.content.startswith("£claim"):
        currentUser=str(message.author.id)
        accounts=pickle.load(open("accounts.p","rb"))
        if "0x"+currentUser in accounts:
            walletAddress="0x"+currentUser
            accounts[walletAddress][0]+=30.0
            pickle.dump(accounts, open( "accounts.p", "wb" ))
    