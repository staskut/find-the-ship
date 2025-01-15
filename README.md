# find-the-ship

Toy dataset for computer vision education and experimentation

<table align="center">
  <tr>
    <td><img src="./set-A_train/20171105_185533_Location-2D_Heading-West_Ship-Freighter.jpg" width="320"></td>
    <td><img src="./set-A_train/20171105_190017_Location-4C_Heading-East_Ship-Cruiser-3.jpg" width="320"></td>
  </tr>
  <tr>
    <td><img src="./set-A_train/20171105_190746_Location-1C_Heading-West_Ship-Cruiser-2.jpg" width="320"></td>
    <td><img src="./set-A_train/20171105_190339_Location-3C_Heading-East_Ship-Fishing-2.jpg" width="320"></td>
  </tr>
</table>

## The Board

The board consists of 28 locations, with rows ranging from 1 through 7 and columns ranging from A through D. Each non-empty image sample contains exactly one ship, and the ship may be facing either West (towards the left of the board) or East (towards the right of the board). The following image sample shows an empty board with each location labeled. 

<div align="center">
  <img src="./README_Board.png" alt="The Board" title="The Board">
</div>

## The Ships

Each non-empty image sample contains exactly one of six possible ships, facing either West (towards the left of the board) or East (towards the right of the board). The following table displays sample images of each ship. 

<table align="center">
  <tr>
    <th>Sample Image</th>
    <th>Ship</th>
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
