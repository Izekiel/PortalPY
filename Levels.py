import eventBasedAnimation
from Tkinter import *

class Levels(object):
	# def __init__(self,w,h):
	# 	self.w, self.h = w, h
	# 	self.wOB=50
	# 	self.boxImg=PhotoImage("images/graySquare.gif")
	# 	self.levelGrid=[]
	# 	(wGrid,hGrid)=(16,10)
	# 	for x in xrange(hGrid):
	# 		self.levelGrid+=[[]]
	# 		for i in xrange(wGrid):
	# 			self.levelGrid[x]+=[[]]

	# def drawFn(self,canvas):
	# 	(w,h,wOB,borderColor)=(self.w,self.h,self.wOB,"gray")

	class Level1(object):
		def __init__(self,w,h,wGrid,hGrid,levelGrid):
			self.w, self.h = w, h
			self.wOB = wOB = 50 ##Width of Blocks
			self.levelGrid=levelGrid
			(self.wGrid,self.hGrid)=(wGrid,hGrid)
			self.playerInitialx0=wOB+15
			self.playerInitialy0=h-wOB-20
			#Data for each cell will be as such
			#[Shootable,notShootable,isBeginning,isEnd,bPortal,oPortal]
			for x in xrange(hGrid):
				self.levelGrid+=[[]]
				for i in xrange(wGrid):
					if (x==0) or (i==0) or (x==hGrid-1) or (i==wGrid-1):
						self.levelGrid[x]+=[[1,0,0,0,0,0]] 
					else:
						self.levelGrid[x]+=[[0,0,0,0,0,0]]

		def setBoard(self):
			(w,h,wOB)=(self.w,self.h,self.wOB)
			(wGrid,hGrid)=(self.wGrid,self.hGrid)
			#The next few lines make the level
			for i in xrange(5):
				self.levelGrid[6][i][0]=1
			for i in xrange(8,wGrid-1):
				self.levelGrid[3][i][0]=1
			for x in xrange(10,wGrid-1):
				self.levelGrid[10][x][0]=1
			for x in xrange(13,wGrid-1):
				self.levelGrid[9][x][0]=1
			for x in xrange(16,wGrid-1):
				self.levelGrid[8][x][0]=1
			for x in xrange(1,6):
				self.levelGrid[x][4][0]=1
			self.levelGrid[10][1][2]=1 	#isBeginning
			self.levelGrid[2][18][3]=1 	#isEnd
			return self.levelGrid


		def drawFn(self,canvas):
			levelGrid=Levels.Level1.setBoard(self)
			(w,h,wOB,wGrid,hGrid)=(self.w,self.h,self.wOB,self.wGrid,\
																self.hGrid)
			for y in xrange(self.hGrid):
				for x in xrange(self.wGrid):
					if self.levelGrid[y][x][0]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="gray")
					elif self.levelGrid[y][x][1]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="dim gray")
					elif self.levelGrid[y][x][2]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="steel blue")
					elif self.levelGrid[y][x][3]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="firebrick")
					elif self.levelGrid[y][x][4]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
											(y*wOB)+wOB,fill="deep sky blue")
					elif self.levelGrid[y][x][5]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
											(y*wOB)+wOB,fill="dark orange")


	class Level2(object):
		def __init__(self,w,h,wGrid,hGrid,levelGrid):
			self.w, self.h = w, h
			self.wOB = wOB = 50 ##Width of Blocks
			self.levelGrid=levelGrid
			(self.wGrid,self.hGrid)=(wGrid,hGrid)
			self.playerInitialx0=wOB+15
			self.playerInitialy0=h-wOB-20
			#Data for each cell will be as such
			#[Shootable,notShootable,isBeginning,isEnd,bPortal,oPortal]
			for x in xrange(hGrid):
				self.levelGrid+=[[]]
				for i in xrange(wGrid):
					if (x==0) or (i==0) or (x==hGrid-1) or (i==wGrid-1):
						self.levelGrid[x]+=[[1,0,0,0,0,0]] 
					else:
						self.levelGrid[x]+=[[0,0,0,0,0,0]]

		def setBoard(self):
			(w,h,wOB)=(self.w,self.h,self.wOB)
			(wGrid,hGrid)=(self.wGrid,self.hGrid)
			#The next few lines make the level
			for i in xrange(11):
				self.levelGrid[6][i][0]=1

			for i in xrange(4,wGrid-1):
				if 4<=i<=wGrid-5:
					self.levelGrid[3][i][0]=1
				else:
					self.levelGrid[3][i][1]=1

			self.levelGrid[5][1][2]=1 	#isBeginning
			self.levelGrid[2][10][3]=1 	#isEnd
			return self.levelGrid


		def drawFn(self,canvas):
			levelGrid=Levels.Level2.setBoard(self)
			(w,h,wOB,wGrid,hGrid)=(self.w,self.h,self.wOB,self.wGrid,\
																self.hGrid)
			canvas.create_rectangle(0,0,1000,800,fill="white")
			for y in xrange(self.hGrid):
				for x in xrange(self.wGrid):
					if self.levelGrid[y][x][0]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="gray")
					elif self.levelGrid[y][x][1]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="dim gray")
					elif self.levelGrid[y][x][2]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="steel blue")
					elif self.levelGrid[y][x][3]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
												(y*wOB)+wOB,fill="firebrick")
					elif self.levelGrid[y][x][4]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
											(y*wOB)+wOB,fill="deep sky blue")
					elif self.levelGrid[y][x][5]==1:
						canvas.create_rectangle(x*wOB,y*wOB,(x*wOB)+wOB,\
											(y*wOB)+wOB,fill="dark orange")
