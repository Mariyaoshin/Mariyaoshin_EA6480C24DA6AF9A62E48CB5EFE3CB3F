#Define the base class Player.
class Player:
  def play(self):
    print("The player is playing cricket.")

#Define a derived class Batsman:
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#create the instances of Batsman and Bowler classes:
batsman=Batsman()
bowler=Bowler()

#call the method play() for each object:
batsman.play()
bowler.play()