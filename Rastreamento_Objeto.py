# Importa a biblioteca OpenCV e exibe a versão
import cv2
print(cv2.__version__)

# Cria um objeto de rastreamento usando o algoritmo CSRT
rastreador = cv2.TrackerCSRT_create()

# Abre um arquivo de vídeo usando o OpenCV
video = cv2.VideoCapture('rua.mp4')

# Lê o primeiro quadro do vídeo e permite a seleção manual da região de interesse (ROI)
ok, frame = video.read()
bbox = cv2.selectROI(frame)

# Inicializa o rastreador com a ROI selecionada
ok = rastreador.init(frame, bbox)
print(ok)

# Entra em um loop para processar cada quadro do vídeo
while True:
    # Lê um novo quadro do vídeo
    ok, frame = video.read()

    # Se não houver mais quadros, sai do loop
    if not ok:
        break

    # Atualiza o rastreamento com o novo quadro
    ok, bbox = rastreador.update(frame)
    print(bbox)

    # Se o rastreamento for bem-sucedido, desenha um retângulo ao redor do objeto rastreado
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
    else:
        # Se o rastreamento falhar, exibe uma mensagem de falha no quadro
        cv2.putText(frame, f'Falha no rastreamento', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Exibe o quadro processado com as informações de rastreamento
    cv2.imshow('Rastreando', frame)

    # Sai do loop se a tecla 'Esc' (código 27) for pressionada
    if cv2.waitKey(1) & 0XFF == 27:
        break
