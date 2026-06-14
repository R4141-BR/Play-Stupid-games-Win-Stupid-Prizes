print("\x1b[2J\033[H")

import random
import pycountry

def goback():
      choice = input("Do you wanna go back to the menu?(Y/N) ").lower()

      if choice == "y":
            menu()
      else:
            print("GOODBYE, THANK YOU FOR PLAYING - R4141-BR")





def Corredor():  
      
      nome = input("What is your name? ")
      velocidade = int(input("What is your current velocity in m/s? "))
      distância = int(input("How far are you from your destination in meters? "))

      tempo = distância / velocidade
      print(f"------Hello {nome}------,")
      print(f"If you run {distância} meters with a velocity of {velocidade}m/s, you'll take {tempo} seconds to get to your destination.")
      goback()
  

def mapamundo():
      print("----WHERE SHOULD YOU GO !!!----")
      wheretogo = []
      for pais in pycountry.countries:
            wheretogo.append(pais.name)

      number = int(input("What is your favorite number? "))
      Luck = number % len(wheretogo)
      randomC = wheretogo[Luck]

      print(f" Congrats, next holiday you should go to {randomC}")
      goback()

def drawcube():
      print("\n---- CUBE MAKER ----")

      X = int(input("What is the lenght of the cube? "))
      Y = int(input("What is the height of the cube? "))

      for i in range(Y):
            print("[ ]"* X)
      goback()


# MAIN MENU

def menu():
      titulo="""
++------------------------------------------------------------++
++------------------------------------------------------------++
|| _________  ___  ___  _______                               ||
|||\___   ___\\  \|\  \|\  ___ \                              ||
||\|___ \  \_\ \  \\\  \ \   __/|                             ||
||     \ \  \ \ \   __  \ \  \_|/__                           ||
||      \ \  \ \ \  \ \  \ \  \_|\ \                          ||
||       \ \__\ \ \__\ \__\ \_______\                         ||
||        \|__|  \|__|\|__|\|_______|                         ||
||                                                            ||
||                                                            ||
||                                                            ||
|| ________  _________  ___  ___  ________  ___  ________     ||
|||\   ____\|\___   ___\\  \|\  \|\   __  \|\  \|\   ___ \    ||
||\ \  \___|\|___ \  \_\ \  \\\  \ \  \|\  \ \  \ \  \_|\ \   ||
|| \ \_____  \   \ \  \ \ \  \\\  \ \   ____\ \  \ \  \ \\ \  ||
||  \|____|\  \   \ \  \ \ \  \\\  \ \  \___|\ \  \ \  \_\\ \ ||
||    ____\_\  \   \ \__\ \ \_______\ \__\    \ \__\ \_______\||
||   |\_________\   \|__|  \|_______|\|__|     \|__|\|_______|||
||   \|_________|                                             ||
||                                                            ||
||                                                            ||
|| ________  ________  _____ ______   _______                 ||
|||\   ____\|\   __  \|\   _ \  _   \|\  ___ \                ||
||\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|               ||
|| \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__             ||
||  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \            ||
||   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\           ||
||    \|_______|\|__|\|__|\|__|     \|__|\|_______|           ||
||                                                            ||
||                                                            ||
||                                                            ||
|| ___  ___  ___  ___  ________                               ||
|||\  \|\  \|\  \|\  \|\   __  \                              ||
||\ \  \\\  \ \  \\\  \ \  \|\ /_                             ||
|| \ \   __  \ \  \\\  \ \   __  \                            ||
||  \ \  \ \  \ \  \\\  \ \  \|\  \                           ||
||   \ \__\ \__\ \_______\ \_______\                          ||
||    \|__|\|__|\|_______|\|_______|                          ||
||                                                            ||
++------------------------------------------------------------++
++------------------------------------------------------------++
                                                                                                                                                                                                               
      """



      print(")=======================()")
      print(titulo)
      print(")=======================()")
      print("1- RUNNER-MAN")
      print("2- HOLIDAY GENERATOR")
      print("3- CUBE GENERATOR")
      print("4- GET OUF THE PROGRAMM")

      opção = input("Choose an option (1-4): ")

      if opção == "1":
            Corredor()
      elif opção == "2":
            mapamundo()
      elif opção == "3":
            drawcube()
      elif opção == "4":
            print("GOODBYE, THANK YOU FOR PLAYING - R4141-BR")
      else:
            print("INVALID OPTION, TRY AGAIN A NUMBER (1-4)")
      

menu()


#Feito por R4141-BR // Made by R4141-BR