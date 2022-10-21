
#importe as bibliotecas
from math import pi, sin
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs=44100
freqs={ '1':(697,1209),'2':(697,1336),'3':(697,1477),'A':(697,1633),
        '4':(770,1209),'5':(770,1336),'6':(770,1477),'B':(770,1633),
        '7':(852,1209),'8':(852,1336),'9':(852,1477),'C':(852,1633),
        'X':(941,1209),'0':(941,1336),'#':(941,1477),'D':(941,1633)}

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em dB, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def build_senoide(freq,time_array):
    A=1
    return A*sin(2*pi*freq*time_array)

myFn = np.vectorize(build_senoide, excluded=['freq'])

def build_tone(tecla,t):
    time_array=np.linspace(0,t,(44100*t)+1)
    return myFn(freqs[tecla][0],time_array)+myFn(freqs[tecla][1],time_array)




def main():
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias correspondentes à tecla pressionada, segundo a tabela DTMF
    # Essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # Lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # O tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Construa com amplitude 1.
    # Some as senoides. A soma será o sinal a ser emitido.
    # Utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumentos.
    # Grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    
    NUM=input('Digite a tecla: ')
    while NUM not in freqs.keys():
        NUM=input('Digite uma tecla válida: ')
        
    tone = build_tone(NUM,1)
    
    

    print("Inicializando encoder")
    print("Aguardando usuário")
    print("Gerando Tons base")
    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(NUM))
    sd.play(tone, fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()
    signal=signalMeu()
    signal.plotFFT(tone, fs)
    

if __name__ == "__main__":
    main()
