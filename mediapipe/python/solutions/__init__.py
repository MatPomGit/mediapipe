# Copyright 2020 The MediaPipe Authors.
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

"""API Python MediaPipe Solutions.

Ten moduł zapewnia gotowe rozwiązania do różnych zadań percepcji wizualnej
i przetwarzania mediów. MediaPipe Solutions oferuje wysokopoziomowe API
dla popularnych zadań uczenia maszynowego, takich jak detekcja twarzy,
śledzenie dłoni, estymacja pozy ciała i segmentacja.

Dostępne rozwiązania:
  - face_detection: Wykrywanie twarzy na obrazach i wideo
  - face_mesh: Detekcja siatki 468 punktów orientacyjnych twarzy
  - hands: Śledzenie dłoni i wykrywanie gestów (21 punktów na dłoń)
  - pose: Estymacja pozy ciała (33 punkty orientacyjne)
  - holistic: Kompleksowe śledzenie (twarz, dłonie, poza)
  - selfie_segmentation: Segmentacja tła portretowego
  - objectron: Detekcja i śledzenie obiektów 3D

Narzędzia pomocnicze:
  - drawing_utils: Narzędzia do rysowania punktów orientacyjnych
  - drawing_styles: Style wizualizacji dla różnych rozwiązań
  - *_connections: Definicje połączeń punktów orientacyjnych

Przykład użycia:
  import mediapipe as mp
  
  # Inicjalizacja rozwiązania do detekcji rąk
  mp_hands = mp.solutions.hands
  hands = mp_hands.Hands()
  
  # Przetworzenie obrazu
  results = hands.process(image)
  
  # Rysowanie wyników
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing.draw_landmarks(image, results.multi_hand_landmarks, 
                            mp_hands.HAND_CONNECTIONS)
"""

# Importy modułów rozwiązań MediaPipe
import mediapipe.python.solutions.drawing_styles
import mediapipe.python.solutions.drawing_utils
import mediapipe.python.solutions.face_detection
import mediapipe.python.solutions.face_mesh
import mediapipe.python.solutions.face_mesh_connections
import mediapipe.python.solutions.hands
import mediapipe.python.solutions.hands_connections
import mediapipe.python.solutions.holistic
import mediapipe.python.solutions.objectron
import mediapipe.python.solutions.pose
import mediapipe.python.solutions.selfie_segmentation
