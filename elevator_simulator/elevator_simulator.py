class Elevator(object):

    def __init__(self, max_capacity = 5):
        # Current floor the elevator is on
        self.cur_floor = 0.
        # DOT = Direction Of Travel. Can be "Up" or "Down".
        self.DOT = "Up"
        # The people in the elevator
        self.passengers_in_elevator_list = []
        # Sets the start time to zero
        self.cur_time = 0
        # Sets the maximum capacity of the elevator
        self.max_capacity = max_capacity
        # Counts the number of people who have reached their destination
        self.happy_people = 0
        # List of all people who are in the simulation
        self.all_passenger_list = []
        # The passengers who are waiting
        self.queue_list = []
        # how much time an event takes... setting this to 4 would make that step take 4 seconds extra
        self.action_time = 0
        # last time it checked the passenger list to see if there are new buttons
        self.last_check = 0
        # This is to know what the top floor is
        self.top_floor = 0

    #This is run once before the simulation begins to set the time
    def set_cur_time(self, cur_time):
        self.cur_time = cur_time

    #This is run once before the simulation begins to create the "all passenger list"
    def set_all_passenger_list(self, all_passenger_list):
        self.all_passenger_list = all_passenger_list

    #This is run once before the simulation begins to create an empty "passengers in elevator list"
    def set_passengers_in_elevator_list(self):
        self.passengers_in_elevator_list = [None for i in range(len(self.all_passenger_list))]

    #This is run once before the simulation begins to set the top_floor taken from the building class
    def set_top_floor(self, top_floor):
        self.top_floor = top_floor

    #This is used to make an action, like someone getting on the elevator, take more time
    def update_time(self):
        return self.action_time

    #This moves the elevator .25 floors up in the indicated direction (moving up one floor takes 2 seconds)
    def move(self, direction):
        if direction == "Up":
            self.cur_floor += 0.25
        else:
            self.cur_floor += -0.25

    # A method that changes the direction of the elevator
    def change_direction(self):
        if self.DOT == "Up":
            self.DOT = "Down"
        else:
            self.DOT = "Up"



    # A method to add passengers to the elevator. It takes a list of passengers as an input and the passengers who have waited the most enter first, either until there are no more people waiting at that floor, or until the maximum capacity of the elevator is reached.
    def new_passenger(self, new_passengers_list):

        #a dynamic list that contains the identities of people who are waiting outside of the elevator and want to get in
        identities_list_still_waiting = [i.identity for i in new_passengers_list]

        #a static list that contains the identities of all the people who wanted to get into the elevator in the beginning
        identities_list_all_passengers = [i.identity for i in new_passengers_list]

        num_passengers_got_on = 0   #how many people got into the elevator
        identities_list_people_who_got_on = []   #a list of identities of the passengers that got on

        # Adding new passengers, while there are still passengers who want to get on and the elevator still has free space:
        while len(new_passengers_list)>num_passengers_got_on and len([x for x in self.passengers_in_elevator_list if x is not None]) < self.max_capacity:

            num_passengers_got_on += 1   #one more person gets in the elevator

            #contains the identity of the passenger that gets in - the one with the smallest identity (waited the most)
            id_passenger_gets_on = min(identities_list_still_waiting)

            #contains the index of the person who gets in within identities_list_all_passengers
            index_of_passenger_in_identities_list_all_passengers = identities_list_all_passengers.index(id_passenger_gets_on)

            #contains the index of the person who gets in within identities_list_still_waiting
            index_of_passenger_in_identities_list_still_waiting = identities_list_still_waiting.index(id_passenger_gets_on)

            #add that person to the elevator
            self.passengers_in_elevator_list[id_passenger_gets_on] = new_passengers_list[index_of_passenger_in_identities_list_all_passengers]

            #set the pickup time of that person
            self.passengers_in_elevator_list[id_passenger_gets_on].set_pickup_time(self.cur_time)

            #add the identity of that person to the list of identities of passengers that should get in
            identities_list_people_who_got_on.append(id_passenger_gets_on)

            #delete that person from identities_list_still_waiting
            del identities_list_still_waiting[index_of_passenger_in_identities_list_still_waiting]

        #delete the passengers who got on from the queue_list
        indeces_to_delete_from_queue_list = []   #the indeces within the queue_list with the people who got on
        for element_in_queue_list in self.queue_list:

            #if the identity of the element in the queue list is also in the list of identities of people who got on:
            if element_in_queue_list[2] in identities_list_people_who_got_on:

                # add that index to indeces_to_delete_from_queue_list
                indeces_to_delete_from_queue_list.append(self.queue_list.index(element_in_queue_list))

        for index_to_delete_from_queue_list in range(len(indeces_to_delete_from_queue_list)-1,-1,-1):
            #delete these elements from the queue_list (deleting in reverse order so not to mess up the indexation)
            del self.queue_list[indeces_to_delete_from_queue_list[index_to_delete_from_queue_list]]

        #print a warning if some passenger could not enter because the elevator was full
        if len(new_passengers_list)>num_passengers_got_on:
            print "Elevator is FULL!!! Some passengers could not enter!"



    # A method used for passengers to get off the elevator at their desired floor. It takes as input a list of passengers who want to exit and removes them from the elevator
    def passenger_exit(self, exit_passengers_list):

        #The destiontions of all passengers that are supposed to exit at this floor should all be this same floor
        exit_destinations = [i.destination for i in exit_passengers_list]
        if exit_destinations != [self.cur_floor for i in range(len(exit_passengers_list))]:
            print "Warning!!! Some passenger(s) do(es) not want to exit on this floor!!!"
        else:
            for exit_passenger in exit_passengers_list:
                self.passengers_in_elevator_list[exit_passenger.identity].set_time_exited(self.cur_time)#set the time of drop off
            for exit_passenger in exit_passengers_list:
                self.passengers_in_elevator_list[exit_passenger.identity] = None   #remove them from passengers_in_elevator_list

            #These people are now happy - they have reached their desired destination
            self.happy_people += len(exit_passengers_list)



    # This method is used to update the "last_check", which is used to see if people have pressed the elevator button since the last time it was checked. This is important because some actions (people getting on elevator) take time and if the elevator only checks for button presses at the current time, it will have missed those that happened between the last check and current time.
    def update_last_check(self):
        self.last_check = self.cur_time

    def simulation(self):
        #There is a bit of logistics happening every time
        #First it restores the time an action takes to default
        self.action_time = 0

        #It then updates the button list, from the action list, adding all actions since it has last been checked
        for passenger in self.all_passenger_list:
            if passenger.time_appeared > self.last_check and passenger.time_appeared <= self.cur_time:
                self.queue_list.append([passenger.pickup_floor, passenger.direction, passenger.identity])
        self.update_last_check()

        #There are then a couple of scenarios in which the elevator could find itself

        #The first scenaroio is that there are no people in the elevator and no one waiting for the elevator,
        # and the elevator waits
        if len(self.queue_list) == 0 and self.passengers_in_elevator_list == [None for i in range(len(self.passengers_in_elevator_list))]:
            return "The elevator is waiting"

        #The next is if there are no people in the elevator, but there are people waiting for the elevator.
        # In this case, the elevator moves to the most extreme person waiting in its direction of travel.

        elif self.passengers_in_elevator_list == [None for i in range(len(self.passengers_in_elevator_list))]:
            if self.DOT == "Up":
                temp_goal= max(item[0] for item in self.queue_list)
                if temp_goal > self.cur_floor:
                    goal = temp_goal
                elif temp_goal < self.cur_floor:
                    self.change_direction()
                    goal = min(item[0] for item in self.queue_list)
                else :
                    goal = self.cur_floor
            elif self.DOT == "Down":
                temp_goal= min(item[0] for item in self.queue_list)
                if temp_goal < self.cur_floor:
                    goal = temp_goal
                elif temp_goal > self.cur_floor:
                    self.change_direction()
                    goal = max(item[0] for item in self.queue_list)
                else :
                    goal = self.cur_floor

        #The third case is that there are people in the elevator. The elevator sets its goal as the most
        # extreme destination from the people on the elevator.
        else :
            if self.DOT == "Up":
                goal = max(passenger.destination for passenger in [i for i in self.passengers_in_elevator_list if i != None])
            else: # self.DOT == "Down"
                goal = min(passenger.destination for passenger in [i for i in self.passengers_in_elevator_list if i != None])

        #This defines how the elevator moves towards its goal
        print "goal =", goal
        if goal > self.cur_floor and self.DOT == "Up":
            self.move("Up")
        elif goal > self.cur_floor and self.DOT == "Down":
            self.DOT = "Up"
            self.move("Up")
        elif goal < self.cur_floor and self.DOT == "Down":
            self.move("Down")
        elif goal < self.cur_floor and self.DOT == "Up":
            self.DOT = "Down"
            self.move("Down")
        elif goal == self.cur_floor:
            self.change_direction()

        #If a person is in the elevator and its on their floor, they should get off
        getting_off = []
        for i in range(0,len(self.passengers_in_elevator_list)):
            if self.passengers_in_elevator_list[i] != None:
                if self.cur_floor == self.passengers_in_elevator_list[i].destination:
                    getting_off.append(self.passengers_in_elevator_list[i])
                    #self.passengers_in_elevator_list[i] = None
                    #It takes 4 seconds for the elevator doors to open and than shut. People both get on and get off during this time, thus if one passenger is getting on or off, the action will take 4 seconds.
                    self.action_time = 4
        print "getting off", [i.identity for i in getting_off]
        self.passenger_exit(getting_off)

        #If a person is on the same level as the elevator and it is moving in their direction of travel, they should get on
        getting_on = []
        for i in range(0,len(self.queue_list)):
            if (self.cur_floor == self.queue_list[i][0] and self.DOT == self.queue_list[i][1]):
                getting_on.append(self.all_passenger_list[self.queue_list[i][2]])
                self.action_time = 4
        self.new_passenger(getting_on)

        print "Queue List is", self.queue_list
        print "Current floor =", self.cur_floor
        print "Passengers in elevator =", [i.identity for i in self.passengers_in_elevator_list if i != None]
        print "Happy people =", self.happy_people

    def simulation_2(self):
        self.action_time = 0
        """ Example strategy. Starts at bottom, moves up to top, moves down, picking people up when it is going in their DOT """
        for passenger in self.all_passenger_list:
            if passenger.time_appeared > self.last_check and passenger.time_appeared <= self.cur_time:
                self.queue_list.append([passenger.pickup_floor, passenger.direction, passenger.identity])
        self.update_last_check()

        #Move in the correct direction, going all the way up and than all the way down

        if self.DOT == "Up" and self.cur_floor != self.top_floor:
            self.move("Up")
        elif self.DOT == "Down" and self.cur_floor != 0:
            self.move("Down")
        elif self.DOT == "Up" and self.cur_floor == self.top_floor:
            self.change_direction()
        elif self.DOT == "Down" and self.cur_floor == 0:
            self.change_direction()

        getting_off = []
        for i in range(0,len(self.passengers_in_elevator_list)):
            if self.passengers_in_elevator_list[i] != None:
                if self.cur_floor == self.passengers_in_elevator_list[i].destination:
                    getting_off.append(self.passengers_in_elevator_list[i])
                    #self.passengers_in_elevator_list[i] = None
                    self.action_time = 4
        self.passenger_exit(getting_off)

        getting_on = []
        for i in range(0,len(self.queue_list)):
            if (self.cur_floor == self.queue_list[i][0] and self.DOT == self.queue_list[i][1]):
                getting_on.append(self.all_passenger_list[self.queue_list[i][2]])
                self.action_time = 4
        self.new_passenger(getting_on)

        print "getting off", [i.identity for i in getting_off]
        print "Queue List is", self.queue_list
        print "Current floor =", self.cur_floor
        print "Passengers in elevator =", [i.identity for i in self.passengers_in_elevator_list if i != None]
        print "Happy people=", self.happy_people



