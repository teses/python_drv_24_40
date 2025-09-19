"""
    Was ist Numpy?

    - Bibliothek für effiziente Berechnungen auf große listen und matrizen (mehrdimensionale arrays)
    - mathematische Funktionen ähnl. MATLAB
    - Numpy arbeitet mit C-Code .
    - Es ist schneller als reine python-Listen


"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
#############################################################
print("-"*50)
print(np.zeros(5))
print(np.zeros((3, 4)))
print(np.ones(5))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))

#############################################################
print("-"*50)
print(matrix.shape) # reihen, spalten
print(matrix.size) # elemente
print(matrix.ndim) # 2

###############################################
# slicing
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[-1])
print(arr[1:4])

print("-"*50)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0][1]) # alte art und weise
print(matrix[0,1]) # numpy art und weise

print(matrix[0,1])
print(matrix[:,1]) # erste spalte
print(matrix[:2,1]) # zeile 1 und 2 - die zweite spalte

############################
# numpy arbeitet elementweise
arr1 = np.array([1, 2, 3])
arr2 = np.array([6, 7, 8])

print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 * 10)
print(arr1 - arr2)
print(arr1 / arr2)
print(arr1 / 2)
#################################
print("-"*50)
artikelNamen = ["TFT 15 Zoll", "32 GB RAM", "Maus"]
artikelPreiseNetto  = [100, 200, 50]
artikelPreiseNettoNumpy = np.array(artikelPreiseNetto)
artikelPreiseBrutto = artikelPreiseNettoNumpy * 1.19
print(artikelPreiseNettoNumpy)
print(artikelPreiseBrutto)

##############################################################
print("-"*50)
artikel = [
    ["TFT 15 Zoll", 100],
    ["32 GB RAM", 200],
    ["Maus", 50],
]
artikel = np.array(artikel)

artikelTransponiert = artikel.T
artikelPreiseBrutto  = np.array(list(map(int,artikelTransponiert[1]))) * 1.19
artikelTransponiert[1] = artikelPreiseBrutto

print(artikelPreiseBrutto)
print(artikel)
print(np.array(list(map(int,artikelTransponiert[1]))))
