
def adventure(): 
    adventure = raw_input("It's a beautiful, sunny day. Would you like to go on an adventure? y/n: ").lower()
    if adventure == "y":
        print "Excellent! Let's have some fun! Don't forget to bring a lunch!"
    else:
        print "Too bad, you're missing out... "

def mountains_or_beach():
    mountains_or_beach = int(raw_input("Where would you like to go? 1: Mountains  2: Beach? "))
    if mountains_or_beach == 1:
        print "'The mountains are calling and I must go.' - John Muir"
    if mountains_or_beach == 2:
        print "B.E.A.C.H. = Best Escape Anyone Can Have"
    else:
        print "OOPS, I don't understand that answer, can you try again?"
        # how do I return to this loop?
        # if / if / else loop?

def hike_or_climb():
    hike_or_climb = int(raw_input("Would you rather go hiking or rock-climbing? 1: Hike  2: Rock-Climb "))
    if hike_or_climb == 1:
        print "'I took a walk in the woods and came out taller than the trees.' - Henry David Thoreau"
    if hike_or_climb == 2:
        print "'Climb the mountain not to plant your flag, but to embrace the challenge, enjoy the air and behold the view. \nClimb it so you can see the world, not so the world can see you.' \n- David McCullough Jr."
    else:
        print "OOPS, I don't understand that answer, can you try again?"

def waterfalls_or_views():
    waterfalls_or_views = int(raw_input("Do you want to see waterfalls or go directly to the summit for the view from the top?? \n1: Waterfalls  \n2: Scenic Views "))
    if waterfalls_or_views == 1:
        print "Good choice - let's go see some waterfalls!"
        # footsteps?
        picnic_or_turn_around_or_go_on()
    if waterfalls_or_views == 2:
        print "You're in for quite a hike, but you will not be disappointed! "
    else:
        print "OOPS, I don't understand that answer, can you try again?"
        waterfalls_or_views()
        # not callable...

def picnic_or_turn_around_or_go_on():
    print "You have reached the base of the waterfall. It is tall, beautiful and majestic. The roaring water intoxicates you and the mist revitalizes you."
    print "'A strong man and a waterfall always channel their own path.' - Anonymous"
    print "Now that you've taken in the splendor of nature, what would you like to do?"
    picnic_or_turn_around_or_go_on = int(raw_input("1: I want to eat my lunch here at the waterfall  \n2: I think I'm ready to head back  \n3: I'm still fresh and there is a trail that will take me to the summmit, I think I'm going to continue on and see what these views are all about " ))
    if picnic_or_turn_around_or_go_on == 1:
        print "What a wonderful place for a picnic!"
        # print a picture of a picnic being eaten
        # print a picture of a squirell / chipmunk
        print "Oh no!! A chipmunk stole your chips... Oh well, I hope you have some trail mix if you get hungry later!"
        print "Now that you're full, do you want to hike back and go home, or do you think you want to continue on to the summit?"
        go_on_or_turn_around = int(raw_input("1: It's been an amazing experience, but I think I'm ready to head home  \n2: Are you kidding me, if the waterfall was this amazing, imagine what the view from the top is going to be like - I'm going on! "))
        if go_on_or_turn_around == 1:
            print "OK, you trace your steps back to the trailhead and head home.  It has been an awesome outing and you still have time to relax at home. "
            # print foot steps or "relaxing"
            exit()  
        if go_on_or_turn_around == 2:
            print "That's the spirit! This is an adventure, after all! "
            # next function...
        else:
            print "OOPS, I don't understand that answer, can you try again?"
            go_on_or_turn_around()
            # not callable... how do I restart loop?
    if picnic_or_turn_around_or_go_on == 2:
        print "OK, you trace your steps back to the trailhead and head home.  \nIt has been an awesome outing and you still have time to relax at home. "
        # print foot steps or "relaxing"
        exit()
    if picnic_or_turn_around_or_go_on == 3:
        print "Excellent, you won't be disappointed!"
    else:
        print "OOPS, I don't understand that answer, can you try again?" 
        picnic_or_turn_around_or_go_on()
        # "int is not callabe"  how do I loop?





        # print "You get hungry halfway back to the car and decide to dig into your lunch after all. "
        # print "You find a log on the side of the trail and decide to sit there to eat. "
        # print "OH NO!! You drop half your sandwich and it is instantly covered with ants"

# ask the user if they would like to take an adventure
# do not forget to bring lunch!
# where would they like to go? mountains or beach?
# mountains: would you like to go for a hike or rock climbing?
# hike: do you want to see waterfalls or great scenic views?
#     waterfalls: hike along the river... a beautiful waterfall
#       do you want to have a picnic at the base of the waterfall or continue on or turn around?
#           picnic: eat lunch - a chipmunk steals your chips - you finish your lunch and have to turn around because you do not have any more food - great outing with a good story
#       continue on: you hike to the top of the mountain and see beautiful scenic views
#       do you have a head lamp? if yes, you stay at the top and watch the sunset and then hike back in the dark with your headlamp: what an amazing time 
#       if not, turn around and head back to the trailhead and go home - what a great outing!
#       turn around: head back to the trailhead - you had a great hike with good scenery and have time to relax at home afterwards
#     great scenic views: hike to the top of the mountain and see beautiful views
#         do you want to picnic or turn around?
#         picnic: eat lunch - meet someone else eating lunch up there and decide to hike back with them - new friends
#         turn around: you head back to the trailhead but have to stop halfway back because you are hungry - drop half of your sandwich (sad face)
#             get back to your car and head for the nearest burger joint because you are still hungry- share your story with a stranger and make a new friend
# rock climbing: do you have a friend with you to belay?  
#     yes: great outing rock climbing with a friend - you get to the top, eat lunch with hikers and hike back with  - new friends
#     no: you were unprepared - go home sad
# beach: do you want to surf or scuba?
# surf: you paddle out and wait for the next set of waves... wipe out!
#     try again: y/n?
#         y: you paddle out and wait for the next set of waves... small wave - manageable but not exciting
#     try again: y/n?
#         y: you paddle out and wait for the next set of waves... wipe out!
#       ::: RANDOMIZER?? :::
#         n: put your board away and eat lunch
#     do you want to hang out at the beach and watch the sunset?
#         y: you grab a towel and a book and lay out on the beach - you see a beautiful sunset - then you go home 
#         n: you go home - you had a good day at the beach
# scuba: do you have a dive buddy? y/n
#   y: you wade out into the water to explore the magical world under the sea 
#     you come up to a cave, do you enter? y/n
#       y: you explore the cave and come face to face with a sea turtle - it swims away peacefully - you explore the cave and exit
#       n: you continue on your journey and come across a sea kelp forrest. do you enter? y/n
#         y: you go exploring and get kelp wrapped around your ankle - do you have a knife to cut yourself free? y/n
#           y: you cut yourself free and find your way out of the kelp and continue on
#           n: you bang on your tank to get your dive buddy's attentionand they use their knife to cut the kelp away - you exit the kelp and continue on
#         n: you circle around the kelp and you swim past a couple of sea otters playing
#         ... you are halfway through your air - time to turn around and return to shore
#         time for lunch and reminise with your dive buddy about all the amazing things you saw on your dive
#   n: you came unprepared - go home sad



# # adventure()
# # mountains_or_beach()
# # hike_or_climb()
# # picnic_or_turn_around_or_go_on()

waterfalls_or_views()

