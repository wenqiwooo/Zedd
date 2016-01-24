class MoodController:

	def __init__(self):
		# nothing
		self.id = 0

	def setMoodParty(self, lightCtlr, mPlayer):
		# disco lighting and party music
		mPlayer.setMoodParty()
		lightCtlr.on(4)

	def setMoodRomantic(self, lightCtlr, mPlayer):
		# pink lighting and romantic music
		mPlayer.setMoodRomantic()
		lightCtlr.on(1);
		
	def setMoodProductive(self, lightCtlr, mPlayer):
		mPlayer.setMoodProductive()
		lightCtlr.on(2)


