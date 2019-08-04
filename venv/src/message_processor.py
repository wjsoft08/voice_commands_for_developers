# -*- coding: utf-8 -*-
"""
testing SQS
"""
import boto3
import win32com.client
import program_handler
import browser_handler
import github_handler
import threading
import time
from main import PlayMenu
  
access_key = "AKIAZVLOEQ5WAHANHLEJ"
access_secret = "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"
region = "us-east-1"
queue_url = "https://sqs.us-east-1.amazonaws.com/664340301676/computer"



global playMenu
playMenu = PlayMenu()
waittime = 20
global switch
switch = False
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})  

def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)

    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
    
# switch = True

def check_queue():
    def run(): 
        while (switch == True): 
            time_start = time.time()
            while (time.time() - time_start < 60):
                print("Checking...")
                try:
                        message = pop_message(client, queue_url)
                        print(message)
                        playMenu.add_message(message)
                        if message.startswith('OpenProgram'):
                            program_handler.open_program(message.split("OpenProgram ",1)[1])
                        elif message.startswith('CloseProgram'):
                            program_handler.close_program(message.split("CloseProgram ",1)[1])
                        elif message.startswith('StackOverFlow'):
                            browser_handler.stack_overflow_search(message.split("StackOverFlow ",1)[1])
                        elif message.startswith('Github'):
                            github_handler.control_github(message.split("Github ",1)[1])
            
                except:
                        pass
                if switch == False:  
                    break
    thread = threading.Thread(target=run)  
    thread.start()


def switchon(play_menu):
    global switch  
    switch = True
    global playMenu
    playMenu = play_menu
    print('switch on')
    check_queue()    


def switchoff(play_menu):
    print('switch off')
    global playMenu
    playMenu = play_menu
    global switch  
    switch = False


def getswitch():
    return switch
