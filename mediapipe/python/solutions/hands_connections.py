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
"""Połączenia punktów orientacyjnych dłoni MediaPipe.

Ten moduł definiuje stałe określające połączenia między punktami orientacyjnymi
dłoni używanymi przez rozwiązanie MediaPipe Hands. Każde połączenie jest
reprezentowane jako krotka dwóch indeksów punktów orientacyjnych.

Połączenia są podzielone na logiczne grupy anatomiczne:
- HAND_PALM_CONNECTIONS: Połączenia tworzące dłoń/nadgarstek
- HAND_THUMB_CONNECTIONS: Połączenia kciuka
- HAND_INDEX_FINGER_CONNECTIONS: Połączenia palca wskazującego
- HAND_MIDDLE_FINGER_CONNECTIONS: Połączenia palca środkowego
- HAND_RING_FINGER_CONNECTIONS: Połączenia palca serdecznego
- HAND_PINKY_FINGER_CONNECTIONS: Połączenia palca małego
- HAND_CONNECTIONS: Kompletny zestaw wszystkich połączeń dłoni

Przykład użycia:
    from mediapipe.python.solutions import hands_connections
    import mediapipe as mp
    
    # Dostęp do wszystkich połączeń dłoni
    all_connections = hands_connections.HAND_CONNECTIONS
    
    # Dostęp do połączeń konkretnego palca
    thumb = hands_connections.HAND_THUMB_CONNECTIONS
    
    # Użycie z MediaPipe Hands do rysowania
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    
    # Przetwarzanie obrazu (zakładając, że 'image' to numpy array RGB)
    results = hands.process(image)
    
    # Rysowanie połączeń dłoni na obrazie
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, hands_connections.HAND_CONNECTIONS)
"""

# Połączenia tworzące strukturę dłoni oraz nadgarstka
HAND_PALM_CONNECTIONS = ((0, 1), (0, 5), (9, 13), (13, 17), (5, 9), (0, 17))

# Połączenia stawów kciuka
HAND_THUMB_CONNECTIONS = ((1, 2), (2, 3), (3, 4))

# Połączenia stawów palca wskazującego
HAND_INDEX_FINGER_CONNECTIONS = ((5, 6), (6, 7), (7, 8))

# Połączenia stawów palca środkowego
HAND_MIDDLE_FINGER_CONNECTIONS = ((9, 10), (10, 11), (11, 12))

# Połączenia stawów palca serdecznego
HAND_RING_FINGER_CONNECTIONS = ((13, 14), (14, 15), (15, 16))

# Połączenia stawów palca małego
HAND_PINKY_FINGER_CONNECTIONS = ((17, 18), (18, 19), (19, 20))

# Kompletny zestaw wszystkich połączeń punktów orientacyjnych dłoni
HAND_CONNECTIONS = frozenset().union(*[
    HAND_PALM_CONNECTIONS, HAND_THUMB_CONNECTIONS,
    HAND_INDEX_FINGER_CONNECTIONS, HAND_MIDDLE_FINGER_CONNECTIONS,
    HAND_RING_FINGER_CONNECTIONS, HAND_PINKY_FINGER_CONNECTIONS
])
