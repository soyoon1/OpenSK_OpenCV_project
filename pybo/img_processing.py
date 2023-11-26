import numpy as np
import cv2 as cv

def embossing(img):
    femboss=np.array([[-1.0, 0.0, 0.0],
                      [ 0.0, 0.0, 0.0],
                      [ 0.0, 0.0, 1.0]]) # 3X3 필터 이렇게 선언해주고 있다.

    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray16=np.int16(gray) # gray는 1바이트(8bits) => 16bit int8로 음수를 표현하는 경우 -128 ~ 127까지만 표현 가능
    emboss=np.uint8(np.clip(cv.filter2D(gray16,-1,femboss)+128,0,255)) # 0보다 작으면 0, 255보다 크면 255
    return emboss


def cartoon(img):
    cartoon = cv.stylization(img, sigma_s=60, sigma_r=0.45)
    return cartoon # 출력 영상

def pencilGray(img):
    sketch_gray, _ = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_gray

def pencilColor(img):
    _, sketch_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_color

def oilPainting(img):
    oil = cv.xphoto.oilPainting(img, 10, 1, cv.COLOR_BGR2Lab)
    return oil

def detailEnhance(img):
    detail = cv.detailEnhance(img,  sigma_s=10, sigma_r=0.15) # sigma_s : 더 많이 블러링 됨. 다른 애들보다 덜 부드러워짐. sigma_r: 에지 부분을 더 세밀하게 표시해준다.
    return detail

# def cartoonFunction(self):
#     self.cartoon = cv.stylization(self.img, sigma_s=60,
#                                   sigma_r=0.45)  # defualt 값으로 주어진 값이다. 비교적 효과를 잘 나타내는 값이다. 영상마다 효과가 다를 수 있기 때문에 값은 수정가능하다.
#     cv.imshow('Cartoon', self.cartoon)
#
# def sketchFunction(self):
#     self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07,
#                                                           shade_factor=0.02)  # 첫번쨰 리턴값: grap스타일로 펜슬 스케치, 하나는 칼라형태로 펜슬 스케치한 결과
#     cv.imshow('Pencil sketch(gray)', self.sketch_gray)
#     cv.imshow('Pencil sketch(color)', self.sketch_color)
#
# def oilFunction(self):
#     self.oil = cv.xphoto.oilPainting(self.img, 10, 1,
#                                      cv.COLOR_BGR2Lab)  # 오일 페인팅 효과를 보여줌. BGR이 있다면 그 중 첫번째 채녈 B를 기준으로 해서 실행됨 -> 딱히 근거는 없음. 오일 페인팅은 그냥 제일 첫번째를 기준으로 해준다. RGB 중요성 다 동등하다.
#     cv.imshow('Oil painting',
#               self.oil)  # HSV: V는 빛의 정도를 표현하고 HS로 색상을 표현한다. 그래서 빛의 정도를 더 표현할 수 있는 방법이다. YCbCr: Y가 그레이 값이다. Cb와 Cr로 색상을 표현해준다. L이 빛의 정도를 나타내고 ab로 색상을 나타냄.
