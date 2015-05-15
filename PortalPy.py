#PortalPy.py
#Isaac Barreto + ibb + O
import eventBasedAnimation
from Tkinter import *
from Levels import *
from Player import *
from Portal import *
from IntroScreens import *
'''
--Clear screen after the level
--Make more Levels/Get the levels to change properly 
--Maybe implement a timer so that you can "lose"
--Add background music
--add images
--add an instruction or two in case the user has never played portal before

'''
##############################################################################
##############################################################################
																			  
		#####                               ##                    ##
		##  ##                              ##                    ##
		##    ##                            ##                    ##
		##     ##                           ##                    ##
		##    ##                            ##                    ##
		##   ##                             ##                    ##
		#####        #####     ##  ###    ######     #####        ##
		##          ##   ##    ####  ##     ##      ##   ###      ##  
		##         ##     ##   ##           ##     ##     ###     ##
		##          ##   ##    ##           ##      ##   ## ##    ##
		##           #####     ##           ##       #####   ##   ##

##############################################################################
##############################################################################

class PortalPy(eventBasedAnimation.Animation):
	def onInit(self,level=1):
		(w,h,wOB,wGrid,hGrid,levelGrid)=1000,600,50,20,12,[]
		self.wOB=wOB
		self.hGrid,self.wGrid=hGrid,wGrid
		self.w,self.h=w,h
		self.Playerh,self.Playerw=20,15
		self.level=level
		self.curLevel=eval("Levels.Level%d(w,h,wGrid,hGrid,levelGrid)"\
																%self.level)
		levelGrid=self.levelGrid=self.curLevel.setBoard()
		for y in xrange(hGrid):
				for x in xrange(wGrid):
					if levelGrid[y][x][2]==1: 
						x0,y0=x*wOB+self.Playerw,(y+1)*wOB-20
					if levelGrid[y][x][3]==1: 
						xF,yF=x*wOB,y*wOB
		self.x0,self.y0=x0,y0
		self.xF,self.yF=xF,yF
		self.player=Player(x0,y0,level)
		self.playerLocX=Player(x0,y0,level).x
		self.playerLocY=Player(x0,y0,level).y
		self.mouseXB,self.mouseYB=0,0
		self.mouseXO,self.mouseYO,self.portalType=0,0,"B"
		self.portal=Portal(x0,y0,level,self.mouseXB,self.mouseYB,self.mouseXO\
										,self.mouseYO,self.portalType)
		self.indexOfCurPosX=(x0-self.Playerw)/wOB
		self.indexOfCurPosY=((y0+self.Playerh)/wOB)-1
		self.keyEvents=""
		self.lastCoords=[[0,0,"B"],[0,0,"O"]]
		self.introScreensStates=states=["Intro","Instr","Game","End"]
		self.introScreens=IntroScreens(states,w,h)
		self.curState=IntroScreens(states,w,h).curState
		self.gameOver=False

	def onStep(self):
		x0,y0,level,wOB=self.player.x,self.player.y,self.level,self.wOB
		mXB,mYB,mXO,mYO=self.mouseXB,self.mouseYB,self.mouseXO,self.mouseYO
		portalType=self.portalType
		pW,pH=self.Playerw,self.Playerh
		oPLocXO=((mXO/wOB)*wOB)+pW
		oPLocYO=(((mYO/wOB)+1)*wOB)-pH
		self.player.stepFn()
		if PortalPy.isLegal(self,x0,y0+self.wOB):
			self.y0+=25
		if PortalPy.isInPortal(self):
			self.player=Player(oPLocXO,oPLocYO,level)
		self.curState=self.introScreens.curState

	def isInPortal(self):
		x0,y0,level,wOB=self.player.x,self.player.y,self.level,self.wOB
		mXB,mYB,mXO,mYO=self.mouseXB,self.mouseYB,self.mouseXO,self.mouseYO
		portalType=self.portalType
		pW,pH=self.Playerw,self.Playerh
		iofMouseXB,iofMouseYB=mXB/self.wOB,(mYB/self.wOB)
		indexOfCurPosX=((x0-self.Playerw)/self.wOB)
		indexOfCurPosY=((y0+self.Playerh)/self.wOB)-1
		if (indexOfCurPosX,indexOfCurPosY)==(iofMouseXB,iofMouseYB):
			return True
		else: 
			return False


	def onDraw(self, canvas):
		# self.Levels.drawFn(canvas)
		if self.curState=="Intro":
			self.introScreens.drawIntro(canvas)
		elif self.curState=="Instr":
			self.introScreens.drawInstr(canvas)
		elif self.curState=="Game":
			x0,y0,level,wOB=self.player.x,self.player.y,self.level,self.wOB
			x1,y1=self.mouseXB,self.mouseYB
			self.curLevel.drawFn(canvas)
			self.portal.drawPortal(canvas)
			self.player.drawFn(canvas)
		if PortalPy.levelOver(self,self.player.x,self.player.y):
			self.introScreens.drawEnd(canvas)


	def isLegal(self,x0,y0):
		illegalCells=[]
		for y in xrange(self.hGrid):
				for x in xrange(self.wGrid):
					if self.levelGrid[y][x][0]==1 or \
											self.levelGrid[y][x][1]==1:
						illegalCells+=[(x,y)]
		indexOfCurPosX=(x0-self.Playerw)/self.wOB
		indexOfCurPosY=((y0+self.Playerh)/self.wOB)-1
		if (indexOfCurPosX,indexOfCurPosY) in illegalCells:
			return False
		else: return True

	def levelOver(self,x0,y0):
		x0,y0,level=self.player.x,self.player.y,self.level
		if self.xF<=x0<=self.xF+self.wOB and self.yF<=y0<=self.yF+self.wOB:
			return True
		else: return False

	def onKey(self, event):
		self.player.moveFn(event)
		w,h,wGrid,hGrid,levelGrid=self.w,self.h,self.wGrid,self.hGrid,self.levelGrid
		x0,y0,level=self.player.x,self.player.y,self.level
		self.indexOfCurPosX=(x0-self.Playerw)/self.wOB
		self.indexOfCurPosY=((y0+self.Playerh)/self.wOB)-1
		if (event.keysym=="b"):
			self.portalType="B"
		elif (event.keysym=="o"):
			self.portalType="O"
		# if PortalPy.levelOver(self,x0,y0):
			# print "Congrats!!!"
			# self.gameOver=True
			# if self.gameOver==True:
			# 	self.gameOver=False
			# 	self.level+=1
			# 	print self.level
				# self.curLevel=eval("Levels.Level%d(w,h,wGrid,hGrid,levelGrid)"\
																# %self.level)
			# PortalPy(self.level)

	def onMouse(self,event):
		self.portal.mouseFn(event)
		mX,mY=event.x,event.y
		x0,y0,level,wOB=self.player.x,self.player.y,self.level,self.wOB
		self.lastCoords+=[[mX,mY]]
		if self.portalType=="B":
			self.lastCoords[-1:][0]+=["B"]
			for x in xrange(len(self.lastCoords)):
				if self.lastCoords[x][2]=="O":
					mXO,mYO=self.lastCoords[x][0],self.lastCoords[x][1]
			mXB,mYB=mX,mY
			self.mouseXB,self.mouseYB=mXB,mYB
			self.mouseXO,self.mouseYO=mXO,mYO
			self.mouseXB,self.mouseYB=mXB,mYB
			self.mouseXO,self.mouseYO=mXO,mYO
			self.portal=Portal(x0,y0,level,mXB,mYB,mXO,mYO,"B")
		elif self.portalType=="O":
			self.lastCoords[-1:][0]+=["O"]
			for x in xrange(len(self.lastCoords)):
				if self.lastCoords[x][2]=="B":
					mXB,mYB=self.lastCoords[x][0],self.lastCoords[x][1]
			mXO,mYO=mX,mY
			self.mouseXB,self.mouseYB=mXB,mYB
			self.mouseXO,self.mouseYO=mXO,mYO
			self.portal=Portal(x0,y0,level,mXB,mYB,mXO,mYO,"O")
		self.introScreens.mouseIntroFn(event)
		if self.introScreens.clickedInIntroBox==True:
			self.introScreens.mouseInstrFn(event)


PortalPy(width=1000,height=600,timerDelay=64).run()
