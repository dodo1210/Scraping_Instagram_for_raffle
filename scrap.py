# -*- coding: utf-8 -*-

'Seguir-> https://www.instagram.com/super__premios/following/'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time



paises = ['Estado da Palestina','Estados Unidos','Estónia','Etiópia','Fiji','Filipinas','Finlândia','França','Gabão','Gâmbia','Gana','Geórgia','Granada','Grécia','Guatemala','Guiana','Guiné','Guiné Equatorial','Guiné-Bissau','Haiti','Honduras','Hungria','Iémen','Ilhas Marechal','Índia','Indonésia','Irão','Iraque','Irlanda','Islândia','Israel','Itália','Jamaica','Japão','Jibuti','Jordânia','Laus','Lesoto','Letónia','Líbano','Libéria','Líbia','Listenstaine','Lituânia','Luxemburgo','Macedónia','Madagáscar','Malásia','Maláui','Maldivas','Mali','Malta','Marrocos','Maurícia','Mauritânia','México','Mianmar','Micronésia','Moçambique','Moldávia','Mónaco','Mongólia','Montenegro','Namíbia','Nauru','Nepal','Nicarágua','Níger','Nigéria','Noruega','Nova Zelândia','Omã','Países Baixos','Palau','Panamá','Papua Nova Guiné','Paquistão','Paraguai','Peru','Polónia','Portugal','Quénia','Quirguistão','Quiribáti','Reino Unido','República Centro-Africana','República Checa','República Democrática do Congo','República Dominicana','Roménia','Ruanda','Rússia','Salomão','Salvador','Samoa','Santa Lúcia','São Cristóvão e Neves','São Marinho','São Tomé e Príncipe','São Vicente e Granadinas','Seicheles','Senegal','Serra Leoa','Sérvia','Singapura','Síria','Somália','Sri Lanca','Suazilândia','Sudão','Sudão do Sul','Suécia','Suíça','Suriname','Tailândia','Taiuã','Tajiquistão','Tanzânia','Timor-Leste','Togo','Tonga','Trindade e Tobago','Tunísia','Turcomenistão','Turquia','Tuvalu','Ucrânia','Uganda','Uruguai','Usbequistão','Vanuatu','Vaticano','Venezuela','Vietname','Zâmbia','Zimbábue','Afeganistão','África do Sul','Albânia','Alemanha','Andorra','Angola','Antiga e Barbuda','Arábia Saudita','Argélia','Argentina','Arménia','Austrália','Áustria','Azerbaijão','Bahamas','Bangladesh','Barbados','Barém','Bélgica','Belize','Benim','Bielorrússia','Bolívia','Bósnia e Herzegovina','Botsuana','Brasil','Brunei','Bulgária','Burquina Faso','Burúndi','Butão','Cabo Verde','Camarões','Camboja','Canadá','Catar','Cazaquistão','Chade','Chile','China','Chipre','Colômbia','Comores','Congo-Brazzaville','Coreia do Norte','Coreia do Sul','Cosovo','Costa do Marfim','Costa Rica','Croácia','Cuaite','Cuba','Dinamarca','Dominica','Egito','Emirados Árabes Unidos','Equador','Eritreia','Eslováquia','Eslovénia','Espanha']
for p in paises:
    driver = webdriver.Chrome(executable_path='/home/doara/Documentos/uns_codigos/Python/bovespa_project/chromedriver_linux64/chromedriver')
    a = driver.get("https://www.instagram.com/p/B-DNz3kJVZH/")
    time.sleep(5)
    content = driver.find_element_by_css_selector('button.sqdOP').click()

    time.sleep(1)
    name = driver.find_element_by_css_selector('input._2hvTZ')
    name.send_keys('dougsiqueira2020')

    password = driver.find_element_by_name('password')
    password.send_keys('')

    list_b = driver.find_elements_by_css_selector('button.sqdOP')
    list_b[4].click()
    time.sleep(5)

    driver.find_element_by_css_selector('textarea.Ypffh').click()
    driver.find_element_by_css_selector('textarea.Ypffh').send_keys(p)
    list_b = driver.find_elements_by_xpath("//button[@type='submit']")
    list_b[0].click()
    time.sleep(20)
    driver.close()



