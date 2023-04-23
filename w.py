import pywhatkit as pwk
phone = str("+2001015678127") 
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+20)
     pwk.sendwhatmsg(phone, "Hi, how are you?", 16, 55)
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")
