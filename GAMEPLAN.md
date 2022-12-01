Notes:
Finding out that everything is versioned. So one can revert back, thus reducing risk. 



Pipeline main objectives:
1) Data validations for specific models (monitoring models)
    
    <img src="https://raw.githubusercontent.com/Aschonn/aschonn-mlops/main/whymonitormodels.PNG">

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

    1) monitoring for:
    - performance in production
    - Prediction performance
    - components
    - version
    - security threats.
    - Shifts (of preference)
        + solution: 
            - create a manual solution if it's seasonal
            - recreate the model
            - Online learning algorithms (given the right situation
            
    2) Model configuration and artifacts

    config:
    
        Training dataset location and version,
        Test dataset location and version,
        Hyperparameters used,
        Default feature values,
        Dependencies and their versions; you want to monitor changes in dependency versions to easily find them for root cause analysis when model failure is caused by dependency changes,
        Environment variables,
        Model type (classification vs regression),
        Model author,
        Target variable name,
        Features to select from the data,
        Code and data for testing scenarios,
        Code for the model and its preprocessing.

    
    Security: 
    - Adversial Attacks: Example: injecting information that skews the prediction of the model. The solution: still ongoing research on algorithms to detect anomolies. Most of the times certain events are manually added to detect suspicious behavior. 
    - https://github.com/Trusted-AI/adversarial-robustness-toolbox
    <img src="https://raw.githubusercontent.com/Trusted-AI/adversarial-robustness-toolbox/main/docs/images/white_hat_blue_red.png">


    4) Model Evaluation: 

    <img src="https://lh3.googleusercontent.com/z-wRX1FekAqLXRJnS5G8naTQXJACI5or9cXIIsxJkApS9xWOKxUU_CBbqfjl8mThVsM475NVmAxpQGQy_CgH4PO2H4b95HaPI_K5gM1aZ-urNcSkH9DAHehoJC3HI4oQfuVbT_3N">


    Classification: Accuracy, confusion matrix, ROC-AUC score, Previsiion and recall scores, and f1-score

    Regression: Root mean Square Error, R-Squared and Ajusted R-Square metrics, mean absolute error, mean absolute percentage error. 



    5) Operational Level Monitoring:

    Three main segments:

        1) Systems Performane Requirements: CPU/GPU, Memory, Fail request management and tracking, Response Time, number of API Calls, and system reliability
        2) Data Pipeline Monitoring: Input data, Intermediate Workflow Steps (ex: Accepting different input files), Output data, and data quality 
        3) Model Pipeline: Keep track of dependencies and log it in pipeline of metadata.
