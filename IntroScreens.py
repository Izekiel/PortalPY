import eventBasedAnimation
from Tkinter import *
from Levels import *
from Player import *
class IntroScreens(object):
	def __init__(self,states,w,h):
		self.states=states
		self.w,self.h=w,h
		self.curState=states[0]
		self.clickedInIntroBox=False
		self.clickedInInstrBox=False
		self.btnBounds=[(w/2)-110,((4*h)/5)-5,(w/2)+110,(6*h)/7]
		self.btnBounds2=[(w/2)-110,((4*h)/5)-55,(w/2)+110,((6*h)/7)-50]

	def drawIntro(self,canvas):
		w,h=self.w,self.h
		states=self.states
		title="PortalPy"
		titleFont="Arial "+str(h/4)+" bold"
		nxtBtn="Click here to continue"
		nxtBtnFont="Arial 20 bold"
		btnBound=self.btnBounds
		canvas.create_rectangle(0,0,w/2,h,fill="dark orange")
		canvas.create_rectangle(w/2,0,w,h,fill="deep sky blue")
		canvas.create_oval(w/5,h/4,w/4,(3*h)/4,fill="black")
		canvas.create_oval((w/5)+600,h/4,(w/4)+600,(3*h)/4,fill="black")
		canvas.create_text(w/5,h/3,text=title,font=titleFont,anchor=NW)
		canvas.create_rectangle(btnBound[0],btnBound[1],btnBound[2]
												,btnBound[3],fill="green")
		canvas.create_text((w/2)-105,(4*h)/5,text=nxtBtn,
												font=nxtBtnFont,anchor=NW)
		if self.clickedInIntroBox==True:
			self.curState=self.states[1]
			IntroScreens(states,w,h).drawInstr(canvas)


	def drawInstr(self,canvas):
		w,h=self.w,self.h
		states=self.states
		cmds=["Side Arrow Keys","Space","'B'+Click","'O'+Click","What to do",
			"","When (and if) you win, you will receive the Py!"]
		actions=["Move","Jump","Draw a blue portal","Draw an orange portal",
			"Get the little red player from the\ndark blue square to the "+
			"dark red one","",""]
		font="Arial 20 bold"
		title,titleFont="Instructions","Arial 30 bold"
		nxtBtn="Got it. Let's Begin!"
		nxtBtnFont="Arial 20 bold"
		btnBound=self.btnBounds
		btnBound2=self.btnBounds2
		leftSpacing=200
		rightSpacing=50
		space=40
		canvas.create_rectangle(0,0,w/2,h,fill="dark orange")
		canvas.create_rectangle(w/2,0,w,h,fill="deep sky blue")
		canvas.create_text((w/2)-75,h/6,text=title,font=titleFont,anchor=NW)
		for x in xrange(len(cmds)):
			canvas.create_text((w/2)-leftSpacing,(h/4)+(x*space),
									text=cmds[x],font=font,anchor=NW)
			canvas.create_text((w/2)+rightSpacing,(h/4)+(x*space),
									text=actions[x],font=font,anchor=NW)
			# canvas.create_text((w/2)-leftSpacing,(h/4)+(x*space),
			# 						text=cmds[x],font=font,anchor=NW)
		canvas.create_rectangle(btnBound2[0],btnBound2[1],btnBound2[2]
												,btnBound2[3],fill="green")
		canvas.create_text((w/2)-105,((4*h)/5)-50,text=nxtBtn,
												font=nxtBtnFont,anchor=NW)
		if self.clickedInInstrBox==True:
			self.curState=self.states[2]

	def mouseIntroFn(self,event):
		w,h=self.w,self.h
		x,y=event.x,event.y
		states=self.states
		btnBound=self.btnBounds
		if btnBound[0]<=x<=btnBound[2] and btnBound[1]<=y<=btnBound[3]:
			self.clickedInIntroBox=True
			IntroScreens(states,w,h).mouseInstrFn(event)

	def mouseInstrFn(self,event):
		w,h=self.w,self.h
		x,y=event.x,event.y
		states=self.states
		btnBound=self.btnBounds2
		if btnBound[0]<=x<=btnBound[2] and btnBound[1]<=y<=btnBound[3]:
			self.clickedInInstrBox=True
			self.curState=self.states[2]

	def drawEnd(self,canvas):
		w,h=self.w,self.h
		canvas.create_rectangle(0,0,w,h,fill="white")
		endText=["The Py was a lie!","But you still finished the game"+
		" and that's something to be proud of","...right?"]
		endFont=["Arial 100 bold","Arial 20 bold"]
		canvas.create_text((w/8),h/6,text=endText[0],font=endFont[0],anchor=NW)
		canvas.create_text((w/4),h/2,text=endText[1],font=endFont[1],anchor=NW)
		canvas.create_text((5*w)/6,(3*h)/4,text=endText[2],font=endFont[1]
														,anchor=NW)




