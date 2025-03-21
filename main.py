import cv2
import numpy as np
import math

img = cv2.imread(r'D:\SR_Works\2nd_Task\Q2\angle2.png')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gblur = cv2.GaussianBlur(grayimg, (5,5), 0)
ret, thresh = cv2.threshold(gblur, 127, 255, cv2.THRESH_BINARY_INV)
# edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(thresh, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=30)

detected_lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    detected_lines.append(((x1, y1), (x2, y2)))
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.circle(img,(x1,y1),5, (0,0,255), 1)
    cv2.circle(img,(x2,y2),5, (0,0,255), 1)

def calculate_angle(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    m1 = math.atan2(y2 - y1, x2 - x1)
    m2 = math.atan2(y4 - y3, x4 - x3)
    angle = abs(math.degrees(m1 - m2))
    return angle if angle <= 90 else 180 - angle

if len(detected_lines) > 1:
    angle = calculate_angle(detected_lines[0], detected_lines[1])
    print(f"Angle: {angle:.2f}°")
cv2.putText(img, f"Angle : {angle:.2f}", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
cv2.imshow("Detected Lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