from random import randint

class Passenger(object):
    #passengers have the basic attributes of how long it took, where they are, where they want to go, and an ID
    def __init__(self, time_appeared = 0., destination = 1, pickup_floor = 0, identity = 0):
        self.pickup_floor = pickup_floor
        self.time_appeared = time_appeared
        self.time_exited = 0.
        self.destination = destination
        self.pickup_time = 0.
        self.identity = identity
        self.direction = "Up" if (self.destination-self.pickup_floor) > 0 else "Down"

    def set_time_exited(self, time_exited):
        self.time_exited = time_exited

    def set_pickup_time(self, pickup_time):
        self.pickup_time = pickup_time

    def get_pickup_time(self):
        return self.pickup_time

    def get_time_exited(self):
        return self.time_exited

    def get_time_appeared(self):
        return self.time_appeared

    def get_destination(self):
        return self.destination

class Building(object):
    # Each building has a distribution of people that will be sampled to produce the passengers, along with a
    # total number of passengers and number of floors
    def __init__(self, distribution_of_people, total_num_passengers):
        self.distribution_of_people = distribution_of_people
        self.floors = len(distribution_of_people)
        self.total_num_passengers = total_num_passengers

    def get_floors(self):
        return self.floors

    def get_distribution(self):
        return self.distribution_of_people

    def get_total_num_passengers(self):
        return self.total_num_passengers


  #______ NEW CELL ____

  import random
