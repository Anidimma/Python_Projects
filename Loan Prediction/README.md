<p align="center">  <img src="https://www.flaticon.com/svg/vstatic/svg/1907/1907675.svg?token=exp=1619058683~hmac=94f8723ec6c7d1db993a6d6fff2a46ee" width = "100"> </p>

<h1 align="center"> LOAN PREDICTION PROJECT </h1>


## Context
Objective of the work is to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others.


```

```

## Modules Used
```python
import pandas as pd
from imblearn.over_sampling import SMOTE
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm      
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
plt.style.use('seaborn-dark')
sns.set()
```

## Best Performing Model
![](SourceImages/RandomForest.PNG)
