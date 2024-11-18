import jiwer

def ObtenerMetricas(hypothesis,ground_truth):
    transformation = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemovePunctuation(),
        jiwer.RemoveWhiteSpace(replace_by_space=True),
        jiwer.RemoveMultipleSpaces(),
        jiwer.ReduceToListOfListOfWords(word_delimiter=" ")
    ]) 

    wer = round(jiwer.wer(ground_truth, hypothesis,truth_transform=transformation,  hypothesis_transform=transformation),2)
    mer = round(jiwer.mer(ground_truth, hypothesis,truth_transform=transformation,  hypothesis_transform=transformation),2)
    wil = round(jiwer.wil(ground_truth, hypothesis,truth_transform=transformation,  hypothesis_transform=transformation),2)

    print("WER: "+str(wer))
    print("MER: "+str(mer))
    print("WIL: "+str(wil))

##CANAL_5_NOTICIAS_CENTRAL_20210730_215000
##CANAL_5_NOTICIAS_CENTRAL_20210803_215000
TranscripcionesWhisper= [
 'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte1\\Whisper\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte1.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte2\\Whisper\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte2.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte3\\Whisper\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte3.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte1\\Whisper\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte1.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte2\\Whisper\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte2.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte3\\Whisper\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte3.txt']


TranscripcionesGoogleSpeechRecognition = ['Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte1\\SpeechRecognition\\ResultadoGoogleSpeechRecognition.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte2\\SpeechRecognition\\ResultadoGoogleSpeechRecognition.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte3\\SpeechRecognition\\ResultadoGoogleSpeechRecognition.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte1\\SpeechRecognition\\ResultadoGoogleSpeechRecognition.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte2\\SpeechRecognition\\ResultadoGoogleSpeechRecognition.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte3\\SpeechRecognition\\ResultadoGoogleSpeechRecognition.txt']

TranscripcionesCorrectas = ['Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte1\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte1Corregido.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte2\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte2Corregido.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000\\Parte3\\CANAL_5_NOTICIAS_CENTRAL_20210730_215000Parte3Corregido.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte1\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte1Corregido.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte2\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte2Corregido.txt'
,'Transcripciones\\Resultados\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000\\Parte3\\CANAL_5_NOTICIAS_CENTRAL_20210803_215000Parte3Corregido.txt']

for TranscripcionWhisper in TranscripcionesWhisper:
    file = open(TranscripcionesCorrectas[TranscripcionesWhisper.index(TranscripcionWhisper)], 'r',encoding="utf-8")
    ground_truth = file.read()
    file = open(TranscripcionWhisper, 'r',encoding="utf-8")
    hypothesis = file.read()
    
    print("Medidas de Whisper - "+TranscripcionWhisper  )
    ObtenerMetricas(hypothesis,ground_truth)

for TranscripcionGoogleSpeechRecognition in TranscripcionesGoogleSpeechRecognition:
    file = open(TranscripcionesCorrectas[TranscripcionesGoogleSpeechRecognition.index(TranscripcionGoogleSpeechRecognition)], 'r',encoding="utf-8")
    ground_truth = file.read()
    file = open(TranscripcionGoogleSpeechRecognition, 'r')
    hypothesis = file.read()
    print("Medidas de GoogleSpeechRecognition - "+TranscripcionGoogleSpeechRecognition)
    ObtenerMetricas(hypothesis,ground_truth)
    