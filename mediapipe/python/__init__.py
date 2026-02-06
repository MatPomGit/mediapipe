# Copyright 2020-2021 The MediaPipe Authors.
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

"""API Python MediaPipe.

Ten moduł zapewnia główne API Python dla MediaPipe, które umożliwia budowanie
i uruchamianie potoków przetwarzania mediów. MediaPipe to framework do budowania
wydajnych potoków przetwarzania percepcyjnego, szczególnie przydatny do
uczenia maszynowego na urządzeniach.

Główne komponenty:
  - CalculatorGraph: Główna klasa do budowania i uruchamiania grafów kalkulatorów
  - Image/ImageFrame: Klasy do reprezentacji i przetwarzania obrazów
  - Packet: Kontener danych przesyłanych między kalkulatorami
  - Timestamp: Reprezentacja znaczników czasowych dla pakietów
  - packet_creator/packet_getter: Narzędzia do tworzenia i odczytywania pakietów

Przykład użycia:
  import mediapipe as mp
  import numpy as np
  
  # Utworzenie grafu kalkulatorów
  graph = mp.CalculatorGraph()
  
  # Tworzenie pakietów
  packet = mp.packet_creator.create_string('hello')
  
  # Przetwarzanie obrazów (zakładając, że image_data to numpy array RGB)
  image_data = np.zeros((480, 640, 3), dtype=np.uint8)
  image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_data)
"""

# Importy podstawowych klas i narzędzi framework'a
from mediapipe.python._framework_bindings import model_ckpt_util
from mediapipe.python._framework_bindings import resource_util
from mediapipe.python._framework_bindings.calculator_graph import CalculatorGraph
from mediapipe.python._framework_bindings.calculator_graph import GraphInputStreamAddMode
from mediapipe.python._framework_bindings.image import Image
from mediapipe.python._framework_bindings.image_frame import ImageFormat
from mediapipe.python._framework_bindings.image_frame import ImageFrame
from mediapipe.python._framework_bindings.matrix import Matrix
from mediapipe.python._framework_bindings.packet import Packet
from mediapipe.python._framework_bindings.timestamp import Timestamp
from mediapipe.python._framework_bindings.validated_graph_config import ValidatedGraphConfig
import mediapipe.python.packet_creator
import mediapipe.python.packet_getter
