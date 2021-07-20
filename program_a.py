import image
import time


def rgb_to_gray(img: image.Image):
    win = image.ImageWin(img.get_width(), img.get_height())
    emg = img.copy()
    for col in range(emg.get_width()):
        for row in range(emg.get_height()):
            p = emg.get_pixel(col, row)
            R = p.getRed()
            G = p.getGreen()
            B = p.getBlue()
            emgGray = (R + G + B)//3

            new_pixel = image.Pixel(emgGray, emgGray, emgGray)

            emg.set_pixel(col, row, new_pixel)

    emg.draw(win)
    win.exit_on_click()
    emg.save('gray.gif')

def negate_img(img: image.Image):
    win = image.ImageWin(img.get_width(), img.get_height())
    emg = img.copy()
    for col in range(emg.get_width()):
        for row in range(emg.get_height()):
            p = emg.get_pixel(col, row)
            R = 255-p.getRed()
            G = 255-p.getGreen()
            B = 255-p.getBlue()

            new_pixel = image.Pixel(R, G, B)

            emg.set_pixel(col, row, new_pixel)

    emg.draw(win)
    win.exit_on_click()
    emg.save('negated.gif')

def filter_out_red(img: image.Image):
    win = image.ImageWin(img.get_width(), img.get_height())
    emg = img.copy()
    for col in range(emg.get_width()):
        for row in range(emg.get_height()):
            p = emg.get_pixel(col, row)
            R = 0
            G = p.getGreen()
            B = p.getBlue()

            new_pixel = image.Pixel(R, G, B)

            emg.set_pixel(col, row, new_pixel)

    emg.draw(win)
    win.exit_on_click()
    emg.save('fRed.gif')

def filter_out_green(img: image.Image):
    win = image.ImageWin(img.get_width(), img.get_height())
    emg = img.copy()
    for col in range(emg.get_width()):
        for row in range(emg.get_height()):
            p = emg.get_pixel(col, row)
            R = p.getRed()
            G = 0
            B = p.getBlue()

            new_pixel = image.Pixel(R, G, B)

            emg.set_pixel(col, row, new_pixel)

    emg.draw(win)
    win.exit_on_click()
    emg.save('fGreen.gif')

def filter_out_blue(img: image.Image):
    win = image.ImageWin(img.get_width(), img.get_height())
    emg = img.copy()
    for col in range(emg.get_width()):
        for row in range(emg.get_height()):
            p = emg.get_pixel(col, row)
            R = p.getRed()
            G = p.getGreen()
            B = 0

            new_pixel = image.Pixel(R, G, B)

            emg.set_pixel(col, row, new_pixel)

    emg.draw(win)
    win.exit_on_click()
    emg.save('fBlue.gif')

def sepia_tone(img: image.Image):
    win = image.ImageWin(img.get_width(), img.get_height())
    emg = img.copy()
    for col in range(emg.get_width()):
        for row in range(emg.get_height()):
            p = emg.get_pixel(col, row)
            R = p.getRed()
            G = p.getGreen()
            B = p.getBlue()
            newR = int(R * 0.393 + G * 0.769 + B * 0.189)
            newG = int(R * 0.349 + G * 0.686 + B * 0.168)
            newB = int(R * 0.272 + G * 0.534 + B * 0.131)
            if newR > 255:
                newR = 255

            if newG > 255:
                newG = 255

            if newB > 255:
                newB = 255

            new_pixel = image.Pixel(newR, newG, newB)

            emg.set_pixel(col, row, new_pixel)

    emg.draw(win)
    win.exit_on_click()
    emg.save('sepia.gif')


if __name__ == '__main__':
    img_path = 'birdCatchesBee.jpg'
    img_path2 = 'taalVolcanoLightning.jpg'

    choice_img = input('Which Image? == ')
    if choice_img == '1':
        temp_path = img_path
    elif choice_img == '2':
        temp_path = img_path2
    else:
        temp_path = img_path
        print('Shit')

    i = image.Image(temp_path)

    value = input("input here:\n")

    if value == "grayscale":
        rgb_to_gray(i)
    elif value == "negate":
        negate_img(i)
    elif value == "filterRed":
        filter_out_red(i)

    elif value == "filterGreen":
        filter_out_green(i)

    elif value == "filterBlue":
        filter_out_blue(i)
    
    elif value == "sepiaTone":
        sepia_tone(i)

    else:
        print("bhudddddddaaaaaaaa")