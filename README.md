# Now Version:1.0.1
# Image2Text

This is a program for MCU which will read image file and convert it to array.  
Any picture can be convert.

## Library
Pyqt5 and Pillow Required.  
## How it works
1) Select a image file.
2) The program will convert it to a bmp file.
3) Program will read pixel infomation,if you choose X,the order is (TOP TO BOTTOM) then (LEFT TO RIGHT).  
if you choose Y,the order is (LEFT TO RIGHT) then (TOP TO BOTTOM).  
4) If the pixel is NOT white(R>240,G>240,B>240),  
it will be treated as a binary 1,otherwise will be treated as a binary 0.  
5) Then the binary data will be saved in a list.
6) The list will output in a NOT nice format.
## Example
Sorry there is no example...  
