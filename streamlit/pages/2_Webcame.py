import cv2
import math
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.write("# Let's detect the Waste 🗑️")
st.write("Welcome to Garbage Detection WebApp ! You wana to try garbage detection in live feed 🎥 we got you!")
st.write("Together, let's take a step towards a cleaner environment.")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1597655601841-214a4cfe8b2c?q=80&w=1889&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
    background-color: rgba(255, 255, 255, 1);
}
[data-testid=stSidebar] {
        background-color: #5888c6;
    }
</style>
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def predict(img):
    model = YOLO(r"F:\Desktop\Projects\Waste Detection\runs\detect\YOLOv8Model\weights\best.pt")
    results = model(img,stream=True)
    classNames = ['BIODEGRADABLE', 'CARDBOARD', 'GLASS', 'METAL', 'PAPER', 'PLASTIC']
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
            w, h = x2-x1,y2-y1

            cv2.rectangle(img,(x1, y1), (x2, y2),color=(255,0,0), thickness=2)
            conf = math.ceil((box.conf[0]*100))/100
            cls = box.cls[0]
            print(conf)
            name = classNames[int(cls)]

            cv2.putText(img,f"{name} {conf}",(max(0,x1), max(35,y1)),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,150,0),1)
    return img

def main_loop():
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    with col1: 
        start_button = st.button("Start")
    with col3:
        stop_button = st.button("Stop")
    if start_button:
        while cap.isOpened() and not stop_button:
            ret, frame = cap.read()
            if not ret:
                st.write("Video Capture Ended")
                break
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            predict_img = predict(img)
            with col2:
                frame_placeholder.image(predict_img,channels="RGB")
            if cv2.waitKey(1) & 0xFF == ord("q") or stop_button:
                break
        cap.release()
        cv2.destroyAllWindows()

col1, col2, col3 = st.columns([1,6,1])
if __name__ == "__main__":
    main_loop()