# ECScore
Code is freely avaiable for use in Jupyter Notebook format (ecscore_total.ipynb) with additional fingerprinting methods or a stand-alone callable file (ecscores.py)!

**CSV-Setup and Data Interpretation from Website or Jupyter Notebook**

Information on how to set up your CSV structure for calculating scores.

![csv_structure](https://github.com/user-attachments/assets/95f697da-a8b3-48e0-92ce-126f26a1240f)

Information on interpreting the output file.

![csv_output](https://github.com/user-attachments/assets/fcdb14a3-697a-4acb-800d-83d0a3c1f610)

**Stand-alone python script**

Requirements

-RDKit

Example usage

from ecscores import ecscore

initial_smile "CCO"

final_smile = "CCCO"

score = ecscore(initial_smile, final_smile)

print(score) #e.g. 0.6

For questions, comments, or concerns, please contact John-Paul Webster at john-paul.webster@yale.edu
