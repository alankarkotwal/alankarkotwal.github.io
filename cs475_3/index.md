# CS475 Assignment 3
-----
#### Alankar Kotwal (12D070010), Manish Goregaokar (120260006)  

##### Running the program
To compile the code unzip the submission, go to the un-zipped folder and type 
```sh
$ make
```
This should generate an executable called `mail` in the folder. To run the executable type
```sh
$ ./main
```

##### Controls

The following positional controls modify the position/orientation of the "selected" segment:

  - `Up`/`Down`: Rotate along `X`
  - `Left`/`Right`: Rotate along `Y`
  - `<`/`>` (actually, `,`/`.`, do not hold shift key): Rotate along `Z`
  - `I`/`K`: Translate along `X`
  - `J`/`L`: Translate along `Y`
  - `U`/`O`: Translate along `Z`

You can switch between the current model using the `M` key. By default, IG-88 is selected.

Using the number keys you can  select a segment to pose.

The segments are labeled below, along with their degrees of freedom. Note that these degrees of freedom correspond to the keys from the positional controls which may be used; not the actual direction in which the segment may rotate.

![](labeling.png)

IG-88:

 1. Whole model (Freely movable)
 2. Left shoulder (Rotation around X)
 3. Right shoulder (Rotation around X)
 4. Left hip (Rotation around Y)
 5. Right hip (Rotation around Y)
 6. Left elbow (Free rotation)
 7. Right elbow (Free rotation)
 8. Left knee (Free rotation)
 9. Right knee (Free rotation)
 10. Head (Rotation around X, Y) [Selected with key `0`]
 11. Left ankle (Rotation around X) [Selected with `Shift`+`1`]
 12. Right ankle (Rotation around X) [Selected with `Shift`+`2`]
 13. 
 
R2-D2:

 1. Whole model (Freely movable)
 2. Head (Rotation around Y)
 3. Probe arm (Translation around Z)
 4. Probe tip (Rotation around Z)
 5. Left "leg" (Rotation around X)
 6. Right "leg" (Rotation around X)
 7. Left foot (Rotation around X)
 8. Right foot (Rotation around X)
 
The camera can be manipulated using the positional controls with the `Shift` key, i.e. `Shift`+`Left` will rotate the camera around Y and `Shift`+`I` will move it along X.

The lights can be similarly manipulated. We have three lights:

 - Light 1 (directionless) can be manipulated with the translation controls with `Ctrl` pressed. It can be toggled with `Ctrl`+`V`
 - Light 2 (directionless) can be manipulated with the translation controls with `Alt` pressed. It can be toggled with `Alt`+`V`
 - The spotlight can be manipulated with all positional controls with `Ctrl` and `Alt` both pressed. I.e. `Ctrl`+`Alt`+`I` will move the spotlight forward along X. It can be toggled with `Ctrl`+`Alt`+`V`
 
Finally, the WASD/QE keys let you "look around" at the current camera. This will not change the "forward" direction of the camera used when moving unlike `Shift`+(arrow keys); it just changes the viewpoint (as if you have turned your neck).


