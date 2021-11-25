<!-- markdownlint-disable -->

<a href="../main.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `main.py`
A program that opens a pop window after scanning the right QR code. The popup window gives an entry space, where the user has to enter the full path of an image. After hitting the enter button, the user will see a message if the path was successfully read or not. If everything is successful, the user has to choose a button among the three provided ones. Each button applies a 'filter' to the image. The three 'filters' either make the image grayscale, add gaussian blur, or remove the red channel pixels from the image. The newly generated images are saved locally. 


---

<a href="../main.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gen_qr_codes`

```python
gen_qr_codes()
```

Saves several generated QR codes 


---

<a href="../main.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `enter_path`

```python
enter_path(label_result, entry_path)
```

Outputs the image path :param label_result :param entry_path :return: A string that is the input in the entry section :rtype: str 


---

<a href="../main.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `enter_qr_path`

```python
enter_qr_path(label_result, entry_qr_path)
```

Checks if the inputted QR path matches with the original one :param label_result :param entry_qr_path :return: A string that states whether the inputted QR path is right or wrong and gives a corresponding instruction :rtype: str 


---

<a href="../main.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gray`

```python
gray(label_result)
```

Converts the image to grayscale :param label_result: :return: An image with the filter saved locally 


---

<a href="../main.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gaus_blur`

```python
gaus_blur(label_result)
```

Adds Gaussian Blur to the image :param label_result: :return: An image with the filter saved locally 


---

<a href="../main.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `remove_red`

```python
remove_red(label_result)
```

Removes the red channel pixels from the image :param label_result: :return: An image with the filter saved locally 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
