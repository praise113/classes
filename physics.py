class Physics:
    def mass(self,force,distance):
        print("enter valuse to claculate mass")
        masf = input("Enter force")
        mass = force * distance
        return  mass
    def velocity(self,distance,time):
         velocity = distance / time
         return  velocity
    def force(self,mass,acceleration):
        force = mass * acceleration
        return  force
    def power(self,workdone,timetaken):
        power = workdone/timetaken
        return power
    def acceleration(self,force,mass):
        acceleration = force / mass
        return acceleration