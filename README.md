# find-the-ship

Toy dataset for computer vision education and experimentation

<table align="center">
  <tr>
    <td><img src="./set-A_train/20171105_185533_Location-2D_Heading-West_Ship-Freighter.jpg" width="200"></td>
    <td><img src="./set-A_train/20171105_190017_Location-4C_Heading-East_Ship-Cruiser-3.jpg" width="200"></td>
    <td><img src="./set-A_train/20171105_190746_Location-1C_Heading-West_Ship-Cruiser-2.jpg" width="200"></td>
  </tr>
  <tr>
    <td><img src="./set-A_train/20171105_190339_Location-3C_Heading-East_Ship-Fishing-2.jpg" width="200"></td>
    <td><img src="./set-A_train/20171105_190437_Empty.jpg" width="200"></td>
    <td><img src="./set-A_train/20171105_214355_Location-6A_Heading-East_Ship-Fishing-1.jpg" width="200"></td>
  </tr>
  <tr>
    <td><img src="./set-A_train/20171105_214605_Location-3A_Heading-East_Ship-Cruiser-1.jpg" width="200"></td>
    <td><img src="./set-A_train/20171106_184157_Location-4A_Heading-West_Ship-Cruiser-2.jpg" width="200"></td>
    <td><img src="./set-A_train/20171106_192310_Location-7C_Heading-West_Ship-Freighter.jpg" width="200"></td>
  </tr>
</table>

This is a multi-task classification dataset I made for fun in late 2017 using a cheap webcam, balsa wood and paint. It consists of 2035 images of a board representing a ficticious ocean area where 6 models of ships operate. Every image is 640 x 480 pixels with three color channels (RGB). Each non-empty image sample contains one scaled model of a ship with a particular location and heading. The tasks are:
* **1.** Determining whether or not the image contains a ship.
* **2.** If the image contains a ship:
  * **A.** Determine the ship's location.
  * **B.** Determine the ship's heading.
  * **C.** Determine the ship's model.

The data split is as follows:
* `set-A_train/` contains 1635 image samples for training
* `set-B_test/` contains 400 image samples for testing (validation)

Needless to say, you may choose any other data split you find useful for your purposes. 

## Board

The board consists of 28 locations, with rows ranging from 1 through 7 and columns ranging from A through D. Each non-empty image sample contains exactly one ship, and the ship may be facing either West (towards the left of the board) or East (towards the right of the board). The following image sample shows an empty board with each location labeled. 

<div align="center">
  <img src="./README_Board.png" alt="The Board" title="The Board">
</div>

## Ship Models

Each non-empty image sample contains exactly one of six possible ship models, facing either West (towards the left of the board) or East (towards the right of the board). The following table displays sample images of each ship model. 

<table align="center">
  <tr>
    <th>Sample Image</th>
    <th>Ship Model</th>
    <th>Shown Facing</th>
  </tr>
  <tr>
    <td><img src="./README_Cruiser-1.jpg" alt="Cruiser-1" title="Cruiser-1" width="160"></td>
    <td><b>Cruiser-1</b></td>
    <td>West</td>
  </tr>
  <tr>
    <td><img src="./README_Cruiser-2.jpg" alt="Cruiser-2" title="Cruiser-2" width="160"></td>
    <td><b>Cruiser-2</b></td>
    <td>East</td>
  </tr>
  <tr>
    <td><img src="./README_Cruiser-3.jpg" alt="Cruiser-3" title="Cruiser-3" width="160"></td>
    <td><b>Cruiser-3</b></td>
    <td>East</td>
  </tr>
  <tr>
    <td><img src="./README_Fishing-1.jpg" alt="Fishing-1" title="Fishing-1" width="160"></td>
    <td><b>Fishing-1</b></td>
    <td>West</td>
  </tr>
  <tr>
    <td><img src="./README_Fishing-2.jpg" alt="Fishing-2" title="Fishing-2" width="160"></td>
    <td><b>Fishing-2</b></td>
    <td>East</td>
  </tr>
  <tr>
    <td><img src="./README_Freighter.jpg" alt="Freighter" title="Freighter" width="160"></td>
    <td><b>Freighter</b></td>
    <td>West</td>
  </tr>
</table>

## Image Labels

Each non-empty image sample contains its labels embedded in its respective filename according to the following format.

<div align="center">
  <code>YYYYMMDD_HHMMSS_Location-[LOC]_Heading-[HEAD]_Ship-[SHIP].jpg</code>
