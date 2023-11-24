from tkinter import *
from tkinter import messagebox

from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service as chrserv
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pyautogui as pg

#-----------------------------------------------------------------#

options = Options()
options.add_argument("headless") #exec em segundo plano

driver = wd.Chrome(service=chrserv(ChromeDriverManager().install()), options=options)

win_width, win_heigth = 750, 650

root = Tk()
root.iconbitmap('RPA\Tkinter\icone.ico')
root.title('Pesquise o CEP')
root.geometry('{}x{}'.format(win_width, win_heigth))
menubar = Menu(root)


def pesquisaCEP(*args):
    
    driver = wd.Chrome(options=options)
    pg.sleep(1)
    driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
    pg.sleep(2)
    cep_find = txtbox_cep.get() 
    driver.find_element(By.XPATH, '//*[@id="endereco"]').send_keys(cep_find)
    driver.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()
    pg.sleep(1)
    
    rua = driver.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
    lb_rua.config(text='Rua: ' + rua, wraplength=win_width)
    bairro = driver.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    lb_bairro.config(text='Bairro: ' + bairro, wraplength=win_width)
    cidade = driver.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    lb_cidade.config(text='Cidade: ' + cidade, wraplength=win_width)
    end_cep = driver.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
    lb_cep.config(text='CEP: ' + end_cep)

def clear_search():
    lb_rua.config(text='Rua: ')
    lb_bairro.config(text='Bairro: ')
    lb_cidade.config(text='Cidade: ')
    lb_cep.config(text='CEP: ')

root.bind('<Return>', pesquisaCEP)

linha_cep = Label(text='CEP: ', font='Arial 30')
linha_cep.grid(row=1, column=0, stick='W')
txtbox_cep = Entry(font = 'Arial 30')
txtbox_cep.grid(row=1, column=1, stick='W')
txtbox_cep.focus()


bt_pesquisar = Button(root, text='Pesquisar', font= 'Arial 30',
                      command = pesquisaCEP)
bt_pesquisar.grid(row=2, column=0, columnspan=2, stick='NSEW')

pady_txt = 2.5

lb_rua = Label(text = '\nRua: ', font = 'Arial 30')
lb_rua.grid(row=3, column=0, columnspan=2, stick='W', pady=pady_txt)
lb_bairro = Label(text = 'Bairro: ', font = 'Arial 30')
lb_bairro.grid(row=4, column=0, columnspan=2, stick='W', pady=pady_txt)
lb_cidade = Label(text = 'Cidade: ', font = 'Arial 30')
lb_cidade.grid(row=5, column=0, columnspan=2, stick='W', pady=pady_txt)
lb_cep = Label(text = 'CEP: ', font = 'Arial 30')
lb_cep.grid(row=6, column=0, columnspan=2, stick='W', pady=pady_txt)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label ='Arquivo', menu = file) 
file.add_command(label ='Limpar', command = clear_search) 
file.add_command(label ='Sair', command = root.destroy) 

root.config(menu = menubar)

root.mainloop()