import numpy as np

result_5 = []

random.seed(1)
np.random.seed(1)


# In order to simulate 10 times, we create an outer while loop
counter = 0
sims_10 = []

while counter <10:

    #Creating the Building, which is called At Home (the name of our Hyderabad residence).
    #distribution_of_people tells us that there will be 6 times more probability that a person will travel to/from the 0-th floor compared to any other floor. Also, there is equal probability that a person will travel to/from i-th floor, compared to j-th floor, when i and j are positive.
    At_Home = Building(distribution_of_people = [220,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], total_num_passengers = 20)

    num_floors = At_Home.get_floors()
    distribution = At_Home.get_distribution()
    num_passengers = At_Home.get_total_num_passengers()

    #Normalize the distribution. Now it contains probabilities.
    distribution = [float(distribution[i])/sum(distribution) for i in range(len(distribution))]

    #Sample the pickup locations according to the distribution
    pickup_locations = np.random.choice(range(num_floors), num_passengers, p=distribution)

    #In order to sample the destinations, we should make sure that we remove the pickup floor from the space of possibilities, but still keep the properties of the distribution.
    destinations = []
    for index_passenger in range(num_passengers):

        #This will be the new distribution once we remove the element that corresponds to the pickup floor of the passenger
        distribution_without_passenger = [a for a in distribution]

        #This will be the new range of possible floors once we remove the pickup floor of the passenger
        range_without_passenger = range(num_floors)

        #Deleting the pickup floor
        del range_without_passenger[pickup_locations[index_passenger]]

        #Deleting the element in the distribution that corresponds to the pickup floor
        del distribution_without_passenger[pickup_locations[index_passenger]]

        #Normalizing the distribution, so that it contains probabilities again
        distribution_without_passenger = [float(distribution_without_passenger[i])/sum(distribution_without_passenger) for i in range(len(distribution_without_passenger))]

        #We sample the desired destination from the new range of floors and the new distribution
        destinations.append(np.random.choice(range_without_passenger, 1, p=distribution_without_passenger)[0])

    #delays is a list that tells us how much time passes between the arrival of two consecutively arriving passengers.
    #We want the delays to be distributed, such that a small proportion of the delays are zero.

    #First, we input the average delay we want:
    average_delay = 40.0

    #We sample the delays from a poisson distribution centered at ten times the average delay.
    #Then we remove nine times the average delay from the result, effectively shifting the poisson distribution to the left.
    #As a result, part of the distribution falls into the negative numbers. Any samples from that part are considered to be zero.
    delays = np.random.poisson(lam=10*average_delay, size=num_passengers-1)
    delays = [(i-9*average_delay)*((i-9*average_delay)>0) for i in delays]

    #The first person always comes at the third second since the start of the simulation
    times_of_arrival = [3.]

    #Appending the times of arrival of all passengers to the list
    for i in range(num_passengers-1):
        times_of_arrival.append(times_of_arrival[i]+delays[i])

    #Creating the list of passengers based on the time they arrive, the pickup floor, and the destination floor. Each passenger has an ID, which is assigned according to the order of arrival. So passengers with smaller IDs have arrived earlier.
    passenger_list=[]
    for i in range(num_passengers):
        passenger_list.append(Passenger(time_appeared = times_of_arrival[i], destination = destinations[i], pickup_floor = pickup_locations[i], identity = i))

    #Setting up the current time
    cur_time = 0.

    #Creating the elevator
    elevator = Elevator()
    elevator.set_all_passenger_list(passenger_list)
    elevator.set_passengers_in_elevator_list()
    elevator.set_top_floor(num_floors-1)

    #Printing the details of the simulation
    print "Times appeared:", [i.time_appeared for i in passenger_list]
    print "Pickup floors:", [i.pickup_floor for i in passenger_list]
    print "Destinations:", [i.destination for i in passenger_list]
    print "IDs:", [i.identity for i in passenger_list]



    #This is the main while loop for the simulation (if only running the simulation once, this is the only while loop needed)
    while num_passengers!=elevator.happy_people:

        #Giving the current time to the elevator
        elevator.set_cur_time(cur_time)

        #Calling the simulation method. It works with .simulation() or .simulation_2().
        elevator.simulation_2()

        #Updating the current time based on what happened in this round of the simulation
        cur_time+=elevator.update_time()

        #Half a second passes at every round no matter what
        cur_time+=0.5

        #Printing the current time
        print "Current time is:", cur_time

    counter +=1
    sims_10.append(passenger_list)

