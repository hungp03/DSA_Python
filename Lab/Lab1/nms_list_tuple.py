# -*- coding: utf-8 -*-
"""4.1 NMS_List_Tuple.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tEBPUpzZmUU7N7oc_jK-Gx8rT3IXM0MM

Hàm non_max_suppression(boxes, overlapThresh) thực hiện thuật toán Non-Maximum Suppression (NMS) để loại bỏ các hộp giới hạn dư thừa dựa trên một ngưỡng trùng lắp.

boxes là một mảng 2D chứa các hộp giới hạn. Mỗi hàng của mảng này biểu diễn một hộp giới hạn và có 5 cột: tọa độ x1, y1 (góc trái trên), tọa độ x2, y2 (góc phải dưới) và điểm confidence của hộp giới hạn.

overlapThresh là ngưỡng trùng lắp dùng để quyết định liệu hai hộp giới hạn có nên được giữ lại hay không.


Khởi tạo danh sách pick để lưu trữ chỉ mục của các hộp giới hạn được giữ lại.

Tính toán diện tích của từng hộp giới hạn.

Sắp xếp các hộp giới hạn theo điểm confidence từ thấp đến cao.

Lặp qua các hộp giới hạn theo thứ tự đã sắp xếp:

Thêm chỉ mục của hộp giới hạn hiện tại vào danh sách pick.

Tính toán phần giao của hộp giới hạn hiện tại với các hộp giới hạn còn lại.

Loại bỏ các hộp giới hạn có trùng lắp với hộp giới hạn hiện tại lớn hơn hoặc bằng overlapThresh.

Trả về danh sách chỉ mục của các hộp giới hạn được giữ lại sau khi áp dụng NMS.

Hàm này trả về một mảng 2D chứa các hộp giới hạn sau khi áp dụng NMS, với mỗi hàng của mảng biểu diễn một hộp giới hạn được giữ lại.
"""

def non_max_suppression(boxes, overlapThresh):
    # if there are no boxes, return an empty list
    if len(boxes) == 0:
        return []

    # initialize the list of picked indexes
    pick = []
    # grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    c = boxes[:, 4]
    # compute the area of the bounding boxes and sort the bounding
    # boxes by the bottom-right y-coordinate of the bounding box
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(c)
    # keep looping while some indexes still remain in the indexes
    # list
    while len(idxs) > 0:
        # grab the last index in the indexes list and add the
        # index value to the list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        # find the largest (x, y) coordinates for the start of
        # the bounding box and the smallest (x, y) coordinates
        # for the end of the bounding box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])
        # compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        # compute the ratio of overlap
        overlap = (w * h) / area[idxs[:last]]
        # delete all indexes from the index list that have
        idxs = np.delete(idxs, np.concatenate(([last],
                                               np.where(overlap > overlapThresh)[0])))
    # return only the bounding boxes that were picked using the
    # integer data type
    return boxes[pick].astype("int")

"""sử dụng hàm non_max_suppression() để loại bỏ các hộp giới hạn dư thừa và vẽ các hộp giới hạn được giữ lại lên hình ảnh.

boundingBoxes là một mảng numpy chứa các hộp giới hạn. Mỗi hàng của mảng này biểu diễn một hộp giới hạn và có 5 cột: tọa độ x1, y1 (góc trái trên), tọa độ x2, y2 (góc phải dưới) và điểm confidence của hộp giới hạn.

Đầu tiên, hình ảnh được sao chép vào biến orig.

Sau đó, một vòng lặp duyệt qua từng hộp giới hạn trong boundingBoxes và vẽ chúng lên hình ảnh orig với màu đỏ.

Hàm non_max_suppression() được gọi để loại bỏ các hộp giới hạn dư thừa dựa trên một ngưỡng trùng lắp là 0.3.

Hình ảnh cuối cùng được hiển thị với các hộp giới hạn được giữ lại sau khi áp dụng NMS với màu xanh lá cây.

Kết quả là hai hình ảnh, một có các hộp giới hạn trước khi áp dụng NMS và một có các hộp giới hạn sau khi áp dụng NMS, với các hộp giới hạn dư thừa đã bị loại bỏ.
"""

# import the necessary packages
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

boundingBoxes = np.array([
	(12, 84, 140, 212, 0.3),
	(24, 84, 152, 212, 0.4),
	(36, 84, 164, 212, 0.5),
	(12, 96, 140, 224, 0.6),
	(24, 96, 152, 224, 0.7),
	(24, 108, 152, 236, 0.8)])

# load the image and clone it
image = cv2.imread("/content/cat_nms.png")
orig = image.copy()
# loop over the bounding boxes for each image and draw them
for (startX, startY, endX, endY, confidence) in boundingBoxes:
	cv2.rectangle(orig, (int(startX), int(startY)), (int(endX), int(endY)), (0, 0, 255), 2)
# perform non-maximum suppression on the bounding boxes
pick = non_max_suppression(boundingBoxes, 0.3)
# loop over the picked bounding boxes and draw them
for (startX, startY, endX, endY, confidence) in pick:
   print(startX,startY,endX,endY)
   cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# display the images
cv2_imshow(orig)
cv2_imshow(image)