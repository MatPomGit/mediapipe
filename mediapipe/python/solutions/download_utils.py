# Copyright 2021 The MediaPipe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Narzędzia do pobierania modeli MediaPipe.

Ten moduł zawiera funkcje pomocnicze do pobierania modeli MediaPipe
z Google Cloud Storage. Modele są automatycznie pobierane tylko wtedy,
gdy nie istnieją lokalnie w pakiecie.
"""

import os
import shutil
import urllib.request

# Prefiks URL dla zasobów MediaPipe w Google Cloud Storage
_GCS_URL_PREFIX = 'https://storage.googleapis.com/mediapipe-assets/'


def download_oss_model(model_path: str):
  """Pobiera model OSS z Google Cloud Storage, jeśli nie istnieje w pakiecie.
  
  Funkcja sprawdza, czy model o podanej ścieżce już istnieje lokalnie.
  Jeśli nie istnieje, pobiera go z Google Cloud Storage i zapisuje
  w odpowiedniej lokalizacji w strukturze pakietu MediaPipe.
  
  Args:
    model_path: Ścieżka do pliku modelu względem głównego katalogu MediaPipe.
                Na przykład: 'modules/face_detection/face_detection_short_range.tflite'
  
  Raises:
    ConnectionError: Jeśli pobieranie modelu z Google Cloud Storage nie powiodło się
                     (np. kod odpowiedzi HTTP różny od 200).
  
  Example:
    download_oss_model('modules/face_detection/face_detection_short_range.tflite')
  """

  # Określ absolutną ścieżkę do katalogu głównego MediaPipe
  mp_root_path = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-4])
  model_abspath = os.path.join(mp_root_path, model_path)
  
  # Jeśli model już istnieje, pomiń pobieranie
  if os.path.exists(model_abspath):
    return
  
  # Skonstruuj URL do modelu w Google Cloud Storage
  model_url = _GCS_URL_PREFIX + model_path.split('/')[-1]
  print('Downloading model to ' + model_abspath)
  
  # Pobierz model i zapisz go lokalnie
  with urllib.request.urlopen(model_url) as response, open(model_abspath,
                                                           'wb') as out_file:
    if response.code != 200:
      raise ConnectionError('Cannot download ' + model_path +
                            ' from Google Cloud Storage.')
    shutil.copyfileobj(response, out_file)
