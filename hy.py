from firebase import firebase


firebase = firebase.FirebaseApplication('https://hand-sign-27230-default-rtdb.firebaseio.com/', None)

result = firebase.put('/handsign','c',None)
print(result)