# PROJETO 6 - MESTRES DA AUTOMAÇÃO - SISTEMA COMPLETO DE CÁLCULO DE IMC + GUI 


import PySimpleGUI as sg

def calcula_imc(peso,altura):
    altura = float(altura) / 100
    peso = float(peso)

    # cálculo do imc
    imc = peso / (altura*altura)
    return imc


def avalia_imc(imc):
    if imc <= 18.5:
        return 'Abaixo de peso'
    elif imc <= 24.9:
        return 'Peso normal'
    elif imc <= 29.9:
        return 'Sobrepeso'
    elif imc <= 34.9:
        return 'Obesidade 1'
    elif imc <= 39.9:
        return 'Obesidade 2'
    else:
        return 'Obesidade 3'


# Tema 
sg.theme('LightGray1')

# Layout
layout = [
    [sg.Text('Altura (em centímetros)',size=17), sg.Input(key = 'altura',size=5),],
    [sg.Text('Peso (em KG)',size=17),sg.Input(key = 'peso',size=5)],
    [sg.Text(key='texto_avaliacao', size=(20))],
    [sg.Text(key='texto_imc', size=(20))],
    [sg.Button(button_text='Calcular')]
]

# Janela
window = sg.Window('IMC', layout = layout)

# Leitura de eventos e valores
while True:
    event,values = window.read()
    # Ler e reagir aos eventos
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calcular':
        resultado = calcula_imc(values['peso'],values['altura'])
        avaliacao = avalia_imc(resultado)  
        window['texto_imc'].update(font='Bold')
        window['texto_imc'].update(f'IMC: {resultado:.2f}')
        window['texto_avaliacao'].update(font='Bold')
        window['texto_avaliacao'].update(avaliacao)
        if resultado <= 18.5:
            window['texto_avaliacao'].update(text_color='orange')
        elif resultado <= 29.9:
            window['texto_avaliacao'].update(text_color='GREEN')
        else: 
            window['texto_avaliacao'].update(text_color='RED')
        

