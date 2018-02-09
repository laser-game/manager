# coding=utf-8


import json

from core.utils.settings import Settings

GAME_TYPES = json.loads("""
[
  {
    "DeathTime": 5, 
    "Fn": 0, 
    "GameTime": 15, 
    "ID": 0, 
    "Immorality": true, 
    "Name": "Solo", 
    "OffLED": false, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 1, 
    "GameTime": 15, 
    "ID": 1, 
    "Immorality": false, 
    "Name": "S.W.A.T - Light", 
    "OffLED": true, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 2, 
    "GameTime": 15, 
    "ID": 2, 
    "Immorality": false, 
    "Name": "S.W.A.T - UV", 
    "OffLED": true, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 0, 
    "GameTime": 15, 
    "ID": 3, 
    "Immorality": false, 
    "Name": "Invisible", 
    "OffLED": true, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 0, 
    "GameTime": 15, 
    "ID": 4, 
    "Immorality": true, 
    "Name": "Team Game", 
    "OffLED": false, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 1, 
    "GameTime": 15, 
    "ID": 5, 
    "Immorality": false, 
    "Name": "S.W.A.T - Light Team", 
    "OffLED": true, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 2, 
    "GameTime": 15, 
    "ID": 6, 
    "Immorality": false, 
    "Name": "S.W.A.T - UV Team", 
    "OffLED": true, 
    "ShotsInBatch": 1, 
    "Sound": true
  }, 
  {
    "DeathTime": 5, 
    "Fn": 0, 
    "GameTime": 15, 
    "ID": 7, 
    "Immorality": false, 
    "Name": "Invisible Team", 
    "OffLED": true, 
    "ShotsInBatch": 1, 
    "Sound": true
  }
]
""")

api_settings = Settings(__name__, 'API')
