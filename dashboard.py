# get firebase for the app install python-firebase package.
from firebase import firebase


firebase = firebase.FirebaseApplication('https://esp32-5c542-default-rtdb.firebaseio.com', None)
bpm = firebase.get('/test/a', '')
print(bpm)
#sometimes, When we run above code firsttime it can propagate and syntax error, to solve that error please
#rename 'async' file as 'async_' which is in this path C:\Users\mrsak\OneDrive\Desktop\dashboard\venv\Lib\site-packages\firebase
#also reaname the import location of the async file as async_ inside the firebase and _init_ file which are located
# in same path.