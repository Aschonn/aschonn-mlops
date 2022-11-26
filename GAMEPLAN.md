Notes:
Finding out that everything is versioned. So one can revert back, thus reducing risk. 



Pipeline main objectives:
1) Data validations for specific models (monitoring models)
    
    <img src="whymonitormodels.png">

    Things to learn: 

    - Does a feature store remove this possibility? 
    - Does it require pointers to specific date for data

2) Data (data drift detection)

    - Features stores are commonly used to store large amounts of data. They are also perfect for keeping track of changes in data and versions it. By keeping track of previous version we can assess frequency, standard deviation, average, which helps us assess feature drift, if they arise. Changes like prefernce from a customer can cause this. 
    
    Key aspects to keep track of:
    1) Changes to anything (literally) and have backups
    2) Changes of data from training to production and how that effects results.
    3) Detect outliers and useless data that effects performance (pca or removal or allocation)

    Things to learn: 
     - Determine features sensitivity
     - Create metrics for distributions on production vs training data/outputs (statisitics)
     - What is an evaluation store?



3) Models


