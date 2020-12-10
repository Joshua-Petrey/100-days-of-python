print('''
         .e$c"*eee...                 
                z$$$$$$.  "*$$$$$$$$$.                    
            .z$$$$$$$$$$$e. "$$$$$$$$$$c.                 
         .e$$P""  $$  ""*$$$bc."$$$$$$$$$$$e.             
     .e$*""       $$         "**be$$$***$   3             
     $            $F              $    4$r  'F            
     $           4$F              $    4$F   $            
    4P   \       4$F              $     $$   3r           
    $"    r      4$F              3     $$r   $           
    $     '.     $$F              4F    4$$   'b          
   dF      3     $$    ^           b     $$L   "L         
   $        .    $$   %            $     ^$$r   "c        
  JF             $$  %             4r     '$$.   3L       
 .$              $$ "               $      ^$$r""         
 $%              $$P                3r  .e*"              
'*=*********************************$$P"    
''')

print("You awake in your tent to the sound off gunshots")
print("You take a peek outside to see your fellow campers lying on the ground dead")
print("Your misson is to escape alive")

print("You crawl slowly from you tent")

dir = input("To your left you see you see a shadowy figure. To the right you see your guide's tent which may have a weapon in it./n Which way do you go?").lower()
if dir == "left":
	print('''The figure is startled by your approach. As it turns you can see a pistol in its hand\n
	It aims a at your head and shoots
	YOUR DEAD!''')
else:
	print(''' You scurry to your guides tent and rummage around to no avail. There is nothing here
	''' )

dir2 = input('''As you leave your guides tent you hear a scream to you right.
Do you want to investigate the scream or wait in the tent?
 ''')

if dir2 == "wait":
	print(''' You wait in the tent until there is nothing but silence.You can hear police sirens in the distance.

	YOU ARE RESCUED!
	''')
	
elif dir2 == "investigate":
	print(''' You move towards the scream to find a male figure standing over a female. Before you can call to the male you are hit over the head with a bat.
		YOUR DEAD
	''')