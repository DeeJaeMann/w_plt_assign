#!/usr/bin/env python3.12
# Rewrite this in Unit Test

from caesar_cipher import caesar_cipher, Message

print(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!")
print(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
print(caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz.")
