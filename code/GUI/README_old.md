# Deep Learning HFO Detector GUI

## Overview
The Deep Learning HFO Detector is a Python-based project aimed at detecting High Frequency Oscillations (HFOs) using deep learning techniques. This project provides a graphical user interface (GUI) for easy interaction. 

The provided GUI takes an .edf SEEG signal which may be in bipolar or raw format and outputs the model's predictions for HFO (ripples and fast-ripples) positions in the signal. These predictions can be saved in a .mrk file which may be opened as any .txt file. However we suggest the use of AnyWave for simultaneous visualization of the signal and provided predictions.

### Models Provided

The HFO detector is based on LSTM architecture which analyses small segments of bipolar SEEG signals with a sampling frequency of 2048 Hz and provides a binary prediction if that window includes a HFO or not.

Due to the importance of differentiating between ripples and fast-ripples, two models are provided, one each for the detection of both sub-types of HFOs.

These predictions are then post-processed in order to provide approximations for the position of each detected HFO.

## Installation

### Installation of required software

1. Download and install python from the [official website](https://www.python.org/). Python is necessary for the GUI usage

2. Download and install Anaconda from the [official website](https://www.anaconda.com/products/distribution). Anaconda is used for managing virtual environments and package dependencies.

3. Download and install Visual Studio Code (VSCode) from the [official website](https://code.visualstudio.com/). VSCode is recommended for code editing and development, but any text editor can be used.

### Installation of GUI
To run the Deep Learning HFO Detector, follow these steps:

1. Download the project folder from the repository by clicking on the "Code" button and selecting "Download ZIP" from the dropdown menu. Alternatively, you can clone the repository to your local machine using Git:

```bash 
git clone https://github.com/NCN-Lab/deepHFO
```

2. Extract the downloaded ZIP file (if applicable) to a location of your choice.

3. Open the project folder in Visual Studio Code (VSCode):
- Launch VSCode.
- Select "File" > "Open Folder" from the menu.
- Navigate to the location where you extracted the project folder and select it.

4. Use VSCode terminal to create a Conda virtual environment using the provided conda_environment.yml file:
```bash 
conda env create -f virtual_environment.yml
```

5. Use VSCode terminal to activate the virtual environment:
```bash 
conda activate hfo-detector-env
```

## Usage

To run the Deep Learning HFO Detector, execute the __main__.py file:

```markdown 
python __main__.py
```

This will open the GUI interface, allowing users to interact with the application.

### Bipolar Data Configuration
Before running the code, ensure to configure the `BIPOLAR_DATA` variable in the `__main__.py` file according to your data format:
- If your data is already in bipolar format, set `BIPOLAR_DATA = True`.
- If your data is not in bipolar format, set `BIPOLAR_DATA = False` and your data will be pre-processed accordingly.

Example:
```python
# Set BIPOLAR_DATA to True if your data is already in bipolar format
BIPOLAR_DATA = True
```

## Example Signal
An example signal (`example_signal_synthetic.edf`) is provided in the repository for testing purposes. The example signal was obtained from Roehri, N., Pizzo, F., Bartolomei, F., Wendling, F., & Bénar, C.-G. (2018). Simulation Dataset of SEEG signal for HFO detector validation (Version 3). figshare. https://doi.org/10.6084/m9.figshare.4729645.v3.

### Usage
To use the example signal, simply select the corresponding file when interacting with the interface

### Result Evaluation
For easier visualization of the predictions, we suggest visualizing the results using AnyWave (https://meg.univ-amu.fr/wiki/AnyWave). For this the same example signal can be found in .ades format inside the results folder, along with the detector's predictions.


## Requirements
- Python 3.10
- Conda (for managing virtual environments)
- AnyWave (only for visualization of signal and results)

## Additional Notes
- Make sure to have Anaconda and Visual Studio Code installed before proceeding with the installation and usage steps.