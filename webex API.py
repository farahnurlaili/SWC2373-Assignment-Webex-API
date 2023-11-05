
#NGYxMGQ2MzctZDVjNC00MDQ5LWEyNjctNDE4Zjk3OTY1Y2JjNWExMmFlZjktOGFi_P0A1_346e751c-7bdb-491d-9858-1355bbf861ac

#import necessary libraries
import requests
import json

#function "0" to test the connection
def test_connection(access_token):
    #define the url for fetching the user information
    url = 'https://webexapis.com/v1/people/me'
    #set the headers
    headers ={
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    #send a GET requests to Webex server
    res = requests.get(url, headers=headers)

    #check the response status code
    if res.status_code == 200:
        print("\t\t\t\t\t\t\t\t\tCongrats! Connection to Webex server is successful.")
    else:
        print("\t\t\t\t\t\tSorry, Connection to Webex server failed. Please quit the modeule and try again")
    
#function "1" to display user information
def display_user_info(access_token):
    #define the url for fetching the user information
    url = 'https://webexapis.com/v1/people/me'
    #set the headers
    headers ={
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    #send a GET requests to Webex server
    res = requests.get(url, headers=headers)

    #check the response status code
    if res.status_code == 200:
        user_info = res.json()
        print("\t\t\t\t\t\t\t\t\t\t\tUSER INFORMATION")
        print()
        print(f"\t\t\t\t\t\t\t\t\t\tUser Displayed name: {user_info['displayName']}")
        print(f"\t\t\t\t\t\t\t\t\t\tUser Nickname: {user_info['nickName']}")
        print(f"\t\t\t\t\t\t\t\t\t\tUser email: {', '.join(user_info['emails'])}")
    else:
        print("\t\t\t\t\t\t\t\t\tUnable to retrieve information.")

#function "2" to list rooms
def list_room(access_token):
    #define the url for fetching list of rooms
    url = 'https://webexapis.com/v1/rooms'
    #set the headers
    headers ={
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    #define parameters to limit the num of rooms to 5
    params = {'max': 5}
    #send a GET requests to Webex server
    res = requests.get(url, headers=headers, params=params)

    #check the response status code
    if res.status_code == 200:
        room_info = res.json()
        print("\t\t\t\t\t\t\t\t\t\t\tROOM INFORMATION")
        print()
        for room in room_info['items']:
            print(f"\t\t\t\t\t\tRoom ID: {room['id']}")
            print(f"\t\t\t\t\t\tRoom Title: {room['title']}")
            print(f"\t\t\t\t\t\tDate Created: {room['created']}")
            print(f"\t\t\t\t\t\tLast Activity: {room['lastActivity']}")
            print()
    else:
        print("\t\t\t\t\t\t\t\t\t\tFailed to display list rooms.")

#function "3" to create room
def create_room(access_token):
    #define the url for creating a new room
    url = 'https://webexapis.com/v1/rooms'
    #set the headers
    headers ={
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    print()
    room_name = input("\t\t\t\t\t\t\t\t\tEnter the title for the new room: ")
    #define the data to be sent in the POST requests
    data = {'title' : room_name}
    #send a POST requests to create new room
    res = requests.post(url, headers=headers, json=data)
    
    #check the response status code
    if res.status_code == 200:
        print(f"\t\t\t\t\t\t\t\t\tRoom '{room_name}' has successfully created!")
        print("\t\t\t\t\t\t\t\t\tPlease check your Webex Development Teams.")
    else:
        print("\t\t\t\t\t\t\t\t\tFailed to create the room.")

# Function "4" to send a message to desired rooms
def send_message(access_token):
    #define the url for fetching the list rooms
    url = 'https://webexapis.com/v1/rooms'
    #set the headers
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    #define parameters to limit the num of rooms to 5
    params = {'max': 5}
    #send a GET requests to Webex server
    response = requests.get(url, headers=headers, params=params)

    #check the response status code
    if response.status_code == 200:
        room_info = response.json()
        print()
        print("\t\t\t\t\t\t\t\t\t\t\tROOMS")
        
        #display a numbered list of rooms
        for i, room in enumerate(room_info['items']):
            print(f"({i + 1}) {room['title']}")

        #ask the user to choose a room to t=send the message
        room_choice = int(input("\t\t\t\t\t\t\t\t\tChoose a room to send a message (1-5): ")) - 1
        
        if 0 <= room_choice < len(room_info['items']):
            room_id = room_info['items'][room_choice]['id']
            room_name = room_info['items'][room_choice]['title']

            #ask the user to enter the message to be sent
            message = input("\t\t\t\t\t\t\t\t\tEnter the message you want to send: ")
            url = 'https://webexapis.com/v1/messages'

            #define the data to be sent in the POST requests
            data = {'roomId': room_id, 'markdown': message}
            response = requests.post(url, headers=headers, json=data)

            #check the response status code 
            if response.status_code == 200:
                print(f"\t\t\t\t\t\t\t\t\tMessage '{message}' sent successfully to room '{room_name}'")
            else:
                print("\t\t\t\t\t\t\t\t\t\t\tFailed to send the message.")
    else:
        print("\t\t\t\t\t\t\t\t\tFailed to list rooms.")


print("-" * 184)
access_token = input("\t\tPlease enter your Webex token number: ")
print("-" * 184)

while True:
    print(" " * 100)
    print("-" * 184)
    print("\t\t\t\t\t\t\t\t\t\t\tMENU OPTIONS")
    print("-" * 184)
    print("\t\t\t\t\t\t\t\t\t\tOption (0): Test Connection")
    print("\t\t\t\t\t\t\t\t\t\tOption (1): Display Information")
    print("\t\t\t\t\t\t\t\t\t\tOption (2): List Rooms")
    print("\t\t\t\t\t\t\t\t\t\tOption (3): Create Room")
    print("\t\t\t\t\t\t\t\t\t\tOption (4): Send Message to a Room")
    print("\t\t\t\t\t\t\t\t\t\tOption (5): Quit")
    print("-" * 184)
    print(" " * 100)
    print()
    print("-" * 184)

    option = input("\t\t\t\t\t\t\t\t\tPlease enter your options(0/1/2/3/4/5):")
    print("-" * 184)
    print()

    if option == "0":
        test_connection(access_token)
        print(" " * 100)
        print("-" * 184)
        input("\t\t\t\t\t\t\t\t\t\tPlease Enter to return to the menu.")
        print("-" * 184)
        
    elif option == "1":
        display_user_info(access_token)
        print(" " * 100)
        print("-" * 184)
        input("\t\t\t\t\t\t\t\t\t\tPlease Enter to return to the menu.")
        print("-" * 184)
        
    elif option == "2":
        list_room(access_token)
        print(" " * 100)
        print("-" * 184)
        input("\t\t\t\t\t\t\t\t\t\tPlease Enter to return to the menu.")
        print("-" * 184)
        
    elif option == "3":
        create_room(access_token)
        print(" " * 100)
        print("-" * 184)
        input("\t\t\t\t\t\t\t\t\tPlease Enter to return to the menu.")
        print("-" * 184)
        
    elif option == "4":
        send_message(access_token)
        print(" " * 100)
        print("-" * 184)
        input("\t\t\t\t\t\t\t\t\t\tPlease Enter to return to the menu.")
        print("-" * 170)
        
    elif option == "5":
        print(" " * 100)
        input("\t\t\t\t\t\t\t\t\t\tGoodbye!")
        break
    else:
        print(" " * 100)
        print("\t\t\t\t\t\t\tInvalid choice. Please select a valid option (0/1/2/3/4/5).")