</div>

<p>&nbsp;</p>

On the other hand, empty image sample filenames contain only creation date and time.

<div align="center">
  <code>YYYYMMDD_HHMMSS_Empty.jpg</code>
</div>

<p>&nbsp;</p>

The following table describes the values taken by the placeholders.

<table align="center">
  <tr>
    <th>Placeholder</th>
    <th>Values</th>
  </tr>
  <tr>
    <td><b><code>YYYYMMDD</code></b></td>
    <td>Image sample creation date in YYYY-MM-DD format.</td>
  </tr>
  <tr>
    <td><b><code>HHMMSS</code></b></td>
    <td>Image sample creation time in HH:MM:SS format.</td>
  </tr>
  <tr>
    <td><b><code>[LOC]</code></b></td>
    <td>Ship location row (1,2,3,4,5,6,7) and column (A,B,C,D).</td>
  </tr>
  <tr>
    <td><b><code>[HEAD]</code></b></td>
    <td>Ship heading: West (left) or East (right).</td>
  </tr>
  <tr>
    <td><b><code>[SHIP]</code></b></td>
    <td>Ship model: Cruiser-1, Cruiser-2, Cruiser-3, Fishing-1, Fishing-2 or Freighter.</td>
  </tr>
</table>

<p>&nbsp;</p>

If you don't want to write a parser to read the labels from the image filenames you can use the `image_labels.csv` file inside each dataset directory. It contains a table where each row corresponds to an image sample. The columns are as follows. 

<table align="center">
  <tr>
    <th>Column</th>
    <th>Values</th>
  </tr>
  <tr>
    <td><b>Filename</b></td>
    <td>Filename as is.</td>
  </tr>
  <tr>
    <td><b>Is_nonempty</b></td>
    <td>1 if the image sample is non-empty; 0 otherwise.</td>
  </tr>
  <tr>
    <td><b>Location</b></td>
    <td>If the image is non-empty, ship location row (1,2,3,4,5,6,7) and column (A,B,C,D); blank otherwise.</td>
  </tr>
  <tr>
    <td><b>Heading</b></td>
    <td>If the image is non-empty, ship heading (West or East); blank otherwise.</td>
  </tr>
  <tr>
    <td><b>Ship</b></td>
    <td>If the image is non-empty, ship model: Cruiser-1, Cruiser-2, Cruiser-3, Fishing-1, Fishing-2 or Freighter; blank otherwise.</td>
  </tr>
</table>

The following is an example of the data contained in the `image_labels.csv` files.

<table align="center">
    <tr>
        <th>Filename</th>
        <th>Is_nonempty</th>
        <th>Location</th>
        <th>Heading</th>
        <th>Ship</th>
    </tr>
    <tr>
        <td>20171105_185402_Empty.jpg</td>
        <td>0</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>20171105_185419_Location-1B_Heading-East_Ship-Fishing-1.jpg</td>
        <td>1</td>
        <td>1B</td>
        <td>East</td>
        <td>Fishing-1</td>
    </tr>
    <tr>
        <td>20171105_185451_Location-4C_Heading-East_Ship-Cruiser-1.jpg</td>
        <td>1</td>
        <td>4C</td>
        <td>East</td>
        <td>Cruiser-1</td>
    </tr>
    <tr>
        <td>20171105_185533_Location-2D_Heading-West_Ship-Freighter.jpg</td>
        <td>1</td>
        <td>2D</td>
        <td>West</td>
        <td>Freighter</td>
    </tr>
    <tr>
        <td>20171210_171214_Location-1B_Heading-West_Ship-Cruiser-3.jpg</td>
        <td>1</td>
        <td>1B</td>
        <td>West</td>
        <td>Cruiser-3</td>
    </tr>
    <tr>
        <td>20171210_171245_Empty.jpg</td>
        <td>0</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>20171210_171343_Location-6A_Heading-East_Ship-Cruiser-2.jpg</td>
        <td>1</td>
        <td>6A</td>
        <td>East</td>
        <td>Cruiser-2</td>
    </tr>
</table>

## Examples

You can find example Python scripts in the `/examples` directory. These scripts were written in late 2017 to early 2018, so they are probably deprecrated by now (2025). Back then I used a multi-head Convolutional Neural Network (CNN) written using Keras, which you can find in the `detectorcnn.py` script. 
