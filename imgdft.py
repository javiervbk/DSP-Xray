import skimage.exposure as ex
from numpy import meshgrid
from numpy.fft import fft2, fftshift, ifft2
from PIL import Image
from skimage import io

def _bw_high(x, y, D=15):
    return 1 - 1 / (1 + ((x ** 2 + y ** 2) / D ** 2) ** 2)

def filter_img(imgpath, wc):
    imgarray = io.imread(imgpath)
    ar1 = range(-imgarray.shape[1]//2, imgarray.shape[1]//2)
    ar2 = range(-imgarray.shape[0]//2, imgarray.shape[0]//2)
    x, y = meshgrid(ar1, ar2)

    bh = _bw_high(x, y, wc)
    cf = fftshift(fft2(imgarray))
    cfbh = cf * bh

    imgarray = abs(ifft2(cfbh))
    img = Image.fromarray(imgarray, 'L')
    img.save('resultado.png')