import matplotlib.pyplot as plt
import skimage.exposure as ex
from numpy import meshgrid
from numpy.fft import fft2, fftshift, ifft2
from PIL import Image
from skimage import io

def _bw_high(x, y, D=15):
    #Aplicacion de la formula para el filtro de Butterworth
    return 1 - 1 / (1 + ((x ** 2 + y ** 2) / D ** 2) ** 2)

def filter_img(imgpath, wc):
    #lee la imagen correspondiente
    imgarray = io.imread(imgpath, as_gray=True)
    #Generación del rango de (-Ancho/2,Ancho/2)
    ar1 = range(-imgarray.shape[1]//2, imgarray.shape[1]//2)
    #Generación del rango de (-Alto/2,Alto/2)
    ar2 = range(-imgarray.shape[0]//2, imgarray.shape[0]//2)
    #Crea maya rectangular con los valores de los rangos ar1 y ar2
    x, y = meshgrid(ar1, ar2)
    #Ejecuta el filtro del Butterworth
    bh = _bw_high(x, y, wc)
    #FFT2 Ejecuta la transformada de dos dimensiones sobre la imagen
    #FFSHIFT Mueve los componentes de frecuencia ceros al centro del espectro de la transformada
    cf = fftshift(fft2(imgarray))
    #Convoluciona la máscara de Butterworth con la transformada de la imagen
    cfbh = cf * bh
    #Genera la transformada inversa de la imagen convolucionada y se toman los valores absolutos para descartar solo los valores reales positivos
    io.imshow(ex.rescale_intensity(abs(ifft2(cfbh)), out_range=(0.0, 1.0)))
    # Guarda el resultado
    plt.savefig('resultado.png')