results_5 = sims_10

#____ NEW CELL (MARKDOWN)___

The Results_X lists are lists of the output of each type of simulation
    each one is made up of 10 lists of 20 passengers with their associated values



<b>results_matrix_0: This is a normal simulation.</b> <br />
Number of Floors = 12 <br />
Average delay = 40 seconds  <br />
Floor Distribution = [110,10,10,10,10,10,10,10,10,10,10,10] <br />
Number of Passengers = 20 <br />
This runs our algorithim.

<b>results_matrix_1:</b> <br />
is the same as above but with the comparison algorithm.

<b>results_matrix_2: This is a high density simulation.</b> <br />
Number of Floors = 12 <br />
Average delay = 3 seconds  <br />
Floor Distribution = [110,10,10,10,10,10,10,10,10,10,10,10], <br />
Number of Passengers = 20 <br />
This runs our algorithim.

<b>results_matrix_3:</b> <br />
is the same as above but with the comparison algorithm.

<b>results_matrix_4: This is a large building with lots of floors.</b> <br />
Number of Floors = 23 <br />
Average delay = 40 seconds  <br />
Floor Distribution = [220,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], <br />
Number of Passengers = 20 <br />
This runs our algorithim.

<b>results_matrix_5:</b> <br />
is the same as above but with the comparison algorithm.

