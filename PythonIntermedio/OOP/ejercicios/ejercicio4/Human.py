class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Feet:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand

class Torso:
    def __init__(self, head:Head, right_arm:Arm, left_arm:Arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm


class Leg:
    def __init__(self, feet:Feet):
        self.feet = feet

class Human:
    def __init__(self, torso:Torso, right_leg:Arm, left_leg:Leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg  



head = Head()

left_hand = Hand()
right_hand = Hand()

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

torso = Torso(head, right_arm, left_arm)

left_feet = Feet()
right_feet = Feet()

right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

human = Human(torso, right_leg, left_leg)

print(human.torso)
print(human.torso.head)
print(human.torso.right_arm)
print(human.torso.right_arm.hand)
print(human.right_leg)
print(human.right_leg.feet)