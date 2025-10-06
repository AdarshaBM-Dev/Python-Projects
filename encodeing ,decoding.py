import base64

message = "I Love You"
message_in_bytes = bytes(message,"utf-8")
encoded_message = base64.b64encode(message_in_bytes)
print(encoded_message)
message2 = "SSBMb3ZlIFlvdQ=="
message2_in_bytes = bytes(message2,"utf-8")
decoded_message = base64.b64decode(message2_in_bytes)

print(f"EnCoded: {encoded_message} DeCoded: {decoded_message}")

#user side
import base64
def decoder():
    message = input("Message to be decoded >> ")
    message_in_bytes = bytes(message,"utf-8")
    decoded_message = base64.b64decode(message_in_bytes)
    print(f"Decoded: {decoded_message}")
    
def encoder():
    message = input("Message to be encoded >> ")
    message_in_bytes = bytes(message,"utf-8")
    encoded_message = base64.b64encode(message_in_bytes)
    print(f"Encoded: {encoded_message}")
print("python Decoder and Ender")

print("1. Encoder")
print("2. Decoder")

option = int(input("select option (1/2) >> "))

if option==1:
    encoder()
elif option==2:
    decoder()
else:
    print("Eorror! Try Again")

