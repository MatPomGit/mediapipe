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
"""Połączenia punktów orientacyjnych pozy MediaPipe.

Ten moduł definiuje stałe określające połączenia między punktami orientacyjnymi
pozy ciała używanymi przez rozwiązanie MediaPipe Pose. Każde połączenie jest
reprezentowane jako krotka dwóch indeksów punktów orientacyjnych.

Połączenia obejmują:
- Punkty twarzy (nos, oczy, uszy)
- Tułów (ramiona i biodra)
- Kończyny górne (ramiona, łokcie, nadgarstki, dłonie)
- Kończyny dolne (biodra, kolana, kostki, stopy)

Stała POSE_CONNECTIONS zawiera kompletny zestaw wszystkich połączeń
określających szkielet pozy człowieka w 3D.

Przykład użycia:
    from mediapipe.python.solutions import pose_connections
    import mediapipe as mp
    
    # Dostęp do wszystkich połączeń pozy
    connections = pose_connections.POSE_CONNECTIONS
    
    # Użycie z MediaPipe Pose do rysowania
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    
    # Przetwarzanie obrazu (zakładając, że 'image' to numpy array RGB)
    results = pose.process(image)
    
    # Rysowanie szkieletu pozy na obrazie
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, pose_connections.POSE_CONNECTIONS)
"""

# Kompletny zestaw połączeń punktów orientacyjnych pozy ciała
# Obejmuje twarz, tułów, kończyny górne i dolne
POSE_CONNECTIONS = frozenset([(0, 1), (1, 2), (2, 3), (3, 7), (0, 4), (4, 5),
                              (5, 6), (6, 8), (9, 10), (11, 12), (11, 13),
                              (13, 15), (15, 17), (15, 19), (15, 21), (17, 19),
                              (12, 14), (14, 16), (16, 18), (16, 20), (16, 22),
                              (18, 20), (11, 23), (12, 24), (23, 24), (23, 25),
                              (24, 26), (25, 27), (26, 28), (27, 29), (28, 30),
                              (29, 31), (30, 32), (27, 31), (28, 32)])
