from datetime import datetime
from Evento import Evento
from Ingresso import Ingresso
from Participante import Participante

def main():
    evento1 = Evento("evento 1", "estádio 1", datetime(2023, 8, 25, 20, 30),10)
    evento2 = Evento("evento 2", "estádio 2", datetime(2023, 8, 26, 21, 30),20)
    evento3 = Evento("evento 3", "estádio 3", datetime(2023, 8, 27, 22, 30),30)

    participante1 = Participante("João", "joao@gmail.com")
    participante2 = Participante("Paulo", "paulo@gmail.com")
    participante3 = Participante("Mario", "mario@gmail.com")

    participante1.comprarIngresso(evento1)
    participante1.comprarIngresso(evento2)
    participante1.comprarIngresso(evento3)
    participante2.comprarIngresso(evento3)
    participante2.comprarIngresso(evento2)
    participante3.comprarIngresso(evento3)
    print("***********************")
    participante1.mostrarIngressosParticipantes()
    participante2.mostrarIngressosParticipantes()
    participante3.mostrarIngressosParticipantes()
    print("***********************")
    evento1.mostrarInfoEvento()
    print("***********************")
    evento1.cancelarEvento()
    print("***********************")
    participante1.mostrarIngressosParticipantes()
    

    

if __name__=="__main__":
    main()