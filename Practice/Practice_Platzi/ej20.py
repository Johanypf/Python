# Input:

# messages = [
#   {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
#   {'sender': 'Bob', 'content': '¡Bien, gracias!'},
#   {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
#   {'sender': 'Charlie', 'content': 'Hola a todos.'},
#   {'sender': 'Alice', 'content': 'Nos vemos luego.'}
# ]

# user = 'Alice'
# filter_user_messages(messages, user)

# Output:

# [
#   {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
#   {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
#   {'sender': 'Alice', 'content': 'Nos vemos luego.'}
# ]


messages = [ {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
            {'sender': 'Bob', 'content': '¡Bien, gracias!'},
   {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},]

user = 'Alice'
# messages_out = []
# for z in messages:
#     for x in z.values():
#         if x == user:
#             messages_out.append(z)

# print(messages_out)

# def check_sender(messages1,sender):
#     messages_out1 = []


#     for s in messages1:
#        if sender in s.values():
#             messages_out1.append(s)
#     return(messages_out1)



def filter_user_messages(messages, sender):
    return list(filter( lambda s: sender in s.values(),messages))



print(filter_user_messages(messages,user))

