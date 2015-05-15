import eventBasedAnimation
from Tkinter import *
from Levels import *
from Player import *
class Portal(object):
	def __init__(self,x0,y0,level,mouseXB,mouseYB,mouseXO,mouseYO,portalType):
		(w,h,wOB,wGrid,hGrid,levelGrid)=800,500,50,20,12,[]
		self.hGrid,self.wGrid,self.wOB=hGrid,wGrid,wOB
		self.mouseXB,self.mouseYB=mouseXB,mouseYB
		self.mouseXO,self.mouseYO,self.portalType=mouseXO,mouseYO,portalType
		self.Playerh,self.Playerw=20,15
		self.level=level
		self.curLevel=eval("Levels.Level%d(w,h,wGrid,hGrid,levelGrid)"\
																%self.level)
		self.levelGrid=self.curLevel.setBoard()
		self.bPortalCoordXB, self.bPortalCoordYB= 0, 0
		self.oPortalCoordXO, self.oPortalCoordYO= 0, 0
		self.pX=Player(x0,y0,level).x
		self.pY=Player(x0,y0,level).y
		self.x0,self.y0=x0,y0

	def drawPortal(self,canvas):
		x0,y0,level,portalType=self.x0,self.y0,self.level,self.portalType
		mXB,mYB,mXO,mYO=self.mouseXB,self.mouseYB,self.mouseXO,self.mouseYO
		wOB=self.wOB
		iofMouseXB,iofMouseYB=mXB/self.wOB,(mYB/self.wOB)
		iofMouseXO,iofMouseYO=mXO/self.wOB,(mYO/self.wOB)
		(w,h,wOB,wGrid,hGrid,levelGrid)=800,500,50,20,12,[]
		self.bPortalCoordXB,self.bPortalCoordYB=iofMouseXB,iofMouseYB
		self.oPortalCoordXO,self.oPortalCoordYO=iofMouseXO,iofMouseYO
		if self.portalType=="B":
			self.levelGrid[iofMouseYB][iofMouseXB][4]=1
			self.levelGrid[iofMouseYO][iofMouseXO][5]=1
			levelGrid=self.levelGrid
			self.curLevel.drawFn(canvas)
		elif self.portalType=="O":
			self.levelGrid[iofMouseYB][iofMouseXB][4]=1
			self.levelGrid[iofMouseYO][iofMouseXO][5]=1
			levelGrid=self.levelGrid
			self.curLevel.drawFn(canvas)

	def mouseFn(self,event):
		x0,y0,level,portalType=self.x0,self.y0,self.level,self.portalType
		mXB,mYB=self.mouseXB,self.mouseYB
		mXB,mYB,wOB=self.mouseXO,self.mouseYO,self.wOB
		self.mouseX, self.mouseY = event.x, event.y

	def isInPortal(self):
		x0,y0=self.pX,self.pY
		pW,pH=self.Playerw,self.Playerh
		mXB,mYB=self.mouseXB,self.mouseYB
		iofMouseXB,iofMouseYB=mXB/self.wOB,(mYB/self.wOB)
		indexOfCurPosX=((x0-self.Playerw)/self.wOB)+1
		indexOfCurPosY=((y0+self.Playerh)/self.wOB)-1
		if (indexOfCurPosX,indexOfCurPosY)==\
		                          (self.bPortalCoordXB,self.bPortalCoordYB):
		  return True
		else: return False
