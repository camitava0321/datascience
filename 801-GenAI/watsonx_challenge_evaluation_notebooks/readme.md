# How to setup notebook environment

Due to the volume of participants (around 150,000) we are asking users to use a local machine to run notebooks as the preferred option.

Please see here for instructions on setting up a notebook environmnent on your local machine.
https://w3.ibm.com/w3publisher/watsonx-ai-challenge-extra-details/setting-up-a-notebook-environment
and 
https://w3.ibm.com/w3publisher/watsonx-ai-challenge-extra-details
for more general points on why this is the recommended path.

Please use Python 3.10 environment for running notebooks.


## Running sample notebooks

### Edit the `Data loading` section in the notebook
If the dataset location is different than one in the notebook it needs to be updated.
```python
read_csv("train.csv")
```

Pass the correct filename/filepath to `read_csv()` method.

## Troubleshooting

### Missing packages
In case the missing package error occurs, it can be installed by adding code cell in the notebook with command:
```cmd
!pip install missing_package_name
```

**Note:** the kernel restart may be required.