<b>results_matrix_6: This is a building with a skewed distribution. </b> <br />
Number of Floors = 12 <br />
Average delay = 40 seconds  <br />
Floor Distribution = [10,10,100,10,10,10,10,10,100,10,10,10], <br />
Number of Passengers = 20 <br />
This runs our algorithim.

<b>results_matrix_7:</b> <br />
is the same as above but with the comparison algorithm.
____

Each of these 8 lists is a list of 10, with each element being <br />
a list of passengers (passenger_list) after the simulation,, <br />
with their associated attributes (time they got on the elevator, <br />
time they got off, etc.)

Thus, <br />
results_matrix_0[0]: <br />
is the first of 10 runs of the simulation with the given conditions, and is a list of all passengers and  <br />
results_matrix_0[0][0] is the first passenger in the given simulation.


#______New Cell___

#This can be run to get a summary of results for a run of the simulation
import numpy as np

#This function prints a variety of metrics from a list
def results(lis,name):

    print "Average time from",name, sum(lis)/float(len(lis))
    print "Max time from",name, max(lis)
    print "95th percentile of time from",name, np.percentile(np.array(lis), 95)
    print "Median of time from",name,  np.median(np.array(lis))
    print "__________\n"

# This is the main results function, it takes a list of length 100 and prints the appropriate results
# We run this function on the 8 lists of 100 contained within results list

def print_results(simulation_10_list, label):

    pushing_to_arrival = []
    wait_for_elevator = []
    wait_in_elevator = []

    for j in range(0,len(simulation_10_list)):
        for i in simulation_10_list[j]:
            wait_for_elevator.append(i.get_pickup_time() - i.get_time_appeared())
            wait_in_elevator.append(i.get_time_exited() - i.get_pickup_time())
            pushing_to_arrival.append(i.get_time_exited() - i.get_time_appeared())

    print label
    print "Measures of efficiency:"
    print "__________\n"


    results(wait_for_elevator, "start to getting on the elevator:")
    results(wait_in_elevator, "getting on the elevator to getting to destination:")
    results(pushing_to_arrival, "pressing the button to getting to destination:")


# print_results(results_0, "Normal- simulation")
# print_results(results_1, "Normal- simulation_2")
# print_results(results_2, "High Density- simulation")
# print_results(results_3, "High Density- simulation_2")
# print_results(results_4, "Tall- simulation")
# print_results(results_5, "Tall- simulation_2")
# print_results(results_6, "Skewed- simulation")
# print_results(results_7, "Skewed- simulation_2")

