import streamlit as st
import cv2

run=st.checkbox('run')
frame_window=st.image([])
cam=cv2.VideoCapture(0)
while run:
	ret,frame=cam.read()
	#frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame_window.image(frame)
	frame_window.image(frame)
else:
	st.write('stopped')
