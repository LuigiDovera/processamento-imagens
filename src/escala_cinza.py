from PIL import Image
from utils import in_file, out_file
import cv2


# Escala de Cinza: https://youtu.be/_3VcRHwZpPU
def media_grayscale(colored):
    h, w, c = colored.shape
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored[x, y]
            # média das coordenadas RGB
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x,y), (lum, lum, lum))
    return img

# Escala de Cinza: https://youtu.be/_3VcRHwZpPU
def grayscale(colored):
    h, w, c = colored.shape
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored[x, y]
            # média ponderada das coordenadas RGB
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            #eu sei lá bixo
            img.putpixel((x,y), (lum, lum, lum))
    return img
            

if __name__ == "__main__":
    #img = Image.open(in_file("baloes.jpg"))
    img = cv2.imread(in_file("baloes.jpg"))

    # print(img.getpixel((100, 100)))
    # print(img.getpixel((500, 300)))
    # print(img.getpixel((300, 180)))

    # pb_baloes = grayscale(baloes)
    # pb_baloes.save(out_file("pb_baloes2.jpg"))
    #grayscale(img).save(out_file("pb-baloes.jpg"))
    #grayscale(img).show()
    cv2.imshow("gs", grayscale(img))

    cv2.waitKey(0)
    