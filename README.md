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

This is a multi-task classification dataset. It consists of 2035 images of a board representing a ficticious ocean area where 6 models of ships operate. Each non-empty image sample contains one scaled model of a ship with a particular location and heading. The tasks are:
* **1.** Determining whether or not the image contains a ship.
* **2.** If the image contains a ship:
  * **A.** Determine the ship's location.
  * **B.** Determine the ship's heading.
  * **C.** Determine the ship's model.

## The Board

The board consists of 28 locations, with rows ranging from 1 through 7 and columns ranging from A through D. Each non-empty image sample contains exactly one ship, and the ship may be facing either West (towards the left of the board) or East (towards the right of the board). The following image sample shows an empty board with each location labeled. 

<div align="center">
  <img src="./README_Board.png" alt="The Board" title="The Board">
</div>

## The Ships

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

## The Image Labels

Each non-empty image sample contains its labels embedded in its respective filename according to the following format.

<div align="center">
  <code>YYYYMMDD_HHMMSS_Location-[LOC]_Heading-[HEADING]_Ship-[SHIP].jpg</code>
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
    <td><b><code>[HEADING]</code></b></td>
    <td>Ship heading: West (left) or East (right).</td>
  </tr>
  <tr>
    <td><b><code>[SHIP]</code></b></td>
    <td>Ship model: Cruiser-1, Cruiser-2, Cruiser-3, Fishing-1, Fishing-2 or Freighter.</td>
  </tr>
</table>

<p>&nbsp;</p>

The data split is as follows:
* `set-A_train/` contains 1635 image samples for training
* `set-B_test/` contains 400 image samples for testing (validation)

Needless to say, you may choose any other data split you find useful for your purposes. 
