import eventBasedAnimation
from Tkinter import *
from Levels import *

class Player(object):
	def __init__(self,x0,y0,level):
		(w,h,wOB,wGrid,hGrid,levelGrid)=800,500,50,20,12,[]
		self.hGrid,self.wGrid,self.wOB=hGrid,wGrid,wOB
		self.height=20
		self.width=15
		self.x=x0
		self.y=y0
		self.gravity=25
		self.level=level
		self.curLevel=eval("Levels.Level%d(w,h,wGrid,hGrid,levelGrid)"\
																%self.level)
		self.levelGrid=self.curLevel.setBoard()

	def drawFn(self,canvas):
		(w,h,x0,y0)=(self.width,self.height,self.x,self.y)
		canvas.create_rectangle(x0,y0,x0+w,y0+h,fill="red")

	def isLegal(self,x0,y0):
		illegalCells=[]
		for y in xrange(self.hGrid):
				for x in xrange(self.wGrid):
					if self.levelGrid[y][x][0]==1 or \
											self.levelGrid[y][x][1]==1:
						illegalCells+=[(x,y)]
		indexOfCurPosX=(x0-self.width)/self.wOB
		indexOfCurPosY=((y0+self.height)/self.wOB)-1
		if (indexOfCurPosX,indexOfCurPosY) in illegalCells:
			return False
		else: return True

	def stepFn(self):
		x0,y0,level=self.x,self.y,self.level
		if Player.isLegal(self,x0,y0+self.wOB):
			self.y+=self.gravity

	def moveFn(self,event):
		if (event.keysym=="Right"):
			if Player.isLegal(self,self.x+25,self.y):
				self.x+=25
		elif (event.keysym=="Left"):
			if Player.isLegal(self,self.x-25,self.y):
				self.x-=25
		elif (event.keysym=="space"):
			if Player.isLegal(self,self.x,self.y-50):
				self.y-=50
