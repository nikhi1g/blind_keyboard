from kivy.properties import ObjectProperty
from kivy.core.window import Window, Animation
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from pidev.kivy import ImageButton
# from datetime import datetime #not working, set date for may 30th, 2022 reminder if emails don't work
from pidev.kivy.selfupdatinglabel import SelfUpdatingLabel
from pidev.MixPanel import MixPanel
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import os
# os.environ['DISPLAY'] = ":0.0"
# os.environ['KIVY_WINDOW'] = 'egl_rpi'
from threading import Thread
from kivy.clock import Clock
from kivy.properties import NumericProperty
import time
import kivy.uix.button
from kivy.app import App
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy import DPEAButton