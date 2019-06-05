import matplotlib.pyplot as plt
import skimage.exposure as ex
from numpy import meshgrid
from numpy.fft import fft2, fftshift, ifft2
from PIL import Image
from skimage import io

def _bw_high(x, y, D=15):
    return 1 - 1 / (1 + ((x ** 2 + y ** 2) / D ** 2) ** 2)

def filter_img(imgpath, wc):
    imgarray = io.imread(imgpath, as_gray=True)
    ar1 = range(-imgarray.shape[1]//2, imgarray.shape[1]//2)
    ar2 = range(-imgarray.shape[0]//2, imgarray.shape[0]//2)
    x, y = meshgrid(ar1, ar2)

    bh = _bw_high(x, y, wc)
    cf = fftshift(fft2(imgarray))
    cfbh = cf * bh

    io.imshow(ex.rescale_intensity(abs(ifft2(cfbh)), out_range=(0.0, 1.0)))
    # Filtros FIR, Hamming, Gaussian
    # ax = plt.gca()
    # ax.axes.get_xaxis().set_visible(False)
    # ax.axes.get_yaxis().set_visible(False)
    # plt.get_current_fig_manager().frame.Maximize(True)
    plt.savefig('resultado.png')