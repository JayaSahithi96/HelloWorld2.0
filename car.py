command=""
started= False
while True:
   command= input(">").lower()

   if command == 'start':
       if started:
           print("car is already started")
       else:
           started= True
           print("car started..")
   elif command == "stop":
       if not started:
           print("car is already stopped")
       else:
           Started= False
           print("car stopped")
   elif command== "help":
       print("""
Start-to start
stop- to stop
quit- to quit
       """)
   elif command=="quit":
       break
   else:
       print("sorry I dont understant")